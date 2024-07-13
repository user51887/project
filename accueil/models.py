from django.db import models
from datetime import datetime,date

TITLE_CHOICES = [
     ('consultation', 'Consultation'),
    ('soins dentaire urgents', 'Soins dentaire urgents'),
    
]

# Create your models here.
class Rend(models.Model):
    nom = models.CharField( max_length=40)
    courriel = models.EmailField( max_length=50)
    Ancien_patient = models.CharField(max_length=100, default="non")
    téléphone = models.IntegerField(null=True)
    Raison = models.CharField(max_length=50, choices=TITLE_CHOICES, null=True)
    La_Date = models.DateField(("Date"), default=date.today)
    is_confirmed = models.BooleanField(default=False)
    L_Heure = models.TimeField(default=datetime.now)
    cancel = models.BooleanField(default=False)
    cancel_reason = models.CharField(max_length=255, blank=True, null=True)
    


    def __str__(self):
        return self.nom