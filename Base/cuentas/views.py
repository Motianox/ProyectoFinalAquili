from django.shortcuts import render

#Autenticación
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from cuentas.forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            form.save()
            return render(request, 'home.html', {'mensaje':'Cuenta creada exitosamente.'})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')
            user = authenticate(username = usuario, password = contras)
            if user is not None:
                login(request, user)
                return render(request, 'home.html', {'mensaje':f'¡Bienvenido/a {usuario}!'})
            else:
                return render(request, 'home.html', {'mensaje':'Datos erróneos.'})
        else:
            return render(request, 'home.html', {'mensaje':'Datos inexistentes.'})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})