from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppBlog.forms import SearchKnitForm, SearchYarnForm, SearchAccessoriesForm
from AppBlog.models import Knit, Yarn, Accessories

# Create your views here.


class KnitList(LoginRequiredMixin, ListView):
    model = Knit
    template_name = "AppBlog/lista_tejidos.html"


class YarnList(LoginRequiredMixin, ListView):
    model = Yarn
    template_name = "AppBlog/lista_hilados.html"


class AccessoriesList(LoginRequiredMixin, ListView):
    model = Accessories
    template_name = "AppBlog/lista_accesorios.html"


class KnitDetail(LoginRequiredMixin, DetailView):
    model = Knit
    template_name = "AppBlog/detalle_tejidos.html"


class YarnDetail(LoginRequiredMixin, DetailView):
    model = Yarn
    template_name = "AppBlog/detalle_hilados.html"


class AccessoriesDetail(LoginRequiredMixin, DetailView):
    model = Accessories
    template_name = "AppBlog/detalle_accesorios.html"


class KnitCreate(LoginRequiredMixin, CreateView):
    model = Knit
    template_name = "AppBlog/crear_tejido.html"
    success_url = "/app/listar_tejido/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "instrucciones", "autor", "fecha"]


class YarnCreate(LoginRequiredMixin, CreateView):
    model = Yarn
    template_name = "AppBlog/crear_hilado.html"
    success_url = "/app/listar_hilado/"
    fields = ["nombre", "material", "descripcion", "imagen", "autor", "fecha"]


class AccessoriesCreate(LoginRequiredMixin, CreateView):
    model = Accessories
    template_name = "AppBlog/crear_accesorios.html"
    success_url = "/app/listar_accesorio/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "autor", "fecha"]


class KnitUpdate(LoginRequiredMixin, UpdateView):
    model = Knit
    template_name = "AppBlog/actualizar_tejido.html"
    success_url = "/app/listar_tejido/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "instrucciones", "autor", "fecha"]


class YarnUpdate(LoginRequiredMixin, UpdateView):
    model = Yarn
    template_name = "AppBlog/actualizar_hilado.html"
    success_url = "/app/listar_hilado/"
    fields = ["nombre", "material", "descripcion", "imagen", "autor", "fecha"]


class AccessoriesUpdate(LoginRequiredMixin, UpdateView):
    model = Accessories
    template_name = "AppBlog/actualizar_accesorio.html"
    success_url = "/app/listar_accesorio/"
    fields= ["nombre", "tecnica", "material", "descripcion", "imagen", "autor", "fecha"]


class KnitDelete(LoginRequiredMixin, DeleteView):
    model = Knit
    template_name = "AppBlog/eliminar_tejido.html"
    success_url = "/app/listar_tejido/"
    
    
class YarnDelete(LoginRequiredMixin, DeleteView):
    model = Yarn
    template_name = "AppBlog/eliminar_hilado.html"
    success_url = "/app/listar_hilado/"
    

class AccessoriesDelete(LoginRequiredMixin, DeleteView):
    model = Accessories
    template_name = "AppBlog/eliminar_accesorio.html"
    success_url = "/app/listar_accesorio/"


@login_required
def busqueda_tejido(request):
    nombre = request.GET["nombre"]
    tejido = Knit.objects.filter(nombre__icontains=nombre)
    contexto = {
        "tejido": tejido,
        "form": SearchKnitForm()
    }
    return render(request, "AppBlog/lista_tejidos.html", contexto)


@login_required()
def busqueda_hilado(request):
    nombre = request.GET["nombre"]
    hilado = Yarn.objects.filter(nombre__icontains=nombre)
    contexto = {
        "hilado": hilado,
        "form": SearchYarnForm()
    }
    return render(request, "AppBlog/lista_hilados.html", contexto)


@login_required()
def busqueda_accesorio(request):
    nombre = request.GET["nombre"]
    accesorio = Accessories.objects.filter(nombre__icontains=nombre)
    contexto = {
        "accesorio": accesorio,
        "form": SearchAccessoriesForm()
    }
    return render(request, "AppBlog/lista_accesorios.html", contexto)