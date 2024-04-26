"""
URL configuration for ipfs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from ipfs.views import pagina_principal, upload_file,lista_archivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pagina_principal, name="Pagina principal" ),
    path('upload', upload_file, name="Subir archivo"),
    path('listado',lista_archivos, name="listado_archivos")
]
