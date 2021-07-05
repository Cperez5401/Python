from django.shortcuts import render, redirect

from .models import *

def index(request):
    context ={
        "all_books": Books.objects.all()
    }

    return render(request, 'index.html', context)

def book_results(request):
    print(request.POST)

    Books.objects.create(
        title = request.POST['title'],
        description = request.POST['description']
    )
    return redirect('/')

def display_book(request, id):
    context = {
        "book": Books.objects.get(id = id),
        "books": Books.objects.get(id = id).authors.all(),
        "authors": Author.objects.all(),
    }
    return render(request, 'books.html', context)

def add_author(request, book_id):
    print(request.POST)
    this_book = Books.objects.get(id=book_id)
    this_author = Author.objects.get(id = request.POST["author_id"])

    this_book.authors.add(this_author)
    return redirect(f'/book/{ book_id }')


def author(request):
    context = {
        "allAuthors": Author.objects.all(),
    }

    return render(request, 'author.html', context)

def author_results(request):
    print(request.POST)

    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/author')

def display_author(request, author_id):
    context = {
        "author": Author.objects.get(id = author_id),
        "authors": Author.objects.get(id = author_id).books.all(),
        "books": Books.objects.all(),
    }
    return render(request, 'author_display.html', context)

def add_book(request, author_id):
    print(request.POST)
    this_author = Author.objects.get(id = author_id)
    this_book = Books.objects.get(id = request.POST['book_id'])

    this_author.books.add(this_book)
    return redirect(f'/author/{ author_id }')

