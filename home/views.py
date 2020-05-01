from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.http import HttpResponse

from users.models import Student, Teacher
from payments.models import Payment, Installment
from courses.models import Lesson


class IframeView(View):
    def __set_url(self):
        self.page = self.kwargs.get("page")

        if self.page=="lesson":
            self.url = reverse("admin:courses_lesson_changelist")

        elif self.page=="language":
            self.url = reverse("admin:courses_language_changelist")

        elif self.page=="classroom":
            self.url = reverse("admin:courses_classroom_changelist")

        elif self.page=="department":
            self.url = reverse("admin:courses_department_changelist")

        elif self.page=="teacher":
            self.url = reverse("admin:users_teacher_changelist")

        elif self.page=="department_staff":
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
        # TODO: Add DepartmentStaff Pages
        return HttpResponse("<h1>DepartmentStaff</h2>")


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
