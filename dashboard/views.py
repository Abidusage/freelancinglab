from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def freelencing(request):
    workers = User.objects.all()
    context ={
        'workers': workers
    }
    return render(request, 'dashboard/freelencing.html', context)
    
def voir_plus(request, pk):
    workers = User.objects.get(id=pk)
    context = {
        'workers': workers,
    }
    return render(request, 'dashboard/voir_plus.html', context)
