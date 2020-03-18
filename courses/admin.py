from django.contrib import admin

from courses.models import Classroom, Department, Language, Lesson


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "public_transport_info", "private_transport_info")
    search_fields = (
        "name",
        "adress",
        "public_transport_info",
        "private_transport_info",
    )


@admin.register(Classroom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ("name", "department")
    list_filter = ("department__name",)
    search_fields = ("name", "department")


admin.site.register(Language)
admin.site.register(Lesson)
