from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, UserProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import UserProfile, Cart, CartItem, Product


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def add_to_cart(request, product_id):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(pk=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return render('/cart')

@login_required(login_url='/login')
def remove_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('.cart')

@login_required(login_url='/login')
def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    
    return render(request, 'cart.html', {'cart_items':cart_items, 'user_cart':user_cart})





@login_required(login_url='/login')
def shopGrid(request):
    return render(request, 'shop-grid.html')


"""
_summary_
creating a function for the signup page
"""
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account has successfully been created.')
            return redirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})


def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Successful login.')
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def userLogout(request):
    logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login.html')






"""_summary_
"""
@login_required(login_url='/login')
def userAccount(request):
    user = request.user
    try:
        profile = user.userprofile  # Try to access the UserProfile
    except UserProfile.DoesNotExist:
        # Handle the case where UserProfile doesn't exist
        profile = UserProfile.objects.create(user=user)
        
    user_form = UserUpdateForm(instance=request.user)
    profile_form = UserProfileUpdateForm(instance=request.user.userprofile)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile account saved.')
            return redirect('/profile')
        
    return render(
		request, 
		'profile.html', {
			'user_form':user_form, 
			'profile_form': profile_form,
			'user':user,
			'profile':profile,
		}
	)
    
