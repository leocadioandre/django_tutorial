from django.contrib import admin
from .models import Link

@admin.register(Link) #a classe q irá gerenciar as aplicações
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('criado', 'alterado')
    list_display = ('chave','criado','alterado')


# Register your models here.
