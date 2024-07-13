from django.contrib import admin

from customadmin.models import Patient, Transaction

# Register your models here.
admin.site.register(Patient)
admin.site.register(Transaction)
