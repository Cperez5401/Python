from django.shortcuts import render, redirect
from .models import *

def index (request):
    context ={
        "users":user.objects.all()
    }
    # user.objects.create(name="Christian Perez", email="Cperez@gmail.com", age="19")
    # user.objects.create(name="LeBron James", email="kingJames@gmail.com", age="36")
    # user.objects.create(name="Peter Parker", email="spiderman@gmail.com", age="43")

    return render(request, 'index.html', context)

def addUser (request):
    print(request.POST)

    user.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        age=request.POST['Age']
    )

    return redirect("/")