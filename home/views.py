from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView

from courses.models import Lesson
from payments.models import Installment, Payment
from timeslots.models import TeacherUnavailableSlot
from users.models import DepartmentStaff, Student, Teacher


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

        elif self.page == "installment":
            self.url = reverse("admin:payments_installment_changelist")

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
        return redirect(reverse('teacher'))
    elif request.user.is_student:
        return redirect(reverse('student'))
    elif request.user.is_department_staff:
        return redirect(reverse('department_staff'))


class StudentDetailView(View):
    def get(self, request):
        student = Student.objects.get(user=self.request.user)
        payments = Payment.objects.filter(student=student)
        installments = Installment.objects.filter(payment__in=payments)

        context = {}
        context['payments'] = payments
        context['installments'] = installments
        return render(request, 'student.html', context=context, )


class TeacherDetailView(DetailView):
    def get(self, request):
        teacher = Teacher.objects.get(user=self.request.user)
        lessons = Lesson.objects.filter(teacher=teacher)
        context = {}
        context['lessons'] = lessons
        return render(request, 'teacher.html', context=context, )


class DepartmentStaffIndexView(View):
    def get(self, request, *args, **kwargs):
        department = DepartmentStaff.objects.get(user=request.user).department
        lessons = Lesson.objects.filter(classroom__department=department).order_by("-pk")

        for lesson in lessons:
            # NOTE: bok gibi kod oldu biliyorum
            lesson.slots = TeacherUnavailableSlot.objects.filter(lesson=lesson)

        context = {"lessons": lessons}
        return render(request, "department_staf.html", context)
