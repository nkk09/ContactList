from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'sex',
            'email',
            'phone',
            'date_of_birth',
            'job_title',
            'city',
            'country',
            'address',
            'fees',
        ]
    
    user_id = forms.CharField(max_length=200)
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    sex = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email = forms.EmailField(max_length=254)
    phone = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    job_title = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    country = forms.CharField(max_length=200)
    address = forms.CharField(widget=forms.Textarea)
    fees = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
