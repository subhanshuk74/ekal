from django.contrib.sitemaps import Sitemap
from webpages.models import *
from django.contrib.sites.models import Site
from webpages.views import *

class Site:
    domain = 'ekalshiksha.in'

class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(ArticleSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        return blogs.objects.all()
        

class CourseSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(CourseSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        return Classes.objects.all()
        

class CourseScienceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(CourseScienceSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        return Science.objects.all()

class CourseCommerceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(CourseCommerceSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        return Commerce.objects.all()

class CourseHumanitiesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5
 
    def get_urls(self, site=None, **kwargs):
        site = Site()
        return super(CourseHumanitiesSitemap, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        return Humanities.objects.all()



        
class StudyGrade(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        f=super(StudyGrade, self).get_urls(site=site, **kwargs)
        # print(super(StudyGrade, self).get_urls(site=site,**kwargs))
        # for i in range(len(f)):
        #     for j in range(4):
        #         print((f[i]['location'][22]))
            
        
        return super(StudyGrade, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (Study_Class.objects.all())

    def location(self,Study_Class):
        return '/Mock_Test/%s' % (Study_Class.classid)

class StudyGrade1(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        
        # print(super(StudyGrade, self).get_urls(site=site,**kwargs))
        # for i in range(len(f)):
        #     for j in range(4):
        #         print((f[i]['location'][22]))
            
        
        return super(StudyGrade1, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (Study_Class.objects.all())

    def location(self,Study_Class):
        
            return '/Assignments/%s' % (Study_Class.classid)


class StudyGrade2(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        
        # print(super(StudyGrade, self).get_urls(site=site,**kwargs))
        # for i in range(len(f)):
        #     for j in range(4):
        #         print((f[i]['location'][22]))
            
        
        return super(StudyGrade2, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (Study_Class.objects.all())

    def location(self,Study_Class):
        return '/NCERT_book/%s' % (Study_Class.classid)

class StudyGrade3(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()
        
        # print(super(StudyGrade, self).get_urls(site=site,**kwargs))
        # for i in range(len(f)):
        #     for j in range(4):
        #         print((f[i]['location'][22]))
            
        
        return super(StudyGrade3, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (Study_Class.objects.all())

    def location(self,Study_Class):
        return '/NCERT_solution/%s' % (Study_Class.classid)

class StudySubject(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()         
        
        return super(StudySubject, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (subject.objects.all())

    def location(self,subject):
        
        return '/NCERT_solution/chapter/%s' % (subject.sub)

class StudySubject1(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()         
        
        return super(StudySubject1, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (subject.objects.all())

    def location(self,subject):
       
        return '/NCERT_book/chapter/%s' % (subject.sub)

class StudySubject2(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()         
        
        return super(StudySubject2, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (subject.objects.all())

    def location(self,subject):
        
        return '/Mock_Test/chapter/%s' % (subject.sub)

class StudySubject3(Sitemap):
    changefreq = "daily"
    priority = 0.5
    
    def get_urls(self, site=None, **kwargs):
        site = Site()         
        
        return super(StudySubject3, self).get_urls(site=site, **kwargs)
 
    def items(self):
        
        
        return (subject.objects.all())

    def location(self,subject):
        
        return '/Assignments/chapter/%s' % (subject.sub)

class Micro(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return(Study_Class.objects.all())
    def location(self, Study_Class):
        return '/Micro/%s' % (Study_Class.classid)

class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return ['index','Doubt','contact','About','work','blog']
    def location(self, item):
        return reverse(item)