"""Ekal_Shiksha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from webpages import views
from portal import views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from webpages.sitemap import *
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'StaticSitemap': StaticSitemap,
    'articles': ArticleSitemap,
    'course': CourseSitemap,
    'Science': CourseScienceSitemap,
    'Commerce': CourseCommerceSitemap,
    'Humanities': CourseHumanitiesSitemap,
    'Study_course': StudyGrade,
    'Study_course1': StudyGrade1,
    'Study_course2': StudyGrade2,
    'Study_course3': StudyGrade3,
    'Study_Subject': StudySubject,
    'Study_Subject1': StudySubject1,
    'Study_Subject2': StudySubject2,
    'Study_Subject3': StudySubject3,
    'Micro':Micro,
    }


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml',sitemap,{'sitemaps': sitemaps}, name='sitemap'),
    path('',include('webpages.urls'),name='index'),
    path('portal',include('portal.urls'),name='portal'),
    path('accounts/',include('allauth.urls'))

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = 'webpages.views.error_404'
# handler500 = 'webpages.views.error_500'