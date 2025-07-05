from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile 

# Create your views here.
def index(request):
    return render(request, "kratosubz/index.html")
    
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
        user.save()

        # Save phone number (assuming Profile model is linked to User)
        Profile.objects.create(user=user, phone=phone)

        # Log the user in automatically
        auth_login(request, user)

        messages.success(request, 'Registration successful. Welcome!')
        return redirect('dashboard')

    return render(request, 'kratosubz/register.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
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
    if request.user.is_authenticated:
        return redirect('dashboard')
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

