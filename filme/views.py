from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DeleteView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, FormHome

""" LoginRequiredMixin: classe responsável por bloquear o acesso para determinadas views, ela deve ser o primeiro
argumento na criação de class view, uma vez definido o bloqueio
 é necessário configurar em settings as urls de redirect.
"""

"""
A função retorna diretamente o template, nas classes base views as funções da classe são evocadas.
Ao definir nossas classes temos que ter em mente, uma questão: a natureza da ação, retornar template, exibir lista, etc.

Ver documentação django.views.generic, que é onde estão parte das 
opções de clases que auxiliam a criação de class viwes.

Essas clases além de render passam variáveis de contexto
"""


# class Form View, que necessita de uma class view que foi criada em forms.py
class Homepage(FormView):
    template_name = "homepage.html"
    form_class = FormHome

    # como a função etá sendo editada chamamos a super ao final.
    def get(self, request, *args, **kwargs):
        # se usuário está autenticado
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        # verifica via filtro se o email do banco é igual ao email do post.
        usuario = Usuario.objects.filter(email=email)

        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


# essa classe já passa contexto do models: -> object_list
class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme


#  classe flutuante dos vídeos
class Detalhesfilme(LoginRequiredMixin, DeleteView):
    template_name = "detalhesfilme.html"
    model = Filme

    # object -> Passa um item do modelo filme.

    # função editada para contar as visualizações de videos via request do filme(quando ele entra na pagina);
    # após a contagem ela chama a função get para encaminhar para url.
    def get(self, request, *args, **kwargs):
        filme = self.get_object()  # pega as informações do do filme específico.
        filme.visualizacoes += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)  # redireciona o usuário para url final.

    # passa as informações de filmes relacionados por categoria. passa somente para uma view, detalhes filmes.
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data()
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


# foi criada uma classe que recebe a list view porque o objetivo d é retornar uma lista de filmes relacionados a pesquisa
# se o usuário entrar direto na url/pesquisa

# havendo pesquisa
# ao iniciar o request, capture a palavra chave query.
# por fim a list view retorna uma lista, porém nesse momento essa lista é editada por get_queryset.
# os diversos parametros podem ser capturados.
class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            return None


# editar perfil do usuário
"""Classe update view que atualiza um campo na tabela usuário
ela cria um formulário, recebe os capos que serão alterados a partir de lista.
 e recebe o modelo/tabela padrão"""


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


# criar conta de usuário / configurado como form view, que por padrão recebe um template e uma class de formulário.
class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    # verifica a validade do formulário, foi editada para salvar as inf no banco de dados.
    # editou chama a super.
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # função que recebe somente uma url para o usuário.
    def get_success_url(self):
        return reverse('filme:login')
