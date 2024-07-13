from django.urls import path
from . import views

app_name = 'customadmin'

urlpatterns = [
    path('login/', views.custom_admin_login, name='custom_admin_login'),
    path('dashboard/', views.custom_admin_dashboard, name='dashboard'),
    path('dashboard2/', views.custom_admin_dashboard2, name='dashboard2'),
    path('appointment/', views.appointment, name='appointment'),
    path('<int:id>/', views.edit_appointment, name='edit_appointment'),
    path('message/', views.message, name='message'),
    path('delete_message/<int:id>/', views.delete_message, name='delete_message'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('liste_patients/', views.liste_patients, name='liste_patients'),
    path('blog/', views.blog, name='blog'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('delete_patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit_patient/<int:id>/', views.edit_patient, name='edit_patient'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('add_post/', views.add_post, name='add_post'),
]
