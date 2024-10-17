from django import forms
from .models import Contact
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name', 
            'address', 
            'profession', 
            'tel_number', 
            'email_address', 
        ]
    name = forms.CharField()
    address = forms.CharField()
    profession = forms.CharField()
    tel_number = forms.CharField()
    email_address = forms.EmailField()