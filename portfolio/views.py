from django.shortcuts import redirect, render
from .models import Profile, Project, Education, Experience, Skill, Service, OfferedService
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings

@csrf_exempt
def home(request):
    # Obtener información para armar el home de la página
    profile_info = Profile.objects.all()[0]
    list_education = Education.objects.all().order_by('start_date')
    list_experience = Experience.objects.all().order_by('start_date')
    list_projects = Project.objects.all()
    list_skills = Skill.objects.all()
    list_service = Service.objects.all()

    print(list_projects)

    for skill in list_skills:
        skill.style = f"height: 24px; width: {skill.proficiency}%"

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            contact = form.save() # Guardamos el mensaje en la base de datos
        
            # Construir el mensaje de correo
            subject = f'Mensaje de {contact.name} a través del formulario de contacto'
            message = f'Nombre: {contact.name}\nEmail: {contact.email}\n\nMensaje:\n{contact.message}'

            fr = settings.DEFAULT_FROM_EMAIL
            to = ["paalvarador@gmail.com"]

            # Enviar el correo
            send_mail(
                subject,
                message,
                fr,
                to,
                fail_silently=False,
            )

            # Redirigir o mostrar un mensaje de texto
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    
    form = ContactForm()
    return render(request, 'portfolio/home.html', {
        'list_projects': list_projects, 
        'profile_info': profile_info, 
        'list_education': list_education,
        'list_experience': list_experience,
        'list_skills': list_skills,
        'list_service': list_service,
        'list_projects': list_projects,
        'form': form
        })

def contact_success(request):
    return render(request, 'portfolio/contact_success.html')
        
    
