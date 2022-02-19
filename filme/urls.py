from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhesfilme, Pesquisafilme, Paginaperfil, Criarconta
from django.contrib.auth import views as auth_view  # varios em um


# comando geral de link do app

# ao passar o parâmetro name em cada url, ele pode ser utilizado como identificador dinâmico, na tag a no template
# assim utilizamos um link dinâmico (parâmetro de classe) ao invés de um link fixo direto que poderia atrapalhar o site
# caso houvesse mudanças em urls.

app_name = 'filme'

urlpatterns = [
    # texto em branco cria a homepage, métodos de classe
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    # pk : primary key do modelo Filme
    path("filmes/<int:pk>", Detalhesfilme.as_view(), name="detalhesfilmes"),
    path('pesquisa/', Pesquisafilme.as_view(), name="pesquisafilme"),
    path('login', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name='editarperfil'),
    path('criarconta/', Criarconta.as_view(), name='criarconta'),
    path('mudarsenha/', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha')
]
