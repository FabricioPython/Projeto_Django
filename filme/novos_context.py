from .models import Filme

'''GERENCIADOR DE VARIAVEIS DE CONTEXTO: É NECESSÁRIO INCLUIR EM STTINGS O CAMINHO DE CADA UM DAS FUNÇÕES.'''


def lista_filmes_recentes(request):
    """
    :param request:
    :return: um dicionário contendo os filmes em ordem decrescente, por se tratar de data, o ultimo filme postado será
    o primeiro a ser mostrado e o primeiro filme adicionado no banco de dados será o ultimo a ser mostrado.
    essa função serve para passar dados do banco para qualquer lugar do site.
    """
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    if lista_filmes:
        filme_destaque = lista_filmes[0]
    else:
        filme_destaque = None
    return {'lista_filmes_recentes': lista_filmes, 'filme_destaque':filme_destaque}


def lista_de_filmes_emalta(request):
    """
    :param request:
    :return: um dicionário contendo os filmes em alta (com mais visualizações).
    """
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {'lista_filmes_emalta':lista_filmes}


