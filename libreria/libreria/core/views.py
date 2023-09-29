from django.shortcuts import render

def home (request):
    return render(request, "core/home.html")


def libro (request):
    return render(request, "core/anime-details.html")