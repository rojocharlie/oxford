from django import forms
from .models import Vale, Material, Maestro

class ValeForm(forms.Form):
	no_folio = forms.IntegerField(min_value=0)
	maestro = forms.ModelChoiceField(queryset=Maestro.objects.all())
	material_1 = forms.ModelChoiceField(queryset=Material.objects.all())
	cantidad_1 = forms.IntegerField(min_value=0)
	material_2 = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
	cantidad_2 = forms.IntegerField(min_value=0, required=False)
	material_3 = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
	cantidad_3 = forms.IntegerField(min_value=0, required=False)
	material_4 = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
	cantidad_4 = forms.IntegerField(min_value=0, required=False)
	material_5 = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
	cantidad_5 = forms.IntegerField(min_value=0, required=False)
	material_6 = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
	cantidad_6 = forms.IntegerField(min_value=0, required=False)

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