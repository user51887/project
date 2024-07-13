from django.urls import path
from . import views

app_name = 'equipes'

urlpatterns = [
    path('',views.equipe_list, name='equipe_list' ),
    
]
