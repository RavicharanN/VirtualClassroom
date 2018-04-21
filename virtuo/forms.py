from django.contrib.auth.models import User

from django import forms
from .models import Course, Student, Teacher, Material, Question

class UserForm(forms.ModelForm):
    first_name = forms.CharField(label='first_name', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
    last_name = forms.CharField(label='last_name', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(label='email', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='password',widget= forms.PasswordInput(attrs={'placeholder':'Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class StudentForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all())
    class Meta:
        model = Student
        fields = ['enrollment_no', 'courses']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'courses']

class MaterialModelForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "material_name",
            "material_link",
            "related_course",
            "m_type",
            ]
                    # widgets = {
        #   "description": forms.Textarea(
        #           attrs={
        #               "placeholder": "New Description"
        #           }
        #       ),
        #   "title": forms.TextInput(
        #       attrs= {
        #           "placeholder": "Title"
        #       }
        #   )
        # }

