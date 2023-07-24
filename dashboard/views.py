from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def freelencing(request):
    return render(request, 'dashboard/freelencing.html')

def resource(request):
    return render(request, "dashboard/resource.html")


@login_required(login_url='login')
def dashboard(request):
    return render(request, "dashboard/dashboard.html")