from django import forms
from .models import *
attr={'class':'input'}
# from .models import emp
Grades= [(6,'Grade 6th'),(7,'Grade 7th'),(8,'Grade 8th'),(9,'Grade 9th'),(10,'Grade 10th'),(11,'Grade 11th'),(12,'Grade 12th'),]

class abc(forms.ModelForm):
    class Meta:
        model= student
        fields= ('Name','Email','Number','Class','Course','Information')
        # labels = {
        #     'Information':'What you want to enquire for???',
            
            
        # }

        widgets = {
            'Name': forms.TextInput(attrs={'class':'control','class':'input','required': True}),
            'Email': forms.EmailInput(attrs={'class':'input', 'required': True}),
            'Number': forms.TextInput(attrs={'class':'input','required': True,}),
            'Class':forms.Select(attrs=attr,choices=Grades),
            'Course':forms.TextInput(attrs={'class':'input', 'required': True}),
            'Information':forms.Textarea(attrs={'class':'input', 'required': True}),
        }

class Teach(forms.ModelForm):
    class Meta:
        model= Teacher
        fields= ('Name','Email','Number','Class','Course','Address','Education','Experience','Thoughts','Query')
        labels = {
            'Query':'Any questions you want to ask?',
            
            
        }

        widgets = {
            'Name': forms.TextInput(attrs={'class':'control','class':'input','required': True}),
            'Email': forms.EmailInput(attrs={'class':'input', 'required': True}),
            'Number': forms.TextInput(attrs={'class':'input','required': True,}),
            'Class':forms.Select(attrs=attr,choices=Grades),
            'Course':forms.TextInput(attrs={'class':'input', 'required': True}),
            
            'Address':forms.TextInput(attrs={'class':'input', 'required': True}),
            'Education':forms.TextInput(attrs={'class':'input', 'required': True}),
            'Experience':forms.TextInput(attrs={'class':'input', 'required': True}), 
            'Thoughts':forms.Textarea(attrs={'class':'input', 'required': True}), 
            'Query':forms.Textarea(attrs={'class':'input', 'required': True}),
        }
# # class GeeksForm(forms.ModelForm):
# #     GEEKS_CHOICES =(
# #         ("1", "One"),
# #         ("2", "Two"),
# #         ("3", "Three"),
# #         ("4", "Four"),
# #         ("5", "Five"),
# #     )
#     class Meta:
#         model=emp
#         fields= ('Name','Email','Number','Qualification','Position','Exp','Jobtype')


#         widgets = {
#             'Name': forms.TextInput(attrs={'class':'form-control', 'required': True}),
#             'Email': forms.EmailInput(attrs={'class':'form-control', 'required': True}),
#             'Number': forms.TextInput(attrs={'class':'form-control','required': True,}),
#             'Qual':forms.CharField(attrs={'class':'form-control','required': True,}),
#             'Position':forms.TextInput(attrs={'class':'form-control', 'required': True},widget=forms.Select(choices=GEEK_CHOICES)),
#             'Exp':forms.TextInput(attrs={'class':'form-control', 'required': True}),
#             'Jobtype':forms.TextInput(attrs={'class':'form-control', 'required': True}),
#         }
