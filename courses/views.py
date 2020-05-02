import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from courses.models import Department, Language, Lesson
from payments.models import Installment, Payment
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
        student = get_object_or_404(Student, user_id=request.POST.get("student"))
        lesson = get_object_or_404(Lesson, id=request.POST.get("lesson"))
        amount = int(request.POST.get("amount", 1))
        installment_count = int(request.POST.get("installment_count", 1))

        payment_count = Payment.objects.filter(
            lesson=lesson,
            student=student,
        ).count()

        if payment_count:
            payment = Payment.objects.get(
                lesson=lesson,
                student=student,
            )
            payment.amount = amount
            payment.save()

        else:
            payment = Payment.objects.create(
                lesson=lesson,
                student=student,
                amount=amount
            )

        one_installment = amount/installment_count
        for i in range(installment_count):
            Installment.objects.create(
                amount=one_installment,
                payment=payment,
                is_paid=False
            )

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
