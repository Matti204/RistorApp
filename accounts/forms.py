from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User

class BootstrapFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

class LoginForm(BootstrapFieldsMixin, AuthenticationForm):
    pass

class RegistrationForm(BootstrapFieldsMixin, UserCreationForm):
    first_name = forms.CharField(label="Nome", max_length=150)
    last_name = forms.CharField(label="Cognome", max_length=150)

    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Questa email ? gi? registrata.")
        return email
