from django.forms import ModelForm
from .models import Militar

class MilitarForm(ModelForm):
    class Meta:
        model = Militar
        fields = ['nome', 'nome_guerra','matricula','email','patente','lotacao',
                  'cargo_funcao','comportamento','data_inclusao','sangue',
                  'data_nascimento','grau_instrucao','sexo','naturalidade',
                  'nacionalidade','pai','mae', 'foto', 'obs']

