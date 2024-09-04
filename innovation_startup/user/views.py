from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignupForm, LoginForm
from .models import User



def home(request):

    return render(request,"index.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import LoginForm  # Ensure your form is correctly imported
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

def login_view(request):
    form = None  # Initialize form with None to avoid the UnboundLocalError
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    auth_login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, 'Invalid email or password')
            except User.DoesNotExist:
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()  # Ensure form is initialized here

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')
