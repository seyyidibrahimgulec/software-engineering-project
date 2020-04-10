from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponse


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
        # TODO: Add Teacher Pages
        return HttpResponse("<h1>Teacher</h2>")
    elif request.user.is_student:
        # TODO: Add Student Pages
        return HttpResponse("<h1>Student</h2>")
    elif request.user.is_department_staff:
        # TODO: Add DepartmentStaff Pages
        return HttpResponse("<h1>DepartmentStaff</h2>")
