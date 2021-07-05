from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('book/results', views.book_results),
    path('book/<int:id>', views.display_book),
    path('book/<int:book_id>/add_author', views.add_author),
    path('author',views.author),
    path('author/results',views.author_results),
    path('author/<int:author_id>',views.display_author),
    path('author/<int:author_id>/add_book', views.add_book),

]