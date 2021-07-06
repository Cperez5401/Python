import bcrypt
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash
        )

        request.session['uuid'] = user.id

        return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['uuid'] = user.id
    return redirect('/dashboard ')

def dashboard(request):
    if "uuid" not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id = request.session['uuid'])
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    del request.session['uuid']
    return redirect('/')