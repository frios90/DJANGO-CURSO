from django.shortcuts import render
from .models import Project


# Create your views here.
def portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'projects': projects})
    # return HttpResponse(f"{html_base}<h2>Portafolio</h2><p>Este es el portafolio</p>")
