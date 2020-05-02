from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Şube")
    adress = models.CharField(
        max_length=255, verbose_name="Adress", null=True, blank=True
    )
    public_transport_info = models.CharField(
        max_length=255, verbose_name="Toplu Ulaşım Bilgileri", null=True, blank=True
    )
    private_transport_info = models.CharField(
        max_length=255, verbose_name="Özel Ulaşım Bilgileri", null=True, blank=True
    )
    # extra_infos = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Şube"
        verbose_name_plural = "Şubeler"


class Classroom(models.Model):
    name = models.CharField(max_length=255, verbose_name="Sınıf İsmi")
    department = models.ForeignKey(
        to=Department, on_delete=models.PROTECT, verbose_name="Bağlı Olduğu Şube"
    )

    def __str__(self):
        return f"{self.department}'da {self.name} sınıfı"

    class Meta:
        verbose_name = "Sınıf"
        verbose_name_plural = "Sınıflar"


class Language(models.Model):
    name = models.CharField(max_length=255, verbose_name="Dil")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dil"
        verbose_name_plural = "Diller"


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ders isimi")
    classroom = models.ForeignKey(
        to=Classroom, on_delete=models.PROTECT, verbose_name="Sınıfı"
    )
    # start_datetime = models.DateTimeField(verbose_name="Başlangıç Zamanı")
    # end_datetime = models.DateTimeField(verbose_name="Bitiş Zamanı")
    teacher = models.ForeignKey(
        to="users.Teacher", on_delete=models.PROTECT, verbose_name="Öğretmen"
    )
    language = models.ForeignKey(
        to=Language, on_delete=models.PROTECT, verbose_name="Dil"
    )
    degree = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def get_long_name(self):
        return f"{self.name} - {self.classroom.department} - {self.teacher}"

    class Meta:
        verbose_name = "Ders"
        verbose_name_plural = "Dersler"
