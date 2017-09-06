from django.shortcuts import render, get_object_or_404, redirect
from .forms import PickyAuthenticationForm, NoticiaForm
from .models import Noticia
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	instance = Noticia.objects.order_by('-fecha_publicacion')[1:3]
	noticia_last = Noticia.objects.order_by('-fecha_publicacion')[0]

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			user = request.user
			return render(request, 'index.html',{'user': user, 'noticias':instance, 'last':noticia_last})
  	      	# Redirect to a success page.
		else:
   	    	 # Return an 'invalid login' error message.
			pass

	if request.user.is_authenticated == False:
		return render(request, 'index.html',{'user': '', 'noticias':instance, 'last':noticia_last, 'form': PickyAuthenticationForm})
	else:
		return render(request, 'index.html',{'user': request.user, 'noticias':instance, 'last':noticia_last})

def noticia_view(request, id):
	instance = get_object_or_404(Noticia, id=id)
	return render(request, 'noticia_view.html', {'noticia':instance})

def noticia_add(request):
	form = NoticiaForm()
	if request.method=='POST':
		form = NoticiaForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.save()
			return redirect('index')
	return render(request, 'noticia_form.html', {'form':form})

def logout_view(request):
	logout(request)
	return render(request, 'logout.html', {})