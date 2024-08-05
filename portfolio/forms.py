from django import forms
from .models import ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject','message']
        
        
    