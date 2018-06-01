from django.contrib import admin
from .models import *

class QuartelAdmin(admin.ModelAdmin):
    #fields = ['nome', 'cidade']
    search_fields = ['nome']
    list_filter = ['cidade']
    list_display = ('nome', 'cidade')
admin.site.register(Quartel, QuartelAdmin)

class MilitarAdmin(admin.ModelAdmin):
    #fields = ['nome', 'cidade']
    search_fields = ['nome']
    list_filter = ['patente', 'lotacao']
    list_display = ('nome_guerra', 'sangue', 'patente', 'lotacao')
admin.site.register(Militar, MilitarAdmin)




admin.site.register(Estado)
admin.site.register(Cidade_Quartel)
admin.site.register(Cidade_Natal)

admin.site.register(Tipo_Patente)
admin.site.register(Patente)
admin.site.register(Secao)
admin.site.register(Cargo_Funcao)
admin.site.register(Comportamento)

admin.site.register(Promocao)
admin.site.register(Tipo_Dispensa)
admin.site.register(Dispensa)
admin.site.register(Ferias)
admin.site.register(Tipo_Recompensa)
admin.site.register(Recompensa)
admin.site.register(Tipo_Punicao)
admin.site.register(Punicao)
admin.site.register(Viatura)
admin.site.register(Abastecimento)
admin.site.register(Area_ocorrencia)
admin.site.register(Area_prevencao)
admin.site.register(Tipo_ocorrencia)
admin.site.register(Tipo_prevencao)
admin.site.register(Cidade_ocorrencia)
admin.site.register(Cidade_prevencao)
admin.site.register(Bairro_ocorrencia)
admin.site.register(Bairro_prevencao)

class OcorrenciaAdmin(admin.ModelAdmin):
    #fields = ['nome', 'cidade']
    search_fields = ['tipo', 'livro', 'cidade']
    list_filter = ['tipo', 'livro', 'cidade', 'viaturas', 'atendimento', 'bairro']
    list_display = ('data_saida', 'livro', 'atendimento', 'cidade')
admin.site.register(Ocorrencia, OcorrenciaAdmin)

class PrevencaoAdmin(admin.ModelAdmin):
    #fields = ['nome', 'cidade']
    search_fields = ['tipo', 'livro', 'cidade']
    list_filter = ['tipo', 'livro', 'cidade', 'viaturas', 'atendimento', 'bairro']
    list_display = ('data_saida', 'livro', 'atendimento', 'cidade')
admin.site.register(Prevencao, PrevencaoAdmin)




# Register your models here.
