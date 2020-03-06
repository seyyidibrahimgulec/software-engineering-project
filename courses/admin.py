from django.contrib import admin
from courses.models import Department, Classroom, Language, Lesson


admin.site.register(Department)
admin.site.register(Classroom)
admin.site.register(Language)
admin.site.register(Lesson)
