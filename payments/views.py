from django.shortcuts import redirect, render
from django.views import View


class PayInstallment(View):
    def get(self, request):
        if not request.user.is_department_staff:
            return redirect("/")

        context = {}
        return render(request, "pay_installment.html", context)
