from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "kratosubz/index.html")
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        full_name = request.POST.get('name')  # Optional: full name field

        if not all([username, email, password1, password2]):
            messages.error(request, 'Please fill out all fields.')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.first_name = full_name or ''  # Store name if provided
        user.save()

        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'kratosubz/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')  # Change this to your homepage/dashboard URL name
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')

    return render(request, 'kratosubz/login.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            # In real use, send email with reset link
            messages.success(request, 'If that email is registered, a reset link will be sent.')
        else:
            messages.error(request, 'No user found with that email.')
        return redirect('forgot_password')

    return render(request, 'kratosubz/forgot_password.html')

def blog(request):
    return render(request, "kratosubz/blog.html")
def about_us(request):
    return render(request, "kratosubz/about_us.html")
def reseller(request):
    return render(request, "kratosubz/reseller.html")

@login_required
def dashboard(request):
    return render(request, "kratosubz/dashboard.html")
def forgot_password(request):
    return render(request, "kratosubz/forgot_password.html")
def post_1(request):
    return render(request, "kratosubz/blogpost1.html")
def post_2(request):
    return render(request, "kratosubz/blogpost2.html")
def post_3(request):
    return render(request, "kratosubz/blogpost3.html")
def post_4(request):
    return render(request, "kratosubz/blogpost4.html")
def post_5(request):
    return render(request, "kratosubz/blogpost5.html")
def post_6(request):
    return render(request, "kratosubz/blogpost6.html")
def post_7(request):
    return render(request, "kratosubz/blogpost7.html")
def post_8(request):
    return render(request, "kratosubz/blogpost8.html")
def post_9(request):
    return render(request, "kratosubz/blogpost9.html")
def post_10(request):
    return render(request, "kratosubz/blogpost10.html")

