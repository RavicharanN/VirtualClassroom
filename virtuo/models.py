# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length = 35, null = False, blank = False)
    course_id = models.CharField(max_length = 35, null = False, blank = False, unique = True, primary_key = True)
    credits = models.IntegerField(null = False, blank = False)

    def __str__(self):
        return "%s %s %s" % (self.course_name, self.course_id, self.credits)

class Student(models.Model):
    first_name = models.CharField(max_length = 35, null = False, blank = False)
    last_name = models.CharField(max_length = 35, null = False, blank = False)
    enrollment_no = models.CharField(max_length = 35, primary_key = True ,unique = True, null = False, blank = False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.enrollment_no

class Teacher(models.Model):
    first_name = models.CharField(max_length = 35, null = False, blank = False)
    last_name = models.CharField(max_length = 35, null = False, blank = False)
    teacher_id = models.CharField(max_length = 35, primary_key = True ,unique = True, null = False, blank = False)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.enrollment_no

class Material(models.Model):
    M_TYPE = (
        ('PPT', 'Presentation'),
        ('VID', 'Video'),
    )

    material_name = models.CharField(max_length = 35, null = False, blank = False)
    material_link = models.CharField(max_length = 255, null = False, blank = False, unique = True)
    uploaded_by = models.CharField(max_length = 35, null = False, blank = False)
    related_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    m_type = models.CharField(max_length = 3, choices = M_TYPE)

    def __str__(self):
        return "%s %s" % (self.material_name, self.uploaded_by)




class login(models.Model):
    U_TYPE = (
        ('1', 'Student'),
        ('2', 'Faculty'),
        ('3', 'Admin'),
    )

    user_name = models.CharField(max_length = 35, null = False, blank = False, primary_key = True)
    pwhash = models.CharField(max_length = 30, null = False, blank = False)
    user_type = models.CharField(max_length = 1, choices = U_TYPE)

class Q_A(models.Model):
    QID = models.CharField(max_length = 35, null = False, blank = False, primary_key = True) #Add verbose name
    Material_ID = models.ForeignKey(Material, on_delete = models.CASCADE)
    Question = models.TextField(null = True, blank = True)
    Asked_By = models.CharField(max_length = 10)
    Answered_By = models.CharField(max_length = 10)
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
