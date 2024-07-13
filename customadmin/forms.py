from django import forms
from blog.models import Post
from .models import INDICATIFS_TELEPHONIQUES, Patient


class TelephoneInput(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        widgets = (
            forms.Select(choices=INDICATIFS_TELEPHONIQUES),
            forms.TextInput(attrs={'placeholder': 'Numéro de téléphone'}),
        )
        super().__init__(widgets, *args, **kwargs)

    def decompress(self, value):
        if value:
            return [value.indicatif_telephonique, value.telephone]
        return ['', '']

    def format_output(self, rendered_widgets):
        return '<div style="display:flex;">{0}<span style="margin-left:5px;">{1}</span></div>'.format(rendered_widgets[0], rendered_widgets[1])

class TelephoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        fields = (
            forms.ChoiceField(choices=INDICATIFS_TELEPHONIQUES),
            forms.CharField(),
        )
        super().__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            return f"{data_list[0]} {data_list[1]}"
        return None

class PatientForm(forms.ModelForm):
    SEXE_CHOICES = [
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ]
    
    sexe = forms.ChoiceField(choices=SEXE_CHOICES, widget=forms.RadioSelect)
    telephone = TelephoneField(widget=TelephoneInput)
    

    class Meta:
        model = Patient
        fields = ['nom', 'prenom', 'date_de_naissance','CIN', 'telephone','sexe','infos']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'date_de_naissance': 'Date de naissance',
            'telephone': 'Numéro de téléphone',
        }
       

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telephone'].label = 'Numéro de téléphone'



class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        fields = ['author','title','text','created_date','published_date','image']    


