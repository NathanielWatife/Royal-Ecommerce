from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html')

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
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form':form})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def userLogout(request):
    logout(request)
    return redirect('login.html')