from django.contrib import admin

# Register your models here.
from .models import Rend



@admin.register(Rend)
class RendAdmin(admin.ModelAdmin):
    
  list_display = ('nom', 'Raison', 'La_Date')
  list_filter = ('La_Date', 'Raison', 'nom')
  search_fields = ('La_Date', 'Raison', 'nom')