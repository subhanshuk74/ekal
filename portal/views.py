from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from .models import *
from django.views.generic import CreateView
from django.conf import settings
from django.views.generic import TemplateView
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders

# Create your views here.
class login(TemplateView):
    
    template_name = 'login.html'