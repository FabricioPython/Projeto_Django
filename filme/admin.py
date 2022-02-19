from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin
# Register your models here.

# comando que registra a classe/tabela no django admin.
admin.site.register(Filme)


admin.site.register(Episodio)


# registro de usuário mais o gerenciador de usuários(sessão, login, logout etc)

""""se eu quiser que a informação que eu estou passando a mais para o usuário padrão apareça
na tela inicial com o django admin é necessário editar a estrutura de dados que a classe UserAdmin recebe,
que são as fildsets.

estrutura:

[
    ('informações_pessoais', {'filds: ('primeiro_nome', 'ultimo_nome')})
]


"""

# atribui a lista campos, o itens do usuário padrão.
campos = list(UserAdmin.fieldsets)


# adiciona o campo filmes_vistos que desejo ver no admin.
campos.append(

    ('Histórico', {'fields': ('filmes_vistos',)})

)

# atribui os campos atualizados.
UserAdmin.fieldsets = tuple(campos)

# registro no admin.
admin.site.register(Usuario, UserAdmin)
