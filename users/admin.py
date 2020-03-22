from django.contrib import admin

from users.forms import NewDepartmentStaffForm, NewTeacherForm
from users.models import DepartmentStaff, Student, Teacher, User


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = NewTeacherForm
    list_filter = ("known_langs", "department")
    list_display = (
        "__str__",
        "department",
    )
    fields = tuple()

    def get_fields(self, request, obj=None):
        if obj:
            return (
                "user",
                "known_langs",
                "department",
                "start_work_time",
            )

        else:
            return (
                "username",
                "password",
                "known_langs",
                "home_phone",
                "cell_phone",
                "department",
                "start_work_time",
            )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("user",)
        else:
            return tuple()


@admin.register(DepartmentStaff)
class DepartmentStaffAdmin(admin.ModelAdmin):
    form = NewDepartmentStaffForm
    list_filter = ("department",)
    list_display = (
        "__str__",
        "department",
    )

    fields = tuple()

    def get_fields(self, request, obj=None):
        if obj:
            return ("user", "department")
        else:
            return (
                "username",
                "password",
                "home_phone",
                "cell_phone",
                "department",
            )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("user",)
        else:
            return tuple()


admin.site.register(User)
admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(DepartmentStaff)
