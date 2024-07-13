# Generated by Django 4.0.4 on 2024-03-29 14:33

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0007_patient_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_de_naissance',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='patient',
            name='telephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
