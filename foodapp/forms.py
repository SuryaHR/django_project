# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    contact_number = forms.CharField(max_length=15, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize widgets, labels, and placeholders here if needed
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['contact_number'].widget.attrs.update({'placeholder': 'Contact Number'})
