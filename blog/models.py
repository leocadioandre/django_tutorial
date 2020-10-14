from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #nosso usuário


#Filtra os posts publicados
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='publicado')

class Post(models.Model):
    STATUS = (
        ('rascunho','Rascunho'),
        ('publicado', 'Publicado'),
        
    )
    titulo = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250) #https://site.com/noticias/campeonato-brasileiro-2020/01/02/2020 - o slug é a partir do /campeonato ... 
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #o cascade indica que ao excluir o user ele vai excluiur todos os posts do autor
    conteudo = models.TextField()
    
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True) #oculto
    alterado  = models.DateTimeField(auto_now=True) #oculto
    status    = models.CharField(max_length=10,
                                 choices=STATUS,
                                 default='rascunho')
    
    published = PublishedManager()

#alterar a ordem que é exibida as alterações - se remover o sinal de - volta a forma de antes

    class Meta:
        ordering = ('-publicado',)


#indica o titulo
    
    def __str__(self):
        return self.titulo
       #return '{} - {} '.format(self.titulo, self.slug)


# Create your models here.
