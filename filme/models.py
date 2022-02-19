from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser  # importa o módulo usuário padrão do django

# Create your models here /  criação de tabelas, post, usuário playlist, atraves de classes.
# classe models: modelo padrão do django.

# lista de categorias
LISTA_CATEGORIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros")
)


# criar campos das classes/tabelas
class Filme(models.Model):
    titulo = models.CharField(max_length=100)  # char field, campo de texto;
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)  # campo de texto
    categoria = models.CharField(max_length=20, choices=LISTA_CATEGORIAS)  # choices definir escolha em uma tupla.
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

    # timezone.now pega a hora atual no momento em que o filme foi criado.

    # retorna um nome string para substituir o nome do tipo no formato de objeto.
    def __str__(self):
        return self.titulo


"""Lembrar de instalar a bibliteca pillow que auxilia o django a trabalhar com imagens"""

"""CLASSE EM DJANGO SE ESCREVE NO SINGULAR"""


class Episodio(models.Model):
    # classe ep, que filme é um campo id relacional a classe Filme.
    # argumentos: Nome da classe, identificador de ep pode ser passado para html atraves de class view
    # on delete: garante a exclusão de todos os arquivos se o Filme for deletado.
    filme = models.ForeignKey("Filme", related_name='episodio', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()  # campo de url do video

    def __str__(self):
        return self.filme.titulo + " - " + self.titulo


# criando usuários no django.
"""O módulo padrão já constrói os campos de usuário,
sendo o objetivo secundário da classe a inclusão de um campo relacional
de muitos pra muitos: videos assistidos.

Uma véz que o usuario é criado é necessario incluir no admin,
e o padrão django admin migra junto."""

"""é importante definir esse usuário na primeira migração para evitar ter que deletar as migrações e o db"""


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")



