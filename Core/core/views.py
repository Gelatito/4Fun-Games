from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render
from .models import  Pag1juegos,Aventura,Lucha,Rol,MundoAbierto
from django.http import HttpResponse
# Create your views here.

def home(request):
    Juegos = Pag1juegos.objects.all()
    data = {
        'juegos':Juegos 
    }
    return render(request,'core/home.html',data)

def Adventures (request):
    JuegosAD = Aventura.objects.all()
    data = {
        'juegosad':JuegosAD
    }
    return render(request,'core/Adventures.html',data)

def Luchas (request):
    JuegosLu = Lucha.objects.all()
    data = {
        'juegoslu':JuegosLu
    }
    return render(request,'core/Luchas.html',data)    
 
def rol (request):
    JuegosRol = Rol.objects.all()
    data = {
        'juegosro':JuegosRol
    }
    return render(request,'core/rol.html',data)
    
def openWorld (request):
    JuegosMA = MundoAbierto.objects.all()
    data = {
        'juegosmu':JuegosMA
    }
    return render(request,'core/openWorld.html',data)

def principal(request):
   
    return render(request) 

def Lista(request):
    
    return render(request)


def Modificar(request):
    
    
    return render(request)

def Borrar(request):
    
    return render(request)

def CAT(request):
   
    return render(request)
    
def ModificarCAT(request):
   
    return render(request)     
    
      
def ListaCAT(request):
   
    return render(request)      

    

