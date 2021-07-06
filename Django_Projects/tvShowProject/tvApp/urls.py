from django.urls import path
from . import views
urlpatterns =[
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.addShow),
    path('shows/create', views.create_show),
    path('shows/<int:shows_id>', views.show_show),
    path('shows/<int:shows_id>/edit', views.edit_show),
    path('shows/<int:shows_id>/update', views.update_show),
    path('shows/<int:shows_id>/destroy', views.destroy_show),
]