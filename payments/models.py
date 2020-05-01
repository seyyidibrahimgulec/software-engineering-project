from django.db import models


class Payment(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    lesson = models.ForeignKey(to='courses.Lesson', on_delete=models.PROTECT)
    student = models.ForeignKey(to='users.Student', on_delete=models.PROTECT)


class Installment(models.Model):
    amount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="miktar")
    payment = models.ForeignKey(to=Payment, on_delete=models.PROTECT)
    is_paid = models.BooleanField(verbose_name="Ödendi?")

    def __str__(self):
        return f"{self.payment.student.__str__()}"

    def student(self):
        return self.payment.student

    class Meta:
        default_permissions = ("add", "change", "delete", "view")
