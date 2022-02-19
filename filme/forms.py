from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


# cria um usuário de acordo com o padrão classe Usuário.
class CriarContaForm(UserCreationForm):
    # define o email obrigatório.
    email = forms.EmailField()

    class Meta:
        # 'conecta' o formulário de acordo com os campos da classe Usuário.
        model = Usuario
        # define os campos específicos
        fields = ('username', 'email', 'password1', 'password2')


#  classe de formulário nos moldes padrão form
class FormHome(forms.Form):
    email = forms.EmailField(label=False)

