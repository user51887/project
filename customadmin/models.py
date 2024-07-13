from django.utils import timezone
from django.contrib.auth.models import User  
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _



INDICATIFS_TELEPHONIQUES = [
    ('+212', '+212 (Maroc)'),
    ('+1', '+1 (USA)'),
    ('+33', '+33 (France)'),
    ('+44', '+44 (Royaume-Uni)'),
    ('+49', '+49 (Allemagne)'),
    ('+81', '+81 (Japon)'),
    ('+86', '+86 (Chine)'),
    ('+91', '+91 (Inde)'),
    ('+34', '+34 (Espagne)'),
    ('+39', '+39 (Italie)'),
    ('+61', '+61 (Australie)'),
    ('+7', '+7 (Russie)'),
    ('+52', '+52 (Mexique)'),
    ('+1', '+1 (Canada)'),
    ('+82', '+82 (Corée du Sud)'),
    ('+971', '+971 (Émirats arabes unis)'),
    ('+966', '+966 (Arabie saoudite)'),
    ('+65', '+65 (Singapour)'),
    ('+351', '+351 (Portugal)'),
    ('+852', '+852 (Hong Kong)'),
    # Ajoutez d'autres indicatifs téléphoniques selon vos besoins
]
SEXE_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_de_naissance = models.DateField(default=timezone.now)
    sexe = models.CharField(max_length=10, choices=SEXE_CHOICES)
    infos = models.TextField()
    telephone = PhoneNumberField()
    indicatif_telephonique = models.CharField(max_length=5, choices=INDICATIFS_TELEPHONIQUES, default='+212')
    created_at = models.DateTimeField(default=timezone.now) 
    CIN=models.CharField(max_length=50,default='AB786473')

    def __str__(self):
       return self.nom

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"
