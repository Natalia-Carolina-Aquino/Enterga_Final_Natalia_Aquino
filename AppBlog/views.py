from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppBlog.models import Knit, Yarn, Accessories

# Create your views here.


class KnitList(ListView):
    model = Knit
    template_name = "AppBlog/lista_tejidos.html"


class YarnList(ListView):
    model = Yarn
    template_name = "AppBlog/lista_hilados.html"


class AccessoriesList(ListView):
    model = Accessories
    template_name = "AppBlog/lista_accesorios.html"


class KnitDetail(DetailView):
    model = Knit
    template_name = "AppBlog/detalle_tejidos.html"


class YarnDetail(DetailView):
    model = Yarn
    template_name = "AppBlog/detalle_hilados.html"


class AccessoriesDetail(DetailView):
    model = Accessories
    template_name = "AppBlog/detalle_accesorios.html"


class KnitCreate(CreateView):
    model = Knit
    template_name = "AppBlog/crear_tejido.html"
    success_url = "app/listar_tejido/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "instrucciones", "autor", "fecha"]


class YarnCreate(CreateView):
    model = Yarn
    template_name = "AppBlog/crear_hilado.html"
    success_url = "app/listar_hilado/"
    fields = ["nombre", "material", "descripcion", "imagen", "autor", "fecha"]


class AccessoriesCreate(CreateView):
    model = Accessories
    template_name = "AppBlog/crear_accesorios.html"
    success_url = "app/listar_accesorio/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "autor", "fecha"]


class KnitUpdate(UpdateView):
    model = Knit
    template_name = "AppBlog/actualizar_tejido.html"
    success_url = "app/listar_tejido/"
    fields = ["nombre", "tecnica", "material", "descripcion", "imagen", "instrucciones", "autor", "fecha"]


class YarnUpdate(UpdateView):
    model = Yarn
    template_name = "AppBlog/actualizar_hilado.html"
    success_url = "app/listar_hilado/"
    fields = ["nombre", "material", "descripcion", "imagen", "autor", "fecha"]


class AccessoriesUpdate(UpdateView):
    model = Accessories
    template_name = "AppBlog/actualizar_accesorio.html"
    success_url = "app/listar_accesorio/"
    fields= ["nombre", "tecnica", "material", "descripcion", "imagen", "autor", "fecha"]


class KnitDelete(DeleteView):
    model = Knit
    template_name = "AppBlog/eliminar_tejido.html"
    success_url = "app/listar_tejido/"
    
    
class YarnDelete(DeleteView):
    model = Yarn
    template_name = "AppBlog/eliminar_hilado.html"
    success_url = "app/listar_hilado/"
    

class AccessoriesDelete(DeleteView):
    model = Accessories
    template_name = "AppBlog/eliminar_accesorio.html"
    success_url = "app/listar_accesorio/"