from django.db import models


class ClassroomUnavailableSlot(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    classroom = models.ForeignKey(to="courses.Classroom", on_delete=models.PROTECT)
    lesson = models.ForeignKey(to="courses.Lesson", on_delete=models.CASCADE)


class TeacherUnavailableSlot(models.Model):
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    teacher = models.ForeignKey(to="users.Teacher", on_delete=models.PROTECT)
    lesson = models.ForeignKey(to="courses.Lesson", on_delete=models.CASCADE)
