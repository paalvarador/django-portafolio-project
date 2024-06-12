from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'name': 'name', 'class': 'contact_form_input', 'placeholder': 'Escribe tú nombre'}),
            'email': forms.EmailInput(attrs={'name': 'email', 'class': 'contact_form_input', 'placeholder': 'Escribe tú email'}),
            'message': forms.Textarea(attrs={'name': 'project', 'cols': '30', 'rows': '10', 'class': 'contact_form_input', 'placeholder': 'Escribe el proyecto que tienes en mente'}),
        }