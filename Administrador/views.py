from django.shortcuts import render
from core.models import MundoAbierto
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .forms import MundoAbiertoForm,CategoriasForm
from core.models import Categorias
from django.contrib.auth.decorators import login_required,permission_required


@permission_required('core/can.add_mundoabierto')
def principal(request):

   data ={
       'form':MundoAbiertoForm()
   }
   if request.method=='POST':
       formulario=MundoAbiertoForm(data=request.POST,files=request.FILES)
       if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "guardado mi pana"
       else:
           data['form']=formulario    
      
   return render(request,'agregar_adm.html',data)

@login_required
def Lista (request): 
    JuegosMA = MundoAbierto.objects.all()
    data = {
        'juegosmu':JuegosMA
    }
    return render (request,'listar_adm.html',data)

@login_required
def Modificar(request,id):
    juegos=MundoAbierto.objects.get(Codigo = id)
    data = {
        'form':MundoAbiertoForm(instance=juegos)
    }
    if request.method == "POST":
        formulario = MundoAbiertoForm(data=request.POST,instance=juegos)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
 
    return render(request,'modificar_adm.html',data)

def Borrar(request,id):
    juegos = MundoAbierto.objects.get(Codigo = id)
    
    juegos.delete()

    return redirect("Lista/")



@login_required
def CAT (request):

   data ={
       'form':CategoriasForm()
   }
   if request.method=='POST':
       formulario=CategoriasForm(data=request.POST,files=request.FILES)
       if formulario.is_valid():
           formulario.save()
           data["mensaje"] = "guardado mi pana"
       else:
           data['form']=formulario    
      
   return render(request,'agregarcat_adm.html',data)


@login_required
def ListaCAT (request): 
    Categoriasd = Categorias.objects.all()
    data = {
        'categorias':Categoriasd
    }
    return render (request,'listarcat_adm.html',data)   

@login_required
def ModificarCAT(request,id):
    juegos=Categorias.objects.get(idCategoria = id)
    data = {
        'form':CategoriasForm(instance=juegos)
    }
    if request.method == "POST":
        formulario = CategoriasForm(data=request.POST,instance=juegos)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
 
    return render(request,'modificarcat_adm.html',data)
@login_required
def DeleCAT(request,id):
    categorias = Categorias.objects.get(idCategoria = id)
    
    categorias.delete()

    return redirect("ListaCAT/")






# Create your views here.
