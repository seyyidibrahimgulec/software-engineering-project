import datetime

from django.shortcuts import render
from django.views import View

from courses.models import Department, Language


class AddLessonView(View):
    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        languages = Language.objects.all()

        days = [datetime.datetime.now()]
        one_day = datetime.timedelta(days=1)
        for i in range(10):
            days.append(days[-1] + one_day)

        return render(
            request,
            "add_lesson.html",
            {"departments": departments, "languages": languages, "days": days},
        )
