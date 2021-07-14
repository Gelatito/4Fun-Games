from django.contrib.auth import views
from core.models import Aventura
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import home,Adventures,Luchas,rol,openWorld
from Administrador.views import Modificar,Borrar,Lista,principal,CAT,ModificarCAT,ListaCAT,DeleCAT

urlpatterns=[
    path('',home,name="home"),
    path('Aventura/',Adventures,name="Aventura"),
    path('Lucha/',Luchas,name="Peleas"),
    path('Rol/',rol,name="Rolgames"),
    path('Mundo Abierto/',openWorld,name="GTa"),
    path('principal/',principal,name="ñaco"),
    path('Lista/',Lista,name="Li"),
    path('Modificar/<id>',Modificar,name="mod"),
    path('Admin/<id>',Borrar,name="delete"),
    path('CAT/',CAT,name="cat"),
    path('ModificarCAT/<id>',ModificarCAT,name="cat"),
    path('ListaCAT',ListaCAT,name="asd"),
    path('/<id>',DeleCAT,name="deletecat"),
]
