from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from users.models import Teacher, User, DepartmentStaff, Student


class NewTeacherForm(forms.ModelForm):
    username = forms.CharField(label="Kullanıcı Adı", required=False)
    home_phone = forms.CharField(max_length=255, label="Ev Telefonu", required=False)
    cell_phone = forms.CharField(max_length=255, label="Cep Telefonu", required=False)
    password = forms.CharField(max_length=255, label="Şifre", required=False)

    def save(self, commit=True):
        cell_phone = self.cleaned_data.get("cell_phone", None)
        home_phone = self.cleaned_data.get("home_phone", None)
        username = self.cleaned_data.get("username", None)
        password = self.cleaned_data.get("password", None)

        instance = super(NewTeacherForm, self).save(commit=commit)

        if all((home_phone, cell_phone, username, password)):
            user = User.objects.create(
                cell_phone=cell_phone, home_phone=home_phone, username=username
            )

            if password:
                user.set_password(password)
                user.save()
            instance.user = user

        if commit:
            instance.save()
        return instance

    class Meta:
        fields = (
            "known_langs",
            "department",
            "start_work_time",
        )
        model = Teacher

class NewDepartmentStaffForm(forms.ModelForm):
    username = forms.CharField(label="Kullanıcı Adı", required=False)
    home_phone = forms.CharField(max_length=255, label="Ev Telefonu", required=False)
    cell_phone = forms.CharField(max_length=255, label="Cep Telefonu", required=False)
    password = forms.CharField(max_length=255, label="Şifre", required=False)

    def save(self, commit=True):
        cell_phone = self.cleaned_data.get("cell_phone", None)
        home_phone = self.cleaned_data.get("home_phone", None)
        username = self.cleaned_data.get("username", None)
        password = self.cleaned_data.get("password", None)

        instance = super(NewDepartmentStaffForm, self).save(commit=commit)

        if all((home_phone, cell_phone, username, password)):
            user = User.objects.create(
                cell_phone=cell_phone, home_phone=home_phone, username=username
            )

            if password:
                user.set_password(password)
                user.save()
            instance.user = user

        if commit:
            instance.save()
        return instance

    class Meta:
        fields = (
            "department",
        )
        model = DepartmentStaff


class StudentRegisterForm(UserCreationForm):
    home_phone = forms.CharField(max_length=255, label="Ev Telefonu", required=False)
    cell_phone = forms.CharField(max_length=255, label="Cep Telefonu", required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'username',
            'home_phone',
            'cell_phone',
        )

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        Student.objects.create(user=user)
        return user
