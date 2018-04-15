# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length = 35, null = False, blank = False)
    course_id = models.CharField(max_length = 35, null = False, blank = False, unique = True, primary_key = True)
    credits = models.IntegerField(null = False, blank = False)

    def __str__(self):
        return "%s %s %s" % (self.course_name, self.course_id, self.credits)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default = 1)
    enrollment_no = models.CharField(max_length = 35, primary_key = True ,unique = True, null = False, blank = False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.enrollment_no

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, default = 1)
    teacher_id = models.CharField(max_length = 35, primary_key = True ,unique = True, null = False, blank = False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.teacher_id

class Material(models.Model):
    M_TYPE = (
        ('PPT', 'Presentation'),
        ('VID', 'Video'),
    )
    # material_id1 = models.CharField(max_length = 35, null = False, blank = False, primary_key = True)
    material_name = models.CharField(max_length = 35, null = False, blank = False)
    material_link = models.CharField(max_length = 255, null = False, blank = False, unique = True)
    uploaded_by = models.CharField(max_length = 35, null = False, blank = False)
    related_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    m_type = models.CharField(max_length = 3, choices = M_TYPE, default = 'PPT')

    def __str__(self):
        return "%s %s" % (self.material_name, self.uploaded_by)

class Question(models.Model):
    question_id = models.CharField(max_length = 35, null = False, blank = False, primary_key = True) #Add verbose name
    material_id = models.ForeignKey(Material, on_delete = models.CASCADE)
    question = models.TextField(null = True, blank = True)
    asked_by = models.CharField(max_length = 10)
    answered_by = models.CharField(max_length = 10)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return "%s %s" % (self.question_id, self.material_id)