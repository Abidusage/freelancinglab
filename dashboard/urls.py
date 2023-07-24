from django.urls import path
from . import views

urlpatterns = [
    path('', views.freelencing, name='freelencing'),
    path('resource', views.resource, name="resource"),
    path('dashboard', views.dashboard, name="dashboard"),
]