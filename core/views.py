from django.shortcuts import render, redirect
from .forms import SignUpForm, UserUpdateForm, UserProfileUpdateForm, ContactProfile, NewsLetterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import UserProfile, Cart, CartItem, Product, ContactModel, NewsLetter



# Create your views here.
def base(request):
    return render(request, 'base.html')



@login_required(login_url='/login')
def home(request):
    return render(request, 'index.html')

@login_required(login_url='/login')
def blog_single(request):
    return render(request, 'blog-single.html')


@login_required(login_url='/login')
def contact(request):
    if request.method == 'POST':
        form = ContactProfile(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message has been saved.')
            return redirect('/contact')
    else:
        form = ContactProfile()
    return render(request, 'contact.html', {'form':form})



"""
_summary_
newsletter function
"""
@login_required(login_url='/login')
def newsLetter(request):
    if request.method == 'POST':
        newsletter = NewsLetterForm(request.POST)
        if newsletter.is_valid():
            newsletter.save()
            messages.success(request, 'Thank you for Subscribing.')
        return redirect('/index')
    else:
        newsletter = NewsLetterForm()
    return redirect('/home', {'newsletter': newsletter})


"""
create a function for adding to the cart item
"""
@login_required(login_url='/login')
def add_to_cart(request, product_id):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    product = Product.objects.get(pk=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return render('/cart')

"""
create a function for removing the cart item
"""
@login_required(login_url='/login')
def remove_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(pk=cart_item_id)
    cart_item.delete()
    return redirect('/cart')


"""
create a function for viewing the cart item
"""
@login_required(login_url='/login')
def view_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    
    return render(request, 'cart.html', {'cart_items':cart_items, 'user_cart':user_cart})





"""
_summary_
create a shop grid function
"""
@login_required(login_url='/login')
def shopGrid(request):
    return render(request, 'shop-grid.html')


"""
_summary_
creating a function for the User registration 
"""
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})



"""
created a User login function for already created user.
"""
def signIn(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,  username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Successful login.')
                return redirect('/home')
            else:
                # If authentication fails, add an error message to the form
                form.add_error(None, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})



"""
created a function for logout that have an arg of request

"""
@login_required(login_url='/login')
def userLogout(request):
    logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login.html')






"""_summary_
	user account
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
