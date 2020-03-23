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

from courses.api_view import ClassRoomAPIView, CreateLessonAPIView
from courses.views import AddLessonView
from home.views import IframeView
from timeslots.api_views import TimeAvailableAPIView
from users.api_views import TeachersAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("add_lesson/", AddLessonView.as_view(), name="add_lesson"),
    path("i/<str:page>", IframeView.as_view(), name="home"),
]

# API Views
urlpatterns += [
    path("api/get_class", ClassRoomAPIView.as_view()),
    path("api/get_teacher", TeachersAPIView.as_view()),
    path("api/get_hours", TimeAvailableAPIView.as_view()),
    path("api/create_lesson", CreateLessonAPIView.as_view()),
]
