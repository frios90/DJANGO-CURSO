from django.shortcuts import render
from .models import Regiones2020

def test (request):
    regions = Regiones2020.objects.all().order_by('cut_reg')
    context = { 'regions': regions }
    print(context)

    return render(request, "maps/map.html", context)