# Generated by Django 3.0.3 on 2020-03-06 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.Student'),
        ),
        migrations.AddField(
            model_name='installment',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='payments.Payment'),
        ),
    ]