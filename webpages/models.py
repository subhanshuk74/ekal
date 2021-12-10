from django.db import models
from django.urls import reverse
from datetime import date
Grades= [(6,'Grade 6th'),(7,'Grade 7th'),(8,'Grade 8th'),(9,'Grade 9th'),(10,'Grade 10th'),(11,'Grade 11th'),(12,'Grade 12th'),]
class student(models.Model,):
    
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length = 100)
    Number=models.CharField(max_length = 10)
    Class=models.IntegerField(choices=Grades)
    Course=models.CharField(max_length=30)
    Information=models.CharField(max_length=300)
    
    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')

class Classes(models.Model,):
    
    
    Grade_Title=models.CharField(max_length=100,default='')   
    info=models.CharField(max_length=3000,default='')
    Grade_math= models.CharField(max_length=3000,default='')
    Grade_Science=models.CharField(max_length=3000,default='')
    Grade_English=models.CharField(max_length=3000,default='')
    Grade_SST=models.CharField(max_length=3000,default='')
    desc=models.CharField(max_length=200,default='')
    Title=models.CharField(max_length=100,default='')
    GId = models.IntegerField(default=0)

    def __str__(self):
        return self.Grade_Title

    def get_absolute_url(self):
        return f'/{self.GId}'+'th/'
    
class Science(models.Model,):
    
    
    Grade_Title=models.CharField(max_length=100,default='')   
    info=models.CharField(max_length=3000,default='')
    Math= models.CharField(max_length=3000,default='')
    Chemistry=models.CharField(max_length=3000,default='')
    Physics=models.CharField(max_length=3000,default='')
    Bio=models.CharField(max_length=3000,default='')
    English=models.CharField(max_length=3000,default='')
    desc=models.CharField(max_length=200,default='')
    Title=models.CharField(max_length=100,default='')
    GId = models.IntegerField(default=0)
    
    def get_absolute_url(self):
        return f'/Science/{self.GId}'+'th/'

    

    def __str__(self):
        return self.Grade_Title

        

class Commerce(models.Model,):
    
    
    Grade_Title=models.CharField(max_length=100,default='')   
    info=models.CharField(max_length=3000,default='')
    Math= models.CharField(max_length=3000,default='')
    Eco=models.CharField(max_length=3000,default='')
    Accounts=models.CharField(max_length=3000,default='')
    BST=models.CharField(max_length=3000,default='')
    English=models.CharField(max_length=3000,default='')
    desc=models.CharField(max_length=200,default='')
    Title=models.CharField(max_length=100,default='')
    GId = models.IntegerField(default=0)
    
    
    def get_absolute_url(self):
        return f'/Commerce/{self.GId}'+'th/'
    

    def __str__(self):
        return self.Grade_Title

class Humanities(models.Model,):
    
    
    Grade_Title=models.CharField(max_length=100,default='')   
    info=models.CharField(max_length=3000,default='')
    PolSc= models.CharField(max_length=3000,default='')
    Geo=models.CharField(max_length=3000,default='')
    History=models.CharField(max_length=3000,default='')
    Sociology=models.CharField(max_length=3000,default='')
    Psycology=models.CharField(max_length=3000,default='')
    English=models.CharField(max_length=3000,default='')
    desc=models.CharField(max_length=200,default='')
    Title=models.CharField(max_length=100,default='')
    GId = models.IntegerField(default=0)
    
    
    def get_absolute_url(self):
        return f'/Humanities/{self.GId}'+'th/'
    

    def __str__(self):
        return self.Grade_Title


class Teacher(models.Model,):
    
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length = 100)
    Number=models.CharField(max_length = 10)
    Class=models.IntegerField(choices=Grades)
    Course=models.CharField(max_length=30)
    
    Address=models.CharField(max_length=200)
    Education=models.CharField(max_length=100)
    Experience=models.CharField(max_length=200)
    Thoughts=models.CharField(max_length=100)
    Query=models.CharField(max_length=300)
    
    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('index')

class Study_Class(models.Model,):
    classid= models.CharField(max_length=50,default='Null',primary_key=True)
    
    def __str__(self):
        return str(self.classid)
    
    

class subject(models.Model,):
    studid= models.ForeignKey(Study_Class,on_delete=models.CASCADE)
    sub_name= models.CharField(max_length=100)
    mock_desc=models.CharField(max_length=8000,default='abc')
    ass_desc=models.CharField(max_length=8000,default='abc')
    book_desc=models.CharField(max_length=8000,default='abc')
    sol_desc=models.CharField(max_length=8000,default='abc')
    sub=models.CharField(max_length=100,primary_key=True)
    url_sol=models.CharField(max_length=100,default='abc')
    url_mock=models.CharField(max_length=100,default='abc')
    url_ass=models.CharField(max_length=100,default='abc')
    url_books=models.CharField(max_length=100,default='abc')
    def __str__(self):
        return str(self.sub)

    # 
            

class chap(models.Model,):
    subject=models.ForeignKey(subject,to_field='sub',on_delete=models.CASCADE)
    img_url=models.CharField(max_length=500,default='abc')
    mock_desc=models.CharField(max_length=8000,default='abc')
    ass_desc=models.CharField(max_length=8000,default='abc')
    book_desc=models.CharField(max_length=8000,default='abc')
    sol_desc=models.CharField(max_length=8000,default='abc')
    chap_name=models.CharField(max_length=100)
    Book_url=models.CharField(max_length=500,default='abc')
    Sol_url=models.CharField(max_length=500,default='abc')
    Mock_url=models.CharField(max_length=500,default='abc')
    Ass_url=models.CharField(max_length=500,default='abc')
    def __str__(self):
        return ((str(self.subject))+' '+str(self.chap_name))



        
class blogs(models.Model,):

    image_url=models.CharField(max_length=500,default='')
    blog_title= models.CharField(max_length=200)
    blog_desc=models.TextField(max_length=8000)
    desc=models.CharField(max_length=300,default='')
    hyp_link=models.CharField(max_length=100,default='')
    hyp_text=models.CharField(max_length=100,default='')
    meta_Title=models.CharField(max_length=200,default='')
    slug_url=models.CharField(max_length=100,default='')
    date = models.DateField(default=date.today)
    blog_id=models.IntegerField(default=1)
    def human_readable_title(self):
        
        
        return self.slug_url.replace('-', '_')


    def __str__(self):
        return str(self.blog_title)

    def get_absolute_url(self):
        return f'/blogs/{self.slug_url}/'


class Student_detail(models.Model,):
    Name=models.CharField(max_length=50,default='',blank=True)
    School=models.CharField(max_length=100,default='',blank=True)
    Mother_Name=models.CharField(max_length=50,default='',blank=True)
    Father_Name=models.CharField(max_length=50,default='',blank=True)
    Father_Occupation=models.CharField(max_length=100,default='',blank=True)
    Student_Phone_No=models.CharField(max_length=10,default='',blank=True)
    Father_Phone_No=models.CharField(max_length=10,default='',blank=True)
    Mother_Phone_No=models.CharField(max_length=10,default='',blank=True)
    Email_Id=models.CharField(max_length=50,default='',blank=True)
    Class=models.CharField(max_length=10,default='',blank=True)
    Subject=models.CharField(max_length=100,default='',blank=True)
    Timings=models.CharField(max_length=100,default='',blank=True)
    Address=models.CharField(max_length=100,default='',blank=True)
    Carrier_interest=models.CharField(max_length=50,default='',blank=True)
    Fees=models.CharField(max_length=10,default='',blank=True)
    Comment=models.CharField(max_length=1000,default='',blank=True)
    Referal=models.CharField(max_length=10,default='',blank=True)
    counseling=models.CharField(max_length=10,default='',blank=True)
    conversion=models.CharField(max_length=1000,default='',blank=True)
    leadVia=models.CharField(max_length=30,default='',blank=True)

    def __str__(self):
        return str(self.Name+self.School+self.Class)