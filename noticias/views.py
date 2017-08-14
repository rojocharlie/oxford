from django.shortcuts import render, get_object_or_404
from .forms import PickyAuthenticationForm
from .models import Noticia
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
	instance = Noticia.objects.order_by('-fecha_publicacion')[1:3]
	noticia_last = Noticia.objects.order_by('-fecha_publicacion')[0]
	if request.user.is_authenticated:
		user = request.user
		return render(request, 'index.html',{'user': user, 'noticias':instance, 'last':noticia_last})
	else:
		return render(request, 'index.html',{'user': '', 'noticias':instance, 'last':noticia_last})

def noticia_view(request, id):
	instance = get_object_or_404(Noticia, id=id)
	return render(request, 'noticia_view.html', {'noticia':instance})

def my_view(request):
	if request.method == 'POST':
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        login(request, user)
	        # Redirect to a success page.
	        pass
	    else:
	        # Return an 'invalid login' error message.
	        pass
	return render(request, 'login.html', {'form': PickyAuthenticationForm})


def logout_view(request):
    logout(request)
    return render(request, 'logout.html', {})