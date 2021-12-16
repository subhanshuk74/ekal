from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
from django.views.generic.base import TemplateView
from . import views
from django.urls import include, re_path

urlpatterns = [
    
    path('robots.txt',TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('', hm.as_view(), name='index'),
    path('Doubts/',Doubt.as_view(), name='Doubt'),
    path('blogs/',views.blog, name='blog'),
    url(r'^blogs/(?P<blog_id>[-\w]+)/$', views.article, name='article'),
    
    path('AboutUs/',About.as_view(), name='About'),
    url(r'^NCERT_book/chapter/(?P<Grade_Id>\w+)/$', views.chapter, name='chapter'),
    url(r'^NCERT_solution/chapter/(?P<Grade_Id>\w+)/$', views.chapter, name='chapter'),
    url(r'^Mock_Test/chapter/(?P<Grade_Id>\w+)/$', views.chapter, name='chapter'),
    url(r'^NCERT_book/(?P<Grade_Id>\w+)/$', views.Download, name='Download'),
    url(r'^Assignments/chapter/(?P<Grade_Id>\w+)/$', views.chapter, name='chapter'),
    url(r'^Assignments/(?P<Grade_Id>\w+)/$', views.Download, name='Download'),
    url(r'^NCERT_solution/(?P<Grade_Id>\w+)/$', views.Download, name='Download'),
    url(r'^Mock_Test/(?P<Grade_Id>\w+)/$', views.Download, name='Download'),
    # path('Thankyou/',Thankyou.as_view(),name='Thankyou'),
    path('StudyMaterial/',views.StudyMaterial,name='StudyMaterial'),
    url(r'^Micro/(?P<Grade_Id>\w+)/$', views.Micro, name='Micro'),
    
    path('contact/',contact.as_view(),name='contact'),
    path('work/',work.as_view(),name='work'),
    url(r'^Science/(?P<Grade_Id>\w{0,5})/$', views.Grade_Science, name='Science'),
    url(r'^Commerce/(?P<Grade_Id>\w{0,5})/$', views.Grade_Commerce, name='Commerce'),
    url(r'^Humanities/(?P<Grade_Id>\w{0,5})/$', views.Grade_Humanities, name='Humanities'),
    # url(r'^Study/(?P<Id>\w{0,5})/$', Download.as_view(), name='Study'),
    url(r'^(?P<Grade_Id>\w{0,5})/$', views.Grades, name='Course'),
    path('testimonial/',views.Testimonial, name='testimonial'),
    path('teacher/',Teacher.as_view(),name='teacher'),
    path('student/',Student.as_view(),name='student'),
    path('gallery/',Gallery.as_view(),name='gallery'),




]
