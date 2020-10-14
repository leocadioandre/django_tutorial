from django.contrib import admin
from .models import Post

# Register your models here.

#Configura o painel admin do django com o app

#admin.site.register(Post)

@admin.register(Post) #a classe q irá gerenciar as aplicações
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado','status')
    list_filter = ('status', 'criado', 'publicado','autor')
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)} #ele vai se basear no titulo para indicar o slug de forma automatica
    
    
    
"""
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
"""                                 