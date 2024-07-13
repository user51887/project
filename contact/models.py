from django.utils import timezone
from django.db import models

# Create your models here.

class Contact(models.Model):
    
   
    
    sujet = models.CharField(max_length=50)

    email = models.EmailField()
    
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now) 


    def __str__(self):
        return self.sujet
    
    def delete_message(self):
        # Méthode pour supprimer le message
        self.delete()