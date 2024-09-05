from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignupForm, LoginForm, ResearchForm,InnovationForm
from .models import User





from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import login_required





def home(request):

    return render(request,"index.html")

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.password = form.cleaned_data['password']
#             user.save()
#             return redirect('login')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from .forms import SignupForm, LoginForm
from .models import User
# def login_view(request):
#     form = None  # Initialize form with None to avoid the UnboundLocalError
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             try:
#                 user = User.objects.get(email=email)
#                 if user.password == password:
#                     auth_login(request, user)
#                     return redirect('home')
#                 else:
#                     form.add_error(None, 'Invalid email or password')
#             except User.DoesNotExist:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = LoginForm()  # Ensure form is initialized here

#     return render(request, 'login.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('login')


# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # After signup, redirect to the login page
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             try:
#                 user = User.objects.get(email=email)
#                 if check_password(password, user.password):
#                     auth_login(request, user)
#                     return redirect('dashboard')
#                 else:
#                     form.add_error(None, 'Invalid email or password')
#             except User.DoesNotExist:
#                 form.add_error(None, 'Invalid email or password')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})

from django.contrib.auth.hashers import make_password

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password before saving
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # After signup, redirect to the login page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .models import User

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                if check_password(password, user.password):
                    print(f"Login successful for user: {user.email}")  # Debug line
                    auth_login(request, user)
                    return redirect('dashboard')
                else:
                    print("Password check failed")  # Debug line
                    form.add_error(None, 'Invalid email or password')
            except User.DoesNotExist:
                print("User does not exist")  # Debug line
                form.add_error(None, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



@login_required
def dashboard_view(request):
    print(f"User authenticated: {request.user.is_authenticated}")  # Debug line
    return render(request, 'dashboard.html')

#research
def research_create_view(request):
    if request.method == 'POST':
        form = ResearchForm(request.POST)
        if form.is_valid():
            form.save()
            # Re-render the form with a success message
            return render(request, 'create-research.html', {'form': form, 'success': True})
        else:
            # Re-render the form with errors
            return render(request, 'create-research.html', {'form': form, 'success': False})
    else:
        form = ResearchForm()
    
    return render(request, 'create-research.html', {'form': form})


#innovation
def innovation_create_view(request):
    if request.method == 'POST':
        form = InnovationForm(request.POST)
        if form.is_valid():
            form.save()
            # Re-render the form with a success message
            return render(request, 'innovation_form.html', {'form': form, 'success': True})
        else:
            # Re-render the form with errors
            return render(request, 'innovation_form.html', {'form': form, 'success': False})
    else:
        form = InnovationForm()
    
    return render(request, 'innovation_form.html', {'form': form, 'success': False})


