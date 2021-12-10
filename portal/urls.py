from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView
from . import views
from django.urls import include, re_path

urlpatterns = [

    path('',login.as_view(),name='login'),

]