from django.shortcuts import render
import requests

from .models import Photo, Projectphotos
from django.views.generic import ListView
# Create your views here.


def projectdisplay(request):
    projects = Projectphotos.objects.all()
    return render(request, 'projectD.html',{"projects": projects})

class AboutView(ListView):
   model = Photo
   template_name ='about.html'

