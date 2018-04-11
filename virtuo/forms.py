from .models import Course, Student, Teacher, Material, Question
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelFom):
    password = forms.CharField(widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['enrollment_no', 'courses']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_id', 'courses']