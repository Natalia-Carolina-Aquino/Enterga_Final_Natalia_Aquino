from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('Home')
    form = AuthenticationForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/login.html", contexto)


def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('Login')
    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required()
def editar_request(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.post)
        if form.is_valid():
            data = form.cleaned_data
            user.email = data["email"]
            user.save()

            return redirect("Home")
    form = UserUpdateForm(initial={"email": user.email})
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)


@login_required()
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
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()
            return redirect("Home")
    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)


@login_required()
def saludo(request):
    usuario = User(request.user)
    contexto = {"usuario": usuario}
    return render(request, "accounts/home.html", contexto)