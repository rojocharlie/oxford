from django import forms
from .models import Vale, Material, Maestro, DetalleMaterial


class ValeForm(forms.Form):
    maestro = forms.ModelChoiceField(queryset=Maestro.objects.all())
    material = forms.ModelChoiceField(queryset=Material.objects.all())
    cantidad = forms.IntegerField(min_value=0)
    material2 = forms.ModelChoiceField(queryset=Material.objects.all(),required=False)
    cantidad2 = forms.IntegerField(min_value=0,required=False)
    material3 = forms.ModelChoiceField(queryset=Material.objects.all(),required=False)
    cantidad3 = forms.IntegerField(min_value=0,required=False)
    material4 = forms.ModelChoiceField(queryset=Material.objects.all(),required=False)
    cantidad4 = forms.IntegerField(min_value=0,required=False)
    material5 = forms.ModelChoiceField(queryset=Material.objects.all(),required=False)
    cantidad5 = forms.IntegerField(min_value=0,required=False)


class MaestroForm(forms.ModelForm):
    class Meta:
        model = Maestro
        fields = (
            'nombre',
            'escuela',
        )


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'nombre',
        )
