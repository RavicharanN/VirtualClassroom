from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.first_view, name= 'first_view'),
    url(r'^login/$', auth_views.login, {'template_name': 'virtuo/login.html'}, name='login'),
    # url(r'studentregister/', views.StudentRegister.as_view(), name = 'studentregister'),
    # url(r'teacherregister/', views.TeacherRegister.as_view(), name = 'teacherregister'),
    url(r'register', views.UserRegister.as_view(), name = 'register')
]
