from django.contrib import admin

from .models import Quadros

from .models import Conteudo

from .models import Assuntos



@admin.register(Quadros)
class QuadrosAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','title_quadro01','title_quadro02','title_quadro03')


@admin.register(Conteudo)
class ConteudoAdmin(admin.ModelAdmin):
    list_display = ('assunto','title','cor', 'identificacao')

@admin.register(Assuntos)
class AssuntosAdmin(admin.ModelAdmin):
    list_display = ('name','slug','aba')
    
    