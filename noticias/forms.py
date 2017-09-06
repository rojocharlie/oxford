from django.contrib.auth.forms import AuthenticationForm
from .models import Noticia
from django import forms

class PickyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                _("This account is inactive."),
                code='inactive',
            )
        if user.username.startswith('b'):
            raise forms.ValidationError(
                _("Sorry, accounts starting with 'b' aren't welcome here."),
                code='no_b_users',
            )

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = '__all__'