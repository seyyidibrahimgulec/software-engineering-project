from django.contrib import admin

from payments.models import Installment, Payment


@admin.register(Installment)
class InstallmentAdmin(admin.ModelAdmin):
    list_display = ("student", "amount", "is_paid")
    list_filter = ("is_paid", "amount")
    search_fields = ("payment__student__user__username",)


admin.site.register(Payment)
