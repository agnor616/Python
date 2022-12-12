from django.forms import ModelForm
from app.models import carro, motorista

class carroForm(ModelForm):
    class Meta:
        model = carro
        fields = ['placa','marca','veiculo','km_Troca_Oleo']
        
class motoristaForm(ModelForm):
    class Meta:
        model = motorista
        fields = ['Nome','Telefone','CNH']
        
