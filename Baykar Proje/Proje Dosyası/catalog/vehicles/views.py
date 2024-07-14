from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Vehicle

# Create your views here.

def index(request):
    vehicles = Vehicle.objects.all()

    context = {
        'vehicles': vehicles
    }
    return render(request, 'vehicles/list.html', context)

def detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk = vehicle_id)
    context = {
        'vehicle': vehicle
    }
    return render(request, 'vehicles/detail.html', context)

def search(request):
    return render(request, 'vehicles/search.html')

