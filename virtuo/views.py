# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .forms import UserForm, StudentForm, TeacherForm

# Create your views here.

def first_view(request):
    return render(request, 'text.html', {'name':'Ravicharan'})

def login_view(request):
    return render(request, 'login.html', {})

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
            return render(request, self.template_name, {'message':message ,'form':form})
        return render(request, self.template_name, {'form':form})

# class StudentRegister(View):
#     form_class = StudentForm
#     template_name = 'virtuo/studentregister'

#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form':form})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             student = form.save(commit=False)
#             student.user = request.user
#             student.save()
#             return redirect('virtuo:first_view')
#         return render(request, self.template_name, {'form':form})