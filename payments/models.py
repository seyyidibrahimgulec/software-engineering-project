from django.db import models


class Payment(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    lesson = models.ForeignKey(to='courses.Lesson', on_delete=models.PROTECT)
    student = models.ForeignKey(to='users.Student', on_delete=models.PROTECT)


class Installment(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment = models.ForeignKey(to=Payment, on_delete=models.PROTECT)
    is_paid = models.BooleanField()
