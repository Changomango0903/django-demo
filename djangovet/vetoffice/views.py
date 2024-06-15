from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def home(request):
    context = {"name": "Spot"}
    return render(request, "vetoffice/home.html", context)