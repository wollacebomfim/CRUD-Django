from django.db import models

class Usuarios(models.Model):

    nome = models.CharField(max_length=100)
    sobrenome =  models.TextField(max_length=255)
    email = models.EmailField(max_length=100)
    permissao = models.TextField(max_length=30)
   
    #data_cadastro = models.DateTimeField(auto_now=())

  
    def __str__(self):
        return self.nome



class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=100)


    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.TextField(max_length=100)
    estoque = models.IntegerField()
    minimo = models.IntegerField()
    custo = models.FloatField()
    valor = models.FloatField()

