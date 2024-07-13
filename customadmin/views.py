# customadmin/views.py

from datetime import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from accueil.models import Rend
from blog.forms import CommentForm
from blog.models import Post,Comment
from contact.models import Contact

from django.utils import timezone
from customadmin.forms import PatientForm, PostForm
from customadmin.models import Patient, Transaction



def custom_admin_dashboard(request):
    nbT = Rend.objects.count()
    nombre_messages = Contact.objects.count()
    nbr_patient=Patient.objects.count()
    nbr_article=Post.objects.count()
    nbr_confirmed = Rend.objects.filter(is_confirmed=True).count()
    today = timezone.now().date()
    nombre_messages_today = Contact.objects.filter(created_at__date=today).count()
    nombre_patient_today= Patient.objects.filter(created_at__date=today).count()
    return render(request, 'customadmin/dashboard.html', {'nbT': nbT,'nombre_messages': nombre_messages,
                                                          'nbr_patient':nbr_patient,
                                                          'nbr_article':nbr_article,
                                                          'nbr_confirmed':nbr_confirmed,
                                                          'nombre_messages_today':nombre_messages_today,
                                                          'nombre_patient_today':nombre_patient_today})

def custom_admin_dashboard2(request):
    
    return render(request, 'customadmin/dashboard2.html')


def custom_admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if not user:
            messages.info(request, 'Compte introuvable')
            return redirect(reverse('customadmin:custom_admin_login'))
 # Redirect to login if user not found

        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_superuser:
                login(request, user)
                return redirect('customadmin:dashboard')
            else:
                login(request, user)
                return redirect('customadmin:dashboard2')  # Redirect to dashboard2 if not a superuser
        
        messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
        return redirect(reverse('customadmin:custom_admin_login'))
# Redirect to login if authentication fails
    
    return render(request, 'customadmin/login.html')

    

def appointment(request):
    rendez_vous = Rend.objects.all()
    
    return render(request, 'customadmin/appointment.html', {'rendez_vous': rendez_vous})





def edit_appointment(request, id):
    appointment = get_object_or_404(Rend, id=id)

    

    if request.method == 'POST':
        if 'cancel' in request.POST:
            # Handle appointment cancellation
            appointment.cancel = True
            appointment.save()
            # Redirect to some appropriate page after cancellation
            return redirect('customadmin:appointment')  # Redirect to the appointment list
        else:
            # Handle confirmation status change
            confirmation_status = request.POST.get('confirmation_status')
            appointment.is_confirmed = (confirmation_status == 'confirmed')
            appointment.save()
            # Redirect to some appropriate page after confirmation status change
            return redirect('customadmin:appointment')  # Redirect to the appointment list

    return render(request, 'customadmin/edit_appointment.html', {'appointment': appointment})

def message(request):
    msg=Contact.objects.all()
    
    return render(request, 'customadmin/messages.html',{'msg':msg})


def delete_message(request, id):
    
    message = get_object_or_404(Contact, id=id)
    message.delete()
    messages.success(request, 'Le message a été supprimé avec succès.')
    return redirect('customadmin:message')

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customadmin:add_patient')  # Redirigez vers une page de confirmation après avoir ajouté le patient
    else:
        form = PatientForm()
    return render(request, 'customadmin/add_patient.html', {'form': form})


def liste_patients(request):
    cin = request.GET.get('cin', '')  # Get CIN from query parameters, default to empty string if not provided
    nom = request.GET.get('nom', '')  # Get name from query parameters, default to empty string if not provided
    
    # Filter patients by CIN and name
    patients = Patient.objects.filter(CIN__icontains=cin, nom__icontains=nom)
    transactions = Transaction.objects.all()
    print(transactions)
    return render(request, 'customadmin/liste_patients.html', {'patients': patients,'transactions': transactions})


def blog(request):
    blogs = Post.objects.all()
    
    # Passer les blogs au template
    return render(request, 'customadmin/blog.html', {'blogs': blogs})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk)
    comments = post.comment_set.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post  # Assign the post variable, not post_detail
            new_comment.save()
            return redirect('customadmin:post_detail', pk)  # Redirect back to the same page after adding comment
    else:
        comment_form = CommentForm()

    context = {
        'post': post,  # Pass the post variable instead of post_detail
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, 'customadmin/post_detail.html', context)

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('customadmin:post_detail', pk=post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'customadmin/edit_post.html', {'form': form})




def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customadmin:liste_posts')
    else:
        form = PostForm()
    return render(request, 'customadmin/add_post.html', {'form': form})


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    
    # Créer une transaction de suppression avant de supprimer le patient
    Transaction.objects.create(user=request.user, patient=patient, action='Suppression', timestamp=timezone.now())
    
    patient.delete()
    
    messages.success(request, 'Le patient a été supprimé avec succès.')
    
    return redirect('customadmin:liste_patients')

def confirm_delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    return render(request, 'confirm_delete_patient.html', {'patient': patient})

def perform_delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, 'Le patient a été supprimé avec succès.')
    return redirect('customadmin:liste_patients')
  

def edit_patient(request, id):
    
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST, instance=patient)
    if form.is_valid():
        form.save()
        Transaction.objects.create(user=request.user, patient=patient, action='Modification', timestamp=timezone.now())
        return redirect('customadmin:liste_patients')
    else:
  
        form = PatientForm(instance=patient)
    

    return render(request, 'customadmin/edit_patient.html', {'form': form})