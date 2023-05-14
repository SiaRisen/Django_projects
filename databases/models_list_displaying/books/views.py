import datetime
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    context = {
        'books': books_objects,
    }
    return render(request, template, context)


def books_pagi(request, pub_date):
    template = 'books/books_list.html'
    books_objects = Book.objects.filter(pub_date=pub_date)
    try:
        next_page = Book.objects.filter(pub_date__gt=pub_date).values('pub_date').first()['pub_date'].strftime('%Y-%m-%d')
    except TypeError:
        next_page = None
    try:
        previous_page = Book.objects.filter(pub_date__lt=pub_date).values('pub_date').first()['pub_date'].strftime('%Y-%m-%d')
    except TypeError:
        previous_page = None
    context = {
        'books': books_objects,
        'next_page': next_page,
        'previous_page': previous_page,
    }
    return render(request, template, context)
