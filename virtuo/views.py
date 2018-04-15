# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, StudentForm, TeacherForm, MaterialModelForm
from .models import Material

# Create your views here.

def first_view(request):
    if not request.user.is_authenticated:
        return render(request, 'text.html', {'name':'Not authenticated','logout_button':True})
    return render(request, 'text.html', {'name':request.user.username,'logout_button':False})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('first_view')
        return render(request, 'login.html', {})
    return render(request, 'login.html', {})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    return redirect('login')

class UserRegister(View):
    form_class = UserForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            print(username+"vjh")
            user.save()
            message = "registered successfully"
            login(request, user)
            return redirect('first_view')
        return render(request, self.template_name, {'form':form})

class StudentRegister(View):
    form_class = StudentForm
    template_name = 'studentregister.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form':form})
        return redirect('register')

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            enrollment_no = form.cleaned_data['enrollment_no'] 
            courses = form.cleaned_data['courses']
            print(enrollment_no)
            print(courses)
            student.save()
            return redirect('first_view')
        return render(request, self.template_name, {'form':form})

class TeacherRegister(View):
    form_class = TeacherForm
    template_name = 'teacherregister.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form':form})
        return redirect('register')
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user = request.user
            teacher.save()
            return redirect('first_view')
        return render(request, self.template_name, {'form':form})

class MaterialCreateView(CreateView):
    model = Material
    template_name = "addCourse.html"
    form_class = MaterialModelForm
    success_url = "/itsAddedRenameThis/"
