from django.shortcuts import render
# Note: The stuff above this will already be in this file.
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    ]

