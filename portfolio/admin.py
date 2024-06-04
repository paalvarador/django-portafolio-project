from django.contrib import admin

from .models import Profile, Project, Skill, Experience, Education, Contact, Service, OfferedService

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    fields = ['name', 'bio', 'profile_picture', 'email', 'phone', 'linkedin', 'github', 'x', 'personal_website']

    list_display = ['name', 'email', 'phone']

admin.site.register(Profile, ProfileAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'image', 'technologies', 'github_link', 'live_demo']

    list_display = ['title', 'technologies', 'live_demo', 'created_at']

admin.site.register(Project, ProjectAdmin)

class SkillAdmin(admin.ModelAdmin):
    fields = ['name', 'logo', 'proficiency']

    list_display = ['name', 'proficiency']

admin.site.register(Skill, SkillAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    fields = ['title', 'company', 'description', 'start_date', 'end_date']

    list_display = ['title', 'company', 'start_date', 'end_date']

admin.site.register(Experience, ExperienceAdmin)

class EducationAdmin(admin.ModelAdmin):
    fields = ['degree', 'institution', 'start_date', 'end_date', 'description']

    list_display = ['degree', 'institution', 'start_date', 'end_date']

admin.site.register(Education, EducationAdmin)

class ContactAdmin(admin.ModelAdmin):
    fields = ['name', 'email', 'message']

    list_display = ['name', 'email']

admin.site.register(Contact, ContactAdmin)

class OfferedServiceInline(admin.TabularInline):
    model = OfferedService
    extra = 1

class ServiceAdmin(admin.ModelAdmin):
    fields = ['name', 'icon', 'description']

    list_display = ['name', 'description']

    inlines = [OfferedServiceInline]


admin.site.register(Service, ServiceAdmin)

