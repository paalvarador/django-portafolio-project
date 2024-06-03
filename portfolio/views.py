from django.shortcuts import render
from .models import Profile, Project

# Create your views here.
def home(request):
    # Obtener información para armar el home de la página
    profile_info = Profile.objects.all()[0]
    print(f"profile_info = {profile_info}")
    list_projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'list_projects': list_projects, 'profile_info': profile_info})

