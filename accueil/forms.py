# Importation des modules de formulaire
from datetime import datetime, time, timedelta
from django import forms
from django.utils import timezone
from tempus_dominus.widgets import DateTimePicker


from functools import partial



from accueil.models import TITLE_CHOICES, Rend

# Importation du widget DateInput
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

# Créer une liste d'horaires pour le champ d'horaire
TIME_CHOICES = [
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    # Ajoutez d'autres heures au besoin
]
CHOIX_ANCIEN_PATIENT = [
    ('Oui', 'Oui'),
    ('Non', 'Non')
]

# Classe pour définir les champs du formulaire
class RendForm(forms.ModelForm):
    nom = forms.CharField(label="nom complet*", max_length=40, required=True)
    courriel = forms.EmailField(label="courriel", max_length=50)
    Ancien_patient = forms.ChoiceField(
        label='Etes-vous déjà patient à notre cabinet?*', 
        choices=CHOIX_ANCIEN_PATIENT,
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
        required=True
    )
    téléphone = forms.IntegerField(required=True)
    Raison = forms.ChoiceField(label='Raison de votre visite* :', choices=TITLE_CHOICES,required=True)
    La_Date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date'},
            format='%Y-%m-%d'
        ),
        input_formats=['%Y-%m-%d']
    )
    L_Heure = forms.TimeField(
        label='Heure*',
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={'type': 'time'}
        ),
        required=True
    )



  
    class Meta:
        model = Rend
        fields = ['nom', 'courriel', 'Ancien_patient', 'téléphone', 'Raison', 'La_Date', 'L_Heure','cancel_reason']
        widgets = {
            'La_Date': DateInput(),
        }


from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    
   
    
    sujet = forms.CharField()

    email = forms.CharField(required = True)
    
    message = forms.CharField(widget=forms.Textarea , required = True)


    def __str__(self):
        return self.sujet

    class Meta:
          model = Contact
          fields = ['sujet', 'email','message']          