from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction


User = get_user_model()


class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=150, label="Nome completo")
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirme sua senha")

    def clean_full_name(self):
        return " ".join(self.cleaned_data["full_name"].split())

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(username__iexact=email).exists() or User.objects.filter(email__iexact=email).exists():
            raise ValidationError("Já existe uma conta cadastrada com este e-mail.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmation = cleaned_data.get("password_confirmation")
        if password and confirmation and password != confirmation:
            self.add_error("password_confirmation", "As senhas não coincidem.")
        if password:
            candidate = User(username=cleaned_data.get("email", ""), email=cleaned_data.get("email", ""))
            try:
                validate_password(password, candidate)
            except ValidationError as error:
                self.add_error("password", error)
        return cleaned_data

    def save(self):
        full_name = self.cleaned_data["full_name"]
        first_name, _, last_name = full_name.partition(" ")
        try:
            with transaction.atomic():
                return User.objects.create_user(
                    username=self.cleaned_data["email"],
                    email=self.cleaned_data["email"],
                    password=self.cleaned_data["password"],
                    first_name=first_name,
                    last_name=last_name,
                )
        except IntegrityError as error:
            raise ValidationError("Já existe uma conta cadastrada com este e-mail.") from error


class LoginForm(forms.Form):
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")

    def clean_email(self):
        return self.cleaned_data["email"].strip().lower()
