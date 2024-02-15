from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserAddress
from django.contrib.auth.models import User
from .models import UserMobile
from cart_management.models import OrderDetails
from django.contrib import messages
from wallet.models import Wallet
import re

# Create your views here.
@login_required(login_url='home:signin')
def userProfile(request):
    user = request.user
    print(user)
    
    try:
        mobile = UserMobile.objects.filter(user=user)
    except UserMobile.DoesNotExist:
        mobile = None

    return render(request,'user_details/user_profile.html',{'user': user,'mobile': mobile})

@login_required(login_url='home:signin')
def user_address(request):
    user = request.user
    addresses = UserAddress.objects.filter(user=user)
    
    return render(request,'user_details/user_address.html', {'user': user, 'addresses': addresses} )

@login_required(login_url='home:signin')
def add_user_address(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        landmark = request.POST.get('landmark')

        user_address = UserAddress(
            user=user,
            name=name,
            pincode=pincode,
            address=address,
            city=city,
            district=district,
            state=state,
            landmark=landmark,
            locality = locality
        )
        # Save the instance to the database
        user_address.save()
        return redirect('user_profile:user_address')
    return render(request,'user_details/add_user_address.html')

@login_required(login_url='home:signin')
def add_user_mobile(request):
    if request.method == 'POST':
        user = request.user
        mobile = request.POST.get('mobile')

        # Ensure the mobile number contains exactly 10 digits
        if not mobile.isdigit() or len(mobile) != 10:
            # The mobile number does not meet the required format
            error_message = 'Invalid mobile number format. Please enter a 10-digit number.'
            messages.error(request, error_message)
            return render(request, 'user_details/add_user_mobile.html', {'error_message': error_message})

        # Create a new UserMobile object with the user and mobile number
        user_mobile = UserMobile(
            user=user,
            mobile_number=mobile
        )

        # Save the UserMobile object to the database
        user_mobile.save()

        # Redirect to the user profile page after saving the mobile number
        return redirect('user_profile:user_profile')

    # If the request method is not POST, render the add_user_mobile.html template
    return render(request, 'user_details/add_user_mobile.html')

@login_required(login_url='home:signin')
def add_user_firstname(request):
    if request.method == 'POST':
        user = request.user
        firstname = request.POST.get('firstname').strip()  # Remove leading and trailing whitespaces

        # Validate if firstname is not empty or just whitespace
        if not firstname:
            error_message = 'Please enter a valid first name.'
            messages.error(request, error_message)
            return redirect('user_profile:add_user_firstname')  # Redirect to the same page to display the error message

        # Update user details
        user.first_name = firstname

        # Save the changes
        user.save()

        return redirect('user_profile:user_profile')

    # If the request method is not POST, render the add_user_firstname.html template
    return render(request, 'user_details/add_user_firstname.html')

@login_required(login_url='home:signin')
def add_user_lastname(request):
    if request.method == 'POST':
        user = request.user
        lastname = request.POST.get('lastname').strip()  # Remove leading and trailing whitespaces

        # Validate if lastname is not empty or just whitespace
        if not lastname:
            error_message = 'Please enter a valid last name.'
            messages.error(request, error_message)
            return redirect('user_profile:add_user_lastname')  # Redirect to the same page to display the error message

        # Update user details
        user.last_name = lastname

        # Save the changes
        user.save()

        return redirect('user_profile:user_profile')

    # If the request method is not POST, render the add_user_lastname.html template
    return render(request, 'user_details/add_user_lastname.html')

@login_required(login_url='home:signin')
def delete_user_address(request,id):
    address=UserAddress.objects.get(id=id)
    address.delete()
    return redirect('user_profile:user_address')

@login_required(login_url='home:signin')
def user_order(request):
    user=request.user
    user_orders = OrderDetails.objects.filter(user=user).order_by('-id')
    return render(request,'user_details/user_order.html',{"order":user_orders})

@login_required(login_url='home:signin')
def cancel_order(request, id):
    try:
        order_detail = OrderDetails.objects.get(id=id)

        # Update the order status to 'Cancelled'
        order_detail.order_status = 'Cancelled'
        order_detail.save()
        order_detail.product_variant.quantity += order_detail.product_quantity
        order_detail.product_variant.save()

        # Check if the payment method is 'Paypal'
        if order_detail.payment and (order_detail.payment.payment_type == 'Paypal' or  order_detail.payment.payment_type == 'Wallet'):
            # Add the total price of the canceled order to the user's wallet
            try:
                wallet = Wallet.objects.get(user=request.user)
                wallet.balance += order_detail.product_price * order_detail.product_quantity
                wallet.save()
                
                
            except Wallet.DoesNotExist:
                # Handle the case where the user doesn't have a wallet yet
                messages.error(request, "User's wallet not found.")
        else:
            messages.success(request, f"Order #{order_detail.id} has been cancelled.")
            
    except OrderDetails.DoesNotExist:
        # Handle the case where the order detail does not exist
        messages.error(request, "Order not found.")

    return redirect('user_profile:user_order')

@login_required(login_url='home:signin')
def refund_order(request,id):
    print(id)
    product = OrderDetails.objects.get(id = id)
    product.order_status = 'Refund'
    product.save()
    return redirect('user_profile:user_order')

@login_required(login_url='home:signin')
def replacement_order(request,id):
    print(id)
    product = OrderDetails.objects.get(id = id)
    product.order_status = 'Replacement'
    product.save()
    return redirect('user_profile:user_order')

@login_required(login_url='home:signin')
def edit_user_mobile(request):
    user = request.user
    user_mobile = UserMobile.objects.get(user=user)
    if request.method == 'POST':
        user = request.user
        mobile = request.POST.get('mobile')

        # Ensure the mobile number contains exactly 10 digits
        if not mobile.isdigit() or len(mobile) != 10:
            # The mobile number does not meet the required format
            error_message = 'Invalid mobile number format. Please enter a 10-digit number.'
            messages.error(request, error_message)
            return redirect('user_profile:edit_user_mobile')  # Redirect to the same page to display the error message

        # Check if the user already has a mobile number, and update it if exists
        try:
            user_mobile = UserMobile.objects.get(user=user)
            user_mobile.mobile_number = mobile
        except UserMobile.DoesNotExist:
            # If the user does not have a mobile number, create a new UserMobile object
            user_mobile = UserMobile(user=user, mobile_number=mobile)

        # Save the UserMobile object to the database
        user_mobile.save()

        return redirect('user_profile:user_profile')

    # If the request method is not POST, render the edit_user_mobile.html template
    return render(request, 'user_details/edit_user_mobile.html',{'mobile':user_mobile})

@login_required(login_url='home:signin')
def edit_user_firstname(request):
    user = request.user

    if request.method == 'POST':
        firstname = request.POST.get('firstname', '').strip()

        # Check if firstname is not just a space
        if not firstname:
            messages.error(request, 'Please enter a valid first name.')
            return redirect('user_profile:edit_user_firstname')

        # Update user details
        user.first_name = firstname

        # Save the changes
        user.save()
        return redirect('user_profile:user_profile')

    return render(request, 'user_details/edit_user_firstname.html', {'firstname': user.first_name})

@login_required(login_url='home:signin')
def edit_user_lastname(request):
    user = request.user

    if request.method == 'POST':
        lastname = request.POST.get('lastname', '').strip()

        # Check if lastname is not just a space
        if not lastname:
            messages.error(request, 'Please enter a valid last name.')
            return redirect('user_profile:edit_user_lastname')

        # Update user details
        user.last_name = lastname

        # Save the changes
        user.save()
        return redirect('user_profile:user_profile')

    return render(request, 'user_details/edit_user_lastname.html', {'lastname': user.last_name})

@login_required(login_url='home:signin')
def add_address_checkout(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        locality = request.POST.get('locality')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        landmark = request.POST.get('landmark')

        user_address = UserAddress(
            user=user,
            name=name,
            pincode=pincode,
            address=address,
            city=city,
            district=district,
            state=state,
            landmark=landmark,
            locality = locality
        )
        # Save the instance to the database
        user_address.save()
        return redirect('cart_management:cart_checkout')
    return render(request,'user_details/add_user_address.html')

@login_required(login_url='home:signin')
def more_order_details(request,id):
    user=request.user
    user_order = get_object_or_404(OrderDetails, id=id, user=user)
    return render(request,'user_details/more_order_details.html',{'order':user_order})

@login_required(login_url='home:signin')
def invoice(request,id):
    user=request.user
    user_order = get_object_or_404(OrderDetails, id=id, user=user)
    return render(request,'user_details/invoice.html',{'order':user_order})