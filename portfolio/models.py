from django.db import models
import cloudinary.models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_picture = cloudinary.models.CloudinaryField('profile_picture', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    personal_website = models.URLField(blank=True, null=True)
    cv = cloudinary.models.CloudinaryField('cv', folder='portfolio/cv/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = cloudinary.models.CloudinaryField('project_images', blank=True, null=True)
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=100, blank=True, null=True)
    proficiency = models.IntegerField() # Un valor entre 1 y 100

    def __str__(self) -> str:
        return self.name
    
class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.degree} at {self.institution}"

class Service(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name

class OfferedService(models.Model):
    service = models.ForeignKey(Service, related_name='offered_services', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Message from {self.name} ({self.email})"


