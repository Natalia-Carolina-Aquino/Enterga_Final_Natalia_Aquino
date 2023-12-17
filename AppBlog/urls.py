"""
URL configuration for Entrega_Final_Natalia_Aquino project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static

from AppBlog.views import (KnitList, YarnList, AccessoriesList, KnitDetail, YarnDetail, AccessoriesDetail, KnitCreate,
                           busqueda_tejido, busqueda_hilado, busqueda_accesorio)
from AppBlog.views import (YarnCreate, AccessoriesCreate, KnitUpdate, YarnUpdate, AccessoriesUpdate)
from AppBlog.views import (KnitDelete, YarnDelete, AccessoriesDelete)
from django.urls import path
from django.conf import settings


urlpatterns = [
    path('listar_tejido/', KnitList.as_view(), name="ListaTejidos"),
    path('listar_hilado/', YarnList.as_view(), name="ListaHilados"),
    path('listar_accesorio/', AccessoriesList.as_view(), name="ListaAccesorios"),
    path('detalle_tejido/<int:pk>', KnitDetail.as_view(), name="DetalleTejido"),
    path('detalle_hilado/<int:pk>', YarnDetail.as_view(), name="DetalleHilado"),
    path('detalle_accesorio/<int:pk>', AccessoriesDetail.as_view(), name="DetalleAccesorio"),
    path('crear_tejido/', KnitCreate.as_view(), name="CrearTejido"),
    path('crear_hilado/', YarnCreate.as_view(), name="CrearHilado"),
    path('crear_accesorio/', AccessoriesCreate.as_view(), name="CrearAccesorio"),
    path('editar_tejido/<int:pk>', KnitUpdate.as_view(), name="EditarTejido"),
    path('editar_hilado/<int:pk>', YarnUpdate.as_view(), name="EditarHilado"),
    path('editar_accesorio/<int:pk>', AccessoriesUpdate.as_view(), name="EditarAccesorio"),
    path('borrar_tejido/<int:pk>', KnitDelete.as_view(), name="EliminarTejido"),
    path('borrar_hilado/<int:pk>', YarnDelete.as_view(), name="EliminarHilado"),
    path('borrar_accesorio/<int:pk>', AccessoriesDelete.as_view(), name="EliminarAccesorio"),
    path('buscar_tejido/', busqueda_tejido),
    path('buscar_hilado/', busqueda_hilado),
    path('buscar_accesorio/', busqueda_accesorio),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)