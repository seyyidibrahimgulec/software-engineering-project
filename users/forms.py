from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.db import transaction

from users.models import DepartmentStaff, Student, Teacher, User


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
            user.is_teacher = True
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
                cell_phone=cell_phone, home_phone=home_phone, username=username,
                is_department_staff=True, is_staff=True
            )

            # NOTE: evet tüm permissionları vermek aptalca falan
            permissions = Permission.objects.all()
            for p in permissions:
                user.user_permissions.add(p)
            user.save()

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
