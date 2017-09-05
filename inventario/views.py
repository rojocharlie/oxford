from django.shortcuts import render, redirect
from .models import Vale, DetalleMaterial
from .forms import ValeForm, MaestroForm, MaterialForm

# Create your views here.

def vale_add(request):
    form = ValeForm()
    last_folio = Vale.objects.order_by('-no_folio')[0]
    new_folio = 1 + last_folio.no_folio
    if request.method == 'POST':
        form = ValeForm(request.POST)
        if form.is_valid():
            d = DetalleMaterial(material=form.cleaned_data['material'], cantidad=form.cleaned_data['cantidad'])
            d.save()
            if form.cleaned_data['material2'] and form.cleaned_data['cantidad2']:
                d2 = DetalleMaterial(material=form.cleaned_data['material2'], cantidad=form.cleaned_data['cantidad2'])
                d2.save()
            if form.cleaned_data['material3'] and form.cleaned_data['cantidad3']:
                d3 = DetalleMaterial(material=form.cleaned_data['material3'], cantidad=form.cleaned_data['cantidad3'])
                d3.save()
            if form.cleaned_data['material4'] and form.cleaned_data['cantidad4']:
                d4 = DetalleMaterial(material=form.cleaned_data['material4'], cantidad=form.cleaned_data['cantidad4'])
                d4.save()
            if form.cleaned_data['material5'] and form.cleaned_data['cantidad5']:
                d5 = DetalleMaterial(material=form.cleaned_data['material5'], cantidad=form.cleaned_data['cantidad5'])
                d5.save()
            v = Vale(no_folio=new_folio, maestro=form.cleaned_data['maestro'])
            v.save()
            v.material.add(d)
            try:
                v.material.add(d2)
            except:
                pass
            try:
                v.material.add(d3)
            except:
                pass
            try:
                v.material.add(d4)
            except:
                pass
            try:
                v.material.add(d5)
            except:
                pass

            return redirect('vale_check')

    return render(request, 'vale_add.html', {'formulario':form, 'folio':new_folio})

def vale_check(request):
    instance = Vale.objects.all()
    return render(request, 'vale_check.html', {'lista':instance})

def maestro_add(request):
    form = MaestroForm()
    if request.method == 'POST':
        form = MaestroForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('maestro_add')

    return render(request, 'maestro_add.html', {'formulario':form})

def material_add(request):
    form = MaterialForm()
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('material_add')
    return render(request, 'material_add.html', {'formulario':form})
