# Generated by Django 3.0.3 on 2020-05-01 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20200306_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='installment',
            options={'default_permissions': ('add', 'change', 'delete', 'view')},
        ),
    ]
