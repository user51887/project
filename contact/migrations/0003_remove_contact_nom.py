# Generated by Django 4.0.4 on 2022-07-19 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_contactmodel_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='nom',
        ),
    ]
