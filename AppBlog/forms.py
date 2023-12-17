from django import forms

from AppBlog.models import Knit, Yarn, Accessories


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