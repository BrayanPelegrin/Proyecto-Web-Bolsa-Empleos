# Django
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Owns 
from .forms import SignupForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login(request, user)
            messages.success(request, 'Welcome {}'.format(user.username))

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('home')
        else:
            messages.error(request, "Password or Username doesn't match")

    return render(request, './login/login.html', {})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = SignupForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'User created succesfully')
            return redirect('login')

    context = {'form' : form}
    return render(request, './signup/register.html', context)
