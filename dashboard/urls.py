from django.urls import path
from . import views

urlpatterns = [
    path('', views.freelencing, name='freelencing'),
    path('voir_plus/detail/<int:pk>', views.voir_plus, name='voir_plus'),
]