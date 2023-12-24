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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import login_request, register_request, editar_request, editar_avatar_request, saludo

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('register/', register_request, name="Register"),
    path('home/', saludo, name="Home"),
    path('editar_usuario/', editar_request, name="EditarUsuario"),
    path('editar_avatar/', editar_avatar_request, name="EditarAvatar"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)