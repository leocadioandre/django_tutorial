from django.contrib import admin
from .models import Post, Category

# Register your models here.

@admin.register(Category) #a classe q irá gerenciar as aplicações
class PostAdmin(admin.ModelAdmin):
    list_display = ('nome','criado','publicado')
    list_filter = ('nome','criado','publicado')
    date_hierarchy = 'publicado'
    search_fields = ('nome',)


#Configura o painel admin do django com o app

#admin.site.register(Post)

@admin.register(Post) #a classe q irá gerenciar as aplicações
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado','status')
    list_filter = ('status', 'criado', 'publicado','autor')
    readonly_fields = ('visualizar_imagem',)
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)} #ele vai se basear no titulo para indicar o slug de forma automatica
    
    def visualizar_imagem(self,obj):
        return obj.view_image
    visualizar_imagem.short_description = "Imagem Cadastrada"

    
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