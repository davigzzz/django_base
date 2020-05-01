from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from .models import Usuario
from django import forms


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    class Meta(UserCreationForm):
        model = Usuario
        fields = ('usuario',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ('usuario',)

class UsuarioAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('usuario', 'password')

        def clean(self):
            usuario = self.cleaned_data['usuario']
            password = self.cleaned_data['password']
            if not authenticate(usuario=usuario, password=password):
                raise forms.ValidationError("Credenciales inválidas")



