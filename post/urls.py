from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.showout,name="base"),
    path("list",views.base,name="boom")
]