from django.shortcuts import render

from equipes.models import Equipes

# Create your views here.

def equipe_list(request):
    equipe_list = Equipes.objects.all()

   
    
    context = {
        'equipe_list' : equipe_list ,
    }

    return render(request , 'Equipes/equipe_list.html' , context)
