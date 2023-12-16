from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar


# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username= username, password= password)
            if user:
                login(request, user)
                return redirect('ListaTejidos')
    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm()
        contexto = {
            "form": form
        }
        return render(request, "accounts/registro.html", contexto)


def editar_request(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.post)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.save()

            return redirect("ListaTejidos")
    form = UserUpdateForm(initial={"email": user.email})
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":
        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user= user,
                    imagen= data["imagen"]
                )
            avatar.save()
            return redirect("ListaTejidos")
    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)
