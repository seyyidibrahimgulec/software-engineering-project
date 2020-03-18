from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Lesson, Language, Department
from payments.models import Payment


class User(AbstractUser):
    home_phone = models.CharField(max_length=255, unique=True)
    cell_phone = models.CharField(max_length=255, unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_department_staff = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, related_name='student')
    lessons = models.ManyToManyField(to=Lesson, through=Payment)

    class Meta:
        verbose_name = "Öğrenci"
        verbose_name_plural = "Öğrenciler"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, related_name='teacher')
    known_langs = models.ManyToManyField(to=Language, verbose_name="Bilinen Diller")
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT, verbose_name="Şube")
    start_work_time = models.DateTimeField(verbose_name="İşe başlama tarihi")

    def __str__(self):
        return f"ö: {self.user.username }"

    class Meta:
        verbose_name = "Öğretmen"
        verbose_name_plural = "Öğretmenler"


class DepartmentStaff(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True, related_name='department_staff')
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Çalışan"
        verbose_name_plural = "Çalışanlar"
