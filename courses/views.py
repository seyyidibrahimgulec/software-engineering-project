import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from courses.models import Department, Language, Lesson
from payments.models import Payment
from users.models import Student


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


class AddTimeSlotView(View):
    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()

        days = [datetime.datetime.now()]
        one_day = datetime.timedelta(days=1)
        for i in range(10):
            days.append(days[-1] + one_day)

        return render(
            request,
            "add_timeslot.html",
            {"lessons": lessons, "days": days},
        )


class AddStudentToLessonView(View):
    def get(self, request, lesson_pk):
        lesson = get_object_or_404(Lesson, pk=lesson_pk)
        students = Student.objects.exclude(pk__in=Student.objects.filter(lessons=lesson))

        return render(
            request,
            "add_student_to_lesson.html",
            {"students": students, "lesson": lesson}
        )


class AddStudentToLesson(View):
    def post(self, request):
        print(request.POST)
        student = get_object_or_404(Student, user_id=request.POST.get("student"))
        lesson = get_object_or_404(Lesson, id=request.POST.get("lesson"))
        amount = request.POST.get("amount")

        Payment.objects.create(
            lesson=lesson,
            student=student,
            amount=amount
        )

        return HttpResponse("ok?")
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
