# Generated by Django 3.2.25 on 2024-10-10 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_auto_20241010_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='emp_id',
        ),
    ]
