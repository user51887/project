from django.urls import path
from . import views


app_name = 'accueil'

urlpatterns = [
    path('',views.accueil, name='accueil' ),
    path('services/' , views.service_detail , name='service_detail'),
    path('success/' , views.send_success , name='send_success'),
    path('successs/' , views.send_successs , name='send_successs'),
    path('confirm_appointment/<int:rend_id>/', views.confirm_appointment, name='confirm_appointment'),
    path('enregistrer-date/', views.enregistrer_date, name='enregistrer_date'),
    
]
