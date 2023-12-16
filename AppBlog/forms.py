from django import forms


class KnitForm(forms.Form):
    nombre = forms.CharField()
    tecnica = forms.CharField()
    material = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()
    instrucciones = forms.CharField()
    autor = forms.CharField()
    fecha = forms.DateField()


class YarnForm(forms.Form):
    nombre = forms.CharField()
    material = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms. ImageField()
    autor = forms.CharField()
    fecha = forms.DateField()


class AccessoriesForm(forms.Form):
    nombre = forms.CharField()
    tecnica = forms.CharField()
    material = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField()
    autor = forms.CharField()
    fecha = forms.DateField()