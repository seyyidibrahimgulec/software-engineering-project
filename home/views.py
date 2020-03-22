from django.shortcuts import render
from django.urls import reverse
from django.views import View


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
