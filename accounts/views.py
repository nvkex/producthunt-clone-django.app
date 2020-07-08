from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def signup(request):
    if request.method == 'POST':
        # signed up
        if request.POST['pass'] == request.POST['cnfpass']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password = request.POST['pass'])
                auth.login(request, user)
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'error': ' Password doesnt match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # trying to login
        user = auth.authenticate(username = request.POST['loginusrname'], password = request.POST['loginpass'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or Password is incorrect!'})
    
    return render(request, 'accounts/login.html')

def logout(request):
    # TODO Route to home page
    # and logout
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
