from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort', 'name')
    phones_objects = Phone.objects.all()

    if sorting == 'name':
        phones_objects = phones_objects.order_by('name')
    elif sorting == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sorting == 'max_price':
        phones_objects = phones_objects.order_by('-price')

    context = {
        'phones': phones_objects,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.get(slug=slug)
    context = {
        'phone': phone_objects
    }
    return render(request, template, context)
