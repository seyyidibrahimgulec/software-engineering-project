from django.contrib import admin
from payments.models import Installment, Payment


admin.site.register(Installment)
admin.site.register(Payment)
