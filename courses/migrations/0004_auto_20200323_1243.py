# Generated by Django 3.0.3 on 2020-03-23 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0003_auto_20200318_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Department', verbose_name='Bağlı Olduğu Şube'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Sınıf İsmi'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Dil'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='classroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Classroom', verbose_name='Sınıfı'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='end_datetime',
            field=models.DateTimeField(verbose_name='Bitiş Zamanı'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.Language', verbose_name='Dil'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Ders isimi'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='start_datetime',
            field=models.DateTimeField(verbose_name='Başlangıç Zamanı'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Teacher', verbose_name='Öğretmen'),
        ),
        migrations.DeleteModel(
            name='ClassroomUnavailableSlot',
        ),
    ]