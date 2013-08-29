# Create your views here.
from pm.models import *
from django.shortcuts import render, get_object_or_404

def home(request):
    cources = Cource.objects.all()
    return render(request, 'home.html', {'cources' : cources})

def cource(request, id):
    cource = get_object_or_404(Cource, pk=id)
    return render(request, 'cource.html', {'cource' : cource})

def schedule(request, id):
    cource = get_object_or_404(Cource, pk=id)
    return render(request, 'schedule.html', {'cource' : cource})

def progress(request, id):
    cource = get_object_or_404(Cource, pk=id)
    progress = cource.progress_set.latest()
    return render(request, 'progress.html', {
                'cource' : cource,
                'progress' : progress,
            })

    