from multiprocessing import context
import re
from django.shortcuts import render, redirect
from .models import *

def index(request):
    books = Books.objects.all()
    return render(request, 'Add_Books.html', {'books': books})

def AddBook(request):
    if request.method == 'POST':
        new_book = Books.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc']
        )
        return redirect('/')

def InfoBook(request, book_id):
    context={
        'book':Books.objects.get(id=book_id),
        'authors':Authors.objects.all()
    } 
    return render(request,'Info_Books.html',context)

def delete(request, book_id):
    book = Books.objects.get(id=book_id)
    book.delete()
    return redirect('/')

def author(request):
    context={
        'authors':Authors.objects.all()
    }
    return render(request, 'Add_Author.html', context)

def AddAuthor(request):
    if request.method=='POST':
        _newAuthor=Authors.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes'],
        )
        _newAuthor.save()
        return redirect('/authors')


def InfoAuthor(request, author_id):
    author = Authors.objects.get(id=author_id)
    context = {
        'books': Books.objects.all(),
        'author': author,
    }
    return render(request, 'Info_Author.html', context)

def delete_author(request, author_id):
    author = Authors.objects.get(id=author_id)
    author.delete()
    return redirect('/authors')

def AddAuthor_Book(request, book_id):
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        book = Books.objects.get(id=book_id)
        author = Authors.objects.get(id=author_id)
        book.authors.add(author)
    return redirect('info_book', book_id=book_id)


def assign_author(request, author_id):
    book = Books.objects.get(id=request.POST['book_id'])
    author = Authors.objects.get(id=author_id)
    book.authors.add(author)
    return redirect(f'/authors/{author_id}')