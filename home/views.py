from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.views.generic.detail import SingleObjectMixin

from courses.models import Lesson
from payments.models import Installment, Payment
from timeslots.models import TeacherUnavailableSlot
from users.models import DepartmentStaff, Student, Teacher, User


class IframeView(View):
    def __set_url(self):
        self.page = self.kwargs.get("page")

        if self.page == "lesson":
            self.url = reverse("admin:courses_lesson_changelist")

        elif self.page == "language":
            self.url = reverse("admin:courses_language_changelist")

        elif self.page == "classroom":
            self.url = reverse("admin:courses_classroom_changelist")

        elif self.page == "department":
            self.url = reverse("admin:courses_department_changelist")

        elif self.page == "teacher":
            self.url = reverse("admin:users_teacher_changelist")

        elif self.page == "department_staff":
            self.url = reverse("admin:users_departmentstaff_changelist")

    def get(self, request, *args, **kwargs):
        self.__set_url()
        context = {"url": self.url}
        return render(request, "iframe.html", context)


def homepage(request):
    if request.user.is_anonymous:
        return redirect(reverse('login'))
    elif request.user.is_superuser:
        return redirect(reverse("home", args=['language']))
    elif request.user.is_teacher:
        return redirect(reverse('teacher', kwargs={'pk': request.user.pk}))
    elif request.user.is_student:
        return redirect(reverse('student', kwargs={'pk': request.user.pk}))
    elif request.user.is_department_staff:
        return redirect(reverse('department_staff'))


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = Student.objects.get(user=self.request.user)
        payments = Payment.objects.filter(student=student)
        installments = Installment.objects.filter(payment__in=payments)
        context['payments'] = payments
        context['installments'] = installments
        return context


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = Teacher.objects.get(user=self.request.user)
        lessons = Lesson.objects.filter(teacher=teacher)
        context['lessons'] = lessons
        return context


class DepartmentStaffIndexView(View):
    def get(self, request, *args, **kwargs):
        department = DepartmentStaff.objects.get(user=request.user).department
        lessons = Lesson.objects.filter(classroom__department=department).order_by("-pk")

        for lesson in lessons:
            # NOTE: bok gibi kod oldu biliyorum
            lesson.slots = TeacherUnavailableSlot.objects.filter(lesson=lesson)

        context = {"lessons": lessons}
        return render(request, "department_staf.html", context)
