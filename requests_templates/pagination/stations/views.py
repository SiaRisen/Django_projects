from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        stations = [row for row in reader]
        paginator = Paginator(stations, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
