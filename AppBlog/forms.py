from django import forms

from AppBlog.models import Knit, Yarn, Accessories, KnitComment, YarnComment, AccessoriesComment


class KnitForm(forms.ModelForm):
    class Meta:
        model = Knit
        fields = "__all__"


class YarnForm(forms.ModelForm):
    class Meta:
        model = Yarn
        fields = "__all__"


class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = "__all__"


class SearchKnitForm(forms.Form):
    nombre = forms.CharField()


class SearchYarnForm(forms.Form):
    nombre = forms.CharField()


class SearchAccessoriesForm(forms.Form):
    nombre = forms.CharField()


class KnitCommentForm(forms.ModelForm):
    class Meta:
        model = KnitComment
        fields = ("tejido", "usuario", "comentario")


class YarnCommentForm(forms.ModelForm):
    class Meta:
        model = YarnComment
        fields = ("hilado", "usuario", "comentario")


class AccessoriesCommentForm(forms.ModelForm):
    class Meta:
        model = AccessoriesComment
        fields = ("accesorio", "usuario", "comentario")