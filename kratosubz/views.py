from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "kratosubz/index.html")
    
def register(request):
    if request.method == 'POST':
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

        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, 'Registration successful. You can now log in.')
        return redirect('login')

    return render(request, 'kratosubz/register.html')
def login(request):
    return render(request, "kratosubz/login.html")
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

