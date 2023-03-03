from re import VERBOSE
from tabnanny import verbose

from conta.models import User
from django.db import models

# # Create your models here.


class Publicacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40, verbose_name='Título')
    tipo = models.CharField(max_length=100, verbose_name=('*Tipo de Evento'))
    public = models.CharField(max_length=100, verbose_name=('*Público-alvo'))
    data_evento = models.DateField()
    img = models.ImageField(null=True, blank=True,
                            upload_to='imagens/', verbose_name='*Foto')
    local = models.CharField(max_length=100, verbose_name='*Local')
    custo = models.FloatField()
    descricao = models.TextField(max_length=100, verbose_name=('*Descrição'))

    topensando = models.ManyToManyField(User, related_name='Topensando')
    euvou = models.ManyToManyField(User, related_name='Euvou')
    denuncia = models.IntegerField(verbose_name='Denuncia')

    def __str__(self):
        return "{} ({})".format(self.usuario, self.titulo, self.usuario)

    def number_of_topensando(self):
        return self.topensando.count()

    def number_of_euvou(self):
        return self.euvou.count()
