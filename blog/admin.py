from django.contrib import admin
from .models import Post

# Register your models here.

#Configura o painel admin do django com o app

admin.site.register(Post)