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
    return redirect('/dashboard')


def dashboard(request):
    if "uuid" not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id = request.session['uuid']),
        'trips': Trips.objects.all()
    }
    return render(request, 'dashboard.html', context)


def logout(request):
    del request.session['uuid']
    return redirect('/')


def newTrip(request):
    if "uuid" not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id = request.session['uuid'])
    }
    return render(request, 'addTrip.html', context)


def createTrip(request):
    errors = Trips.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/new')
    else:
        createTrip = Trips.objects.create(
                user = User.objects.get(id=request.session['uuid']),
                destination=request.POST['destination'],
                startDate=request.POST['startDate'],
                endDate=request.POST['endDate'],
                plan=request.POST['plan']
            )
        return redirect('/dashboard')


def displayTrip(request, tripId):
    context = {
        'user': User.objects.get(id = request.session['uuid']),
        'trip':Trips.objects.get(id=tripId)
    }

    return render(request, 'displayTrip.html', context)


def editTrip(request, tripId):
    context = {
        'user': User.objects.get(id = request.session['uuid']),
        'trips':Trips.objects.get(id=tripId)
    }
    return render(request, 'editTrips.html', context)


def updateTrip(request, tripId):
    errors = Trips.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/trips/new')
    else:
        trip = Trips.objects.get(id=tripId)

        trip.destination=request.POST['destination']
        trip.startDate=request.POST['startDate']
        trip.endDate=request.POST['endDate']
        trip.plan=request.POST['plan']
        trip.save()
        return redirect('/dashboard')


def destroyTrip(request, tripId):
    trip = Trips.objects.get(id= tripId)

    trip.delete()

    return redirect('/dashboard')

