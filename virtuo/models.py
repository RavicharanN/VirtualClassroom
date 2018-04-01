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