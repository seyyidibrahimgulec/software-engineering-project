from django.shortcuts import render
from django.urls import reverse
from django.views import View


class CourseChangeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            context = ({"url": reverse("admin:courses_lesson_changelist")})
            return render(request, "iframe.html", context)
