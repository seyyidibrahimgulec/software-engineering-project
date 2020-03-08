from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    extra_infos = models.TextField()


class Classroom(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(to=Department, on_delete=models.PROTECT)


class Language(models.Model):
    name = models.CharField(max_length=255)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    classroom = models.ForeignKey(to=Classroom, on_delete=models.PROTECT)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    teacher = models.ForeignKey(to='users.Teacher', on_delete=models.PROTECT)
    language = models.ForeignKey(to=Language, on_delete=models.PROTECT)
    degree = models.IntegerField()


class ClassroomUnavailableSlot(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    classroom = models.ForeignKey(to=Classroom, on_delete=models.PROTECT)
