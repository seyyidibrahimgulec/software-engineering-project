"""softeng_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from courses.api_view import ClassRoomAPIView, CreateLessonAPIView
from courses.views import AddLessonView
from home.views import IframeView, homepage, StudentDetailView, TeacherDetailView
from timeslots.api_views import TimeAvailableAPIView
from users.api_views import TeachersAPIView
from users.views import StudentRegisterView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("add_lesson/", AddLessonView.as_view(), name="add_lesson"),
    path("i/<str:page>/", IframeView.as_view(), name="home"),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', homepage, name='homepage'),
    path('register/', StudentRegisterView.as_view(), name='register'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher'),
]

# API Views
urlpatterns += [
    path("api/get_class", ClassRoomAPIView.as_view()),
    path("api/get_teacher", TeachersAPIView.as_view()),
    path("api/get_hours", TimeAvailableAPIView.as_view()),
    path("api/create_lesson", CreateLessonAPIView.as_view()),
]
