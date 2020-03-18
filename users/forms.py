from django import forms

from users.models import Teacher, User


class NewTeacherForm(forms.ModelForm):
    username = forms.CharField()
    home_phone = forms.CharField(max_length=255)
    cell_phone = forms.CharField(max_length=255)

    def save(self, commit=True):
        cell_phone = self.cleaned_data.get("cell_phone", None)
        home_phone = self.cleaned_data.get("home_phone", None)
        username = self.cleaned_data.get("username", None)

        user = User.objects.create(
            cell_phone=cell_phone,
            home_phone=home_phone,
            username=username
        )

        instance = super(NewTeacherForm, self).save(commit=commit)
        instance.user = user

        if commit:
            instance.save()
        return instance

    class Meta:
        fields = ("known_langs", "department", "start_work_time",)
        model = Teacher
