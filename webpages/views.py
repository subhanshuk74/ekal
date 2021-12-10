from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from .models import *
from .forms import abc,Teach
from django.views.generic import CreateView
from django.conf import settings
from django.views.generic import TemplateView
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders

def sitemap(request):

    return render(request, 'sitemap.xml', content_type='text/xml')

def robots(request):
    return render(request, 'robots.txt', content_type='text')

class hm(CreateView):
    model = student
    form_class = abc
    template_name = 'Index_copy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["study_class"] = Study_Class.objects.all()
        
        return context


    def form_valid(self, form):
        email = form.cleaned_data['Email']
        name = form.cleaned_data['Name']

        html_content = render_to_string('thankyou.html',{'title':'Test'+name})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(

            'Hi '+name+', Thanks for chosing us',
            text_content,
            settings.EMAIL_HOST_USER,
            [email],
            ['sanchitsinghal.11@gmail.com','sharma.bhavya02@gmail.com','vanshikagarg.45@gmail.com','kinshukg18@gmail.com']
            

        )
        msg.attach_alternative(html_content, "text/html")
        
        msg.send()
        return super(hm, self).form_valid(form)
        
def blog(request):
    event_list = blogs.objects.all()
    event_list1=[]
    for j in event_list:
        
        url_string=(j.image_url)
        a=url_string.replace('/file/d/','/uc?export=view&id=')
        a=a.replace('/view?usp=sharing','')
        
        j.image_url=a

    
    context={'obj':event_list}
    return render(request,'blog2.html',context)



def article(request,blog_id):
    
    event_list1=[]    
    event_list=blogs.objects.get(slug_url=blog_id)

    

    context={'object':event_list}
    
    return render(request,'article.html',context)

def Grades(request, Grade_Id):

    if 'th' in Grade_Id:
        Grade_Id=int(Grade_Id.replace('th',''))
        event_list = Classes.objects.get(GId=Grade_Id)

    # orders=Classes.order_set.all()
        context={'object':event_list}
        return render(request,'Grades.html',context)
    else:
        return render(request,'error.html')

def Grade_Science(request, Grade_Id):

    Grade_Id=int(Grade_Id.replace('th',''))
    event_list = Science.objects.get(GId=Grade_Id)

    # orders=Classes.order_set.all()
    context={'object':event_list}
    return render(request,'Grade_Science.html',context)

def Grade_Commerce(request, Grade_Id):

    Grade_Id=int(Grade_Id.replace('th',''))
    event_list = Commerce.objects.get(GId=Grade_Id)

    # orders=Classes.order_set.all()
    context={'object':event_list}
    return render(request,'Grade_Commerce.html',context)

def Grade_Humanities(request, Grade_Id):




    Grade_Id=int(Grade_Id.replace('th',''))
    event_list = Humanities.objects.get(GId=Grade_Id)

    # orders=Classes.order_set.all()
    context={'object':event_list}
    return render(request,'Grade_Humanities.html',context)

class Doubt(CreateView):
    model = student
    form_class = abc
    template_name = 'doubt.html'

def StudyMaterial(request):

    event_list = Study_Class.objects.all()

    # orders=Classes.order_set.all()
    context={'object':event_list}
    return render(request,'StudyMaterial.html',context)


class About(CreateView):
    model = student
    form_class = abc
    template_name = 'about-us.html'

# def Micro(request, Grade_Id):
    
#     #form_class = abc
#     # grade=micrograde.objects.all()
#     event_list1 = micrograde.objects.get(class_id=Grade_Id)
    
#     event_list = microsub.objects.filter(subject_id=Grade_Id)
#     event_list2 = microdata.objects.filter(grade_id=event_list[0])
#     # print(microdata.objects.get(grade_id=1))
    
#     context={'object':[event_list,event_list2]}
#     print(context)
#     return render(request,'micro.html',context)

def Micro(request,Grade_Id):
       
    
    event_list_class = Study_Class.objects.get(classid=Grade_Id)
    
    event_list_subject = subject.objects.filter(studid_id=Grade_Id)
    
    event_list_new=[]
    for i in event_list_subject:
        
        event_list_chap =chap.objects.filter(subject_id=i)
        
        for j in event_list_chap:
        
            url_string=(j.img_url)
            
            a=url_string.replace('/file/d/','/uc?export=view&id=')
            a=a.replace('/view?usp=sharing','')
            a=a.replace('abc','')
            j.img_url=a
            print(j.img_url)
            
            
        
        
        
        print(event_list_new.append(event_list_chap))

    context={'subject':event_list_subject,'chap':event_list_new}
    
    
    return render(request,'micro.html',context)

class Thankyou(CreateView):
    model = student
    form_class = abc
    template_name = 'thankyou.html'

class login(CreateView):
    model = student
    form_class = abc
    template_name = 'loginsignup.html'

def Download(request,Grade_Id):
    
    r=str(request)
    
    print(r)
    event_list = Study_Class.objects.get(classid=Grade_Id)
        
    event_list1 = subject.objects.filter(studid_id=event_list)   
    
    l=r.split('/')
    print(l)
    context={'object':event_list1,'obc':l[1]}
    print(context['obc'])
    
    return render(request,'page2.html',context)

def chapter(request,Grade_Id):
    
    r=str(request)
    l=r.split('/')
    
    event_list = subject.objects.get(sub=Grade_Id)
    print(event_list)
    
    event_list1 = chap.objects.filter(subject_id=event_list)
    l=str(l[1]).split('_')
    if len(l)>1:
        context={'object':event_list1,'obc':l[1].capitalize()+'s'}
    elif len(l)==1:
        context={'object':event_list1,'obc':l[0].capitalize()+'s'}
    print(context['obc'])

    return render(request,'chapter.html',context)
class contact(CreateView):
    model = student
    form_class = abc
    template_name = 'contact.html'
    def form_valid(self, form):
        email = form.cleaned_data['Email']
        name = form.cleaned_data['Name']

        html_content = render_to_string('thankyou.html',{'title':'Test'+name})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(

            'Hi '+name+', Thanks for chosing us',
            text_content,
            settings.EMAIL_HOST_USER,
            [email],
            ['sanchitsinghal.11@gmail.com','sharma.bhavya02@gmail.com','vanshikagarg.45@gmail.com','kinshukg18@gmail.com']
            

        )
        msg.attach_alternative(html_content, "text/html")
        
        msg.send()
        return super(contact, self).form_valid(form)
class work(CreateView):
    model = student
    form_class = Teach
    template_name = 'work.html'



def error_404(request,exception):
    return render(request,'error.html')

def error_500(request):
    return render(request,'error.html')