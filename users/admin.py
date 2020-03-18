from django.contrib import admin

from users.forms import NewTeacherForm
from users.models import DepartmentStaff, Student, Teacher, User


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = NewTeacherForm
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
                "home_phone",
                "cell_phone",
                "username",
                "known_langs",
                "department",
                "start_work_time",
            )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ("user",)
        else:
            return tuple()



admin.site.register(User)
admin.site.register(Student)
# admin.site.register(Teacher)
admin.site.register(DepartmentStaff)
