# Generated by Django 4.0.6 on 2022-07-18 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_employee_dep_employee_dept_employee_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]