from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return redirect('index')  
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('index')  
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('index')  
        user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username, password=password, email=email)
        user.save()
        messages.success(request, 'User created successfully.')
    return render(request, "index.html")
