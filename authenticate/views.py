from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm

def home(request): 
    return render(request, 'authenticate/home.html', {})

def login_user(request):
    if request.method == 'POST': 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Successfully Logged In!'))
            return redirect('home')
        else:
            messages.success(request, ('Error.  Please Try Again.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Successfully Logged Out'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, ('You Are Now Registered'))
            return redirect('home')


    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your Profile Has Been Edited'))
            return redirect('home')
    else:
        form = EditProfileForm(instance= request.user)

    context = {'form': form}


def change_password(request)

