from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

#paquete para modulo de usuarios
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

#requerimientos formulario de contacto
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

#vista publica del sitiode
def vista_inicio(request):
    template_name = 'index.html'
    Entradas = Entrada.objects.all().order_by('-id')
    paginator = Paginator(Entradas, 3)
    page_number = request.GET.get('page')
    Entradas = paginator.get_page(page_number)
    banners = Banner.objects.all()
    return render(request, "index.html", {'entradas': Entradas, 'banners': banners})

#area privada del sitio, requiere login
def area_miembros(request):
    if request.user.is_authenticated:
        return render(request, "areaMiembros.html")
    return redirect('/login')

#Vistas genericas de django para sistema de usuarios
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "register.html", {'form': form})

def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                do_login(request, user)
                return redirect('/')

    return render(request, "login.html", {'form': form})
def logout(request):
    do_logout(request)
    return redirect('/')

#Formulario de contacto
def VistaContacto(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['asunto']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['mensaje']
            try:
                send_mail(subject, message, from_email, [' '])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contacto.html", {'form': form})
def VistaEnviado(request):
    return HttpResponse('¡Gracias por escribirnos!')
# Create your views here.
