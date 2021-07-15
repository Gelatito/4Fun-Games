"""FinalTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django import urls
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from core.views import principal
from Administrador.views import principal as pri
from core.views import Lista
from Administrador.views import Lista as li
from core.views import Modificar
from Administrador.views import Modificar as mod
from core.views import CAT
from Administrador.views import CAT as cat
from core.views import ModificarCAT
from Administrador.views import ModificarCAT as modcat
from core.views import ListaCAT
from Administrador.views import ListaCAT as lc

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include ('core.urls')),
    path( '', principal ),
    path('Admin/principal/',pri),
    path('Admin/Lista/',li),
    path('Admin/Modificar/<id>',mod),
    path('Admin/CAT/',cat),
    path('ModificarCAT/',modcat),
    path('ListaCAT/',lc),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)