from django.contrib import admin
from users.models import Student, Teacher, DepartmentStaff, User

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(DepartmentStaff)


