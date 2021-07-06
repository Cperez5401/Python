from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *


def index(request):
    return redirect('/shows')


def shows(request):
    context = {
        'shows': Shows.objects.all()
    }
    return render(request, 'shows.html', context)


def addShow(request):
    return render(request, 'addshow.html')


def create_show(request):
    errors = Shows.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        createShow = Shows.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description']
        )
        return redirect('/shows/{ createShow.id }')


def show_show(request, shows_id):
    context = {
        'shows':Shows.objects.get(id=shows_id)
    }

    return render(request, 'display_show.html', context)


def edit_show(request, shows_id):
    context = {
        'shows':Shows.objects.get(id=shows_id)
    }
    return render(request, 'edit_show.html', context)


def update_show(request, shows_id):
    errors = Shows.objects.validate(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        show = Shows.objects.get(id=shows_id)

        show.title=request.POST['title']
        show.network=request.POST['network']
        show.release_date=request.POST['release_date']
        show.description=request.POST['description']
        show.save()
        return redirect(f'/shows/{ show.id }')


def destroy_show(request, shows_id):
    show = Shows.objects.get(id= shows_id)

    show.delete()

    return redirect('/shows')