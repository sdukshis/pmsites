# Create your views here.
from pm.models import *
from django.shortcuts import render, get_object_or_404

def home(request):
    cources = Cource.objects.all()
    return render(request, 'home.html', {'cources' : cources})

    