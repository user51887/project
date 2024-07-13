import json
from django.shortcuts import get_object_or_404, render, redirect
from accueil.forms import ContactForm, RendForm
from accueil.models import Rend
from blog.models import Post
from contact.models import Contact

from equipes.models import Equipes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta  # Vous n'avez pas besoin d'importer datetime ici

from django.core.serializers import serialize
from django.http import JsonResponse



from django.utils import timezone



from django.contrib import messages

from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from accueil.forms import ContactForm, RendForm
from accueil.models import Rend


def accueil(request):
    posts = Post.objects.all()
    
 
    posts = Post.objects.all()
    post_list = Post.objects.all()
    equipes = Equipes.objects.all()
    equipe_list = Equipes.objects.all()
    rendez_vous = RendForm()
    contact_form = ContactForm()


    if request.method == 'POST':
        if 'rendez_vous_submit' in request.POST:
            rendez_vous = RendForm(request.POST, request.FILES)
            if rendez_vous.is_valid():  # Assurez-vous que le formulaire est valide avant d'accéder à clean()
                rendez_vous_date = rendez_vous.cleaned_data['La_Date']
                heure_selectionnee = rendez_vous.cleaned_data['L_Heure']
                
                # Vérifier si la date sélectionnée a des heures disponibles
                heures_prises = Rend.objects.filter(La_Date=rendez_vous_date).values_list('L_Heure', flat=True)
                if heure_selectionnee not in heures_prises:
                    rendez_vous.save()
                    return redirect('accueil:send_success')
                else:
                    # Afficher un message d'erreur indiquant que l'heure sélectionnée n'est pas disponible
                    messages.error(request, "L'heure sélectionnée n'est pas disponible pour cette date. Veuillez choisir une autre heure.")

        elif 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                sujet = contact_form.cleaned_data['sujet']
                email = contact_form.cleaned_data['email']
                message = contact_form.cleaned_data['message']
                try:
                    send_mail(sujet, message, email, ['admin@example.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header')
                return redirect('accueil:send_successs')

    context = {
        'form': rendez_vous,
        'contact_form': contact_form,
       
        
        'posts' : posts,
        'post_list' : post_list ,
        'equipes' : equipes,
        'equipe_list' : equipe_list ,
    }

    return render(request, 'accueil/index.html', context)



def service_detail(request):
    
    

    context = {
        'service_detail' : service_detail ,
        
    }

    return render(request , 'accueil/service_detail.html' , context)



def send_success(request):
    context = {
        'send_success': send_success
    }
    return render(request, 'accueil/send_success.html', context)


def send_successs(request):
    context = {
        'send_successs': send_successs
    }

    return render(request, 'accueil/send_successs.html', context)


def confirm_appointment(request, rend_id):
    appointment = get_object_or_404(Rend, id=rend_id)
    appointment.is_confirmed = True
    appointment.save()
    return redirect('customadmin:dashboard')

def enregistrer_date(request):
    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        date = request.POST.get('date')
        # Ici, vous pouvez enregistrer la date dans votre base de données ou effectuer toute autre opération nécessaire
        # Exemple d'enregistrement de la date dans la console pour cet exemple
        print('Date enregistrée:', date)
        return JsonResponse({'message': 'Date enregistrée avec succès dans la base de données.'})
    else:
        return JsonResponse({'error': 'Requête non autorisée ou non AJAX.'}, status=400)
