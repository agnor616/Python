from django.db import models



class carro(models.Model):
    id_car = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    veiculo = models.CharField(max_length=20)
    km_Troca_Oleo = models.FloatField(max_length=20)
    

class motorista(models.Model):
    id_motorista = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=25)
    Telefone =  models.CharField(max_length=25)
    CNH =  models.CharField(max_length=25)
    
