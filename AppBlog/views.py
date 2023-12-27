from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from AppBlog.forms import SearchKnitForm, SearchYarnForm, SearchAccessoriesForm, KnitCommentForm, YarnCommentForm, \
    AccessoriesCommentForm
from AppBlog.models import Knit, Yarn, Accessories, KnitComment, YarnComment, AccessoriesComment


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
    fields = "__all__"


class YarnCreate(LoginRequiredMixin, CreateView):
    model = Yarn
    template_name = "AppBlog/crear_hilado.html"
    success_url = "/app/listar_hilado/"
    fields = "__all__"


class AccessoriesCreate(LoginRequiredMixin, CreateView):
    model = Accessories
    template_name = "AppBlog/crear_accesorios.html"
    success_url = "/app/listar_accesorio/"
    fields = "__all__"


class KnitUpdate(LoginRequiredMixin, UpdateView):
    model = Knit
    template_name = "AppBlog/actualizar_tejido.html"
    success_url = "/app/listar_tejido/"
    fields = "__all__"


class YarnUpdate(LoginRequiredMixin, UpdateView):
    model = Yarn
    template_name = "AppBlog/actualizar_hilado.html"
    success_url = "/app/listar_hilado/"
    fields = "__all__"


class AccessoriesUpdate(LoginRequiredMixin, UpdateView):
    model = Accessories
    template_name = "AppBlog/actualizar_accesorio.html"
    success_url = "/app/listar_accesorio/"
    fields= "__all__"


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
    nombre = request.GET.get("nombre")
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


@login_required()
def comentario_tejido(request):
    if request.method == "POST":
        formulario = KnitCommentForm(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            tejido = Knit.objects.get(id=informacion["tejido"])
            comentario_crear = KnitComment(usuario=request.user, tejido=tejido, comentario=informacion["comentario"])
            comentario_crear.save()
            return redirect("/app/listar_tejido/")
        else:
            formulario = KnitCommentForm()
        return render(request, "AppBlog/detalle_tejidos.html", {'form': formulario})




@login_required()
def comentario_hilado(request):
    formulario = YarnCommentForm(request.POST)
    if formulario.is_valid():
        informacion = formulario.cleaned_data
        hilado = Yarn.objects.get(id= informacion["hilado"])
        comentario_crear = YarnComment(usuario=request.user, hilado=hilado, comentario=informacion["comentario"])
        comentario_crear.save()
        return redirect("/app/listar_hilado/")
    return render(request, "AppBlog/detalle_hilados.html", {"form": formulario})


@login_required()
def comentario_accesorio(request):
    formulario = AccessoriesCommentForm(request.post)
    if formulario.is_valid():
        informacion = formulario.cleaned_data
        accesorio = Accessories.objects.get(id=informacion["accesorio"])
        comentario_crear = AccessoriesComment(usuario=request.user, accesorio=accesorio, comentario=informacion["comentario"])
        comentario_crear.save()
        return redirect("/app/listar_accesorio/")
    return render(request, "AppBlog/detalle_accesorios.html", {'form': formulario} )


@login_required()
def ComingSoon(request):
    contexto = {}
    return render(request,"AppBlog/pagina_en_construccion.html", contexto)


def about(request):
    contexto = {}
    return render(request, "AppBlog/about.html", contexto)