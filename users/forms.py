from django import forms
from .models import UserAccount

class SignupForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length = 2,
        max_length = 50,
        widget = forms.TextInput(attrs={
            'class' : 'form-control',
            'id' : 'username',
            'aria-hidden' : 'true'
        })
    )

    password = forms.CharField(
        required=True,
        min_length = 8,
        max_length = 100,
        widget = forms.PasswordInput(attrs = {
            'class' : 'form-control',
            'aria-hidden' : 'true'
        })
    )

    def save(self):
        return UserAccount.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('password'),
        )