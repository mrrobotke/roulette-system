# accounts/forms.py
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text="Enter your phone number")

    class Meta:
        model = User
        fields = ['username', 'email']  # Only include username and email from the User model

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)