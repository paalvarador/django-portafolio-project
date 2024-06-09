from django.shortcuts import render
from .models import Profile, Project, Education, Experience, Skill, Service, OfferedService

# Create your views here.
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

    return render(request, 'portfolio/home.html', {
        'list_projects': list_projects, 
        'profile_info': profile_info, 
        'list_education': list_education,
        'list_experience': list_experience,
        'list_skills': list_skills,
        'list_service': list_service,
        'list_projects': list_projects
        })

