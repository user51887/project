from .models import Services

from django.shortcuts import render

# Create your views here.


def service_list(request):
    service_list = Services.objects.all()

   
    
    context = {
        'service_list' : service_list ,
    }

    return render(request , 'Services/service_list.html' , context)


def service_detail(request , id):
    service_detail = Services.objects.get(id=id)
    

    context = {
        'service_detail' : service_detail ,
        
    }

    return render(request , 'Services/service_detail.html' , context)




