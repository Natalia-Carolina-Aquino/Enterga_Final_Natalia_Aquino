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

from django.urls import path

from accounts.views import login_request, register_request, editar_request, editar_avatar_request

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('register/', register_request, name="Register"),
    path('editar_usuario/', editar_request, name="EditarUsuario"),
    path('editar_avatar/', editar_avatar_request, name="EditarAvatar"),

]

