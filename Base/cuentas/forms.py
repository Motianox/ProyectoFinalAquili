from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Ingrese su nombre de usuario:')
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    imagen = forms.ImageField(required=True)
    class Meta:
        model = User
        fields = ['imagen']
        help_texts = {k:'' for k in fields}

class UserInfoForm(forms.Form):
    description = forms.CharField(max_length=250)
    links = forms.URLField()
