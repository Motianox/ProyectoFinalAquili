from django.shortcuts import render, redirect

#Autenticación
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

#Programa
from cuentas.forms import *
from cuentas.models import *

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

@login_required
def update_acc(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            if informacion['password1'] == informacion['password2']:
                usuario.username = informacion['username']
                usuario.email = informacion['email']
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'home.html', {"mensaje":"Contraseña incorrecta."})
            return redirect('Home')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email, 'username':usuario.username})
    return render(request, 'update_acc.html', {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def add_info(request):
    if request.method == 'POST':
            miFormulario = UserInfoForm(request.POST)
            print(miFormulario)
            if miFormulario.is_valid:
                usuario=request.user
                informacion = miFormulario.cleaned_data
                userinfo = UserInfo(id=usuario.id, description=informacion['description'], links=informacion['links'])
                userinfo.save()
                return redirect('Home')
    else:
        miFormulario = UserInfoForm()
    return render(request, 'add_info.html', {'miFormulario':miFormulario})

@login_required
def add_avatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            usuario = request.user
            avatar = Avatar.objects.filter(user=usuario)
            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = miFormulario.cleaned_data["imagen"]
                avatar.save()
            else:
                avatar = Avatar(user=usuario, imagen=miFormulario.cleaned_data["imagen"])
                avatar.save()
        return render(request, 'home.html')
    else:
        miFormulario = AvatarFormulario()
        return render(request, 'add_avatar.html', {'miFormulario':miFormulario})

@login_required
def profile(request):
    avatar = Avatar.objects.filter(user=request.user.id)
    usuario = request.user
    userinfo = UserInfo.objects.filter(id=usuario.id).first()
    if userinfo: 
        if len(avatar) > 0:
            return render (request, 'profile.html', {"avatar":avatar[0].imagen.url, "usuario":usuario, "description":userinfo.description, "links":userinfo.links})
        return render (request, 'profile.html', {"usuario":usuario, "description":userinfo.description, "links":userinfo.links})
    else: 
        if len(avatar) > 0:
            return render (request, 'profile.html', {"avatar":avatar[0].imagen.url, "usuario":usuario})
        return render (request, 'profile.html', {"usuario":usuario})
