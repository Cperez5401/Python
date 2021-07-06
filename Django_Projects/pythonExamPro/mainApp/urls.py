from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('dashboard', views.dashboard),
    path('trips/new', views.newTrip),
    path('trips/create', views.createTrip),
    path('trips/<int:tripId>', views.displayTrip),
    path('trips/<int:tripId>/edit', views.editTrip),
    path('trips/<int:tripId>/update', views.updateTrip),
    path('trips/<int:tripId>/destroy', views.destroyTrip),
]