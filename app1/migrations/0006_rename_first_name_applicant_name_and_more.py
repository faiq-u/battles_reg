# Generated by Django 4.2.2 on 2023-12-25 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_applicant_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='last_name',
        ),
    ]
