from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import StudentRegisterForm


class StudentRegisterView(CreateView):
    form_class = StudentRegisterForm
    template_name = "register.html"
    success_url = reverse_lazy("homepage")
