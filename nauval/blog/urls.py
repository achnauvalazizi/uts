from django.shortcuts import render
from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('',views.blog),
    path('admin/', admin.site.urls),
]
