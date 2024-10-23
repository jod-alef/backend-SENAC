from django.db import models


# Modelo para Imóveis
class Imovel(models.Model):
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    preco_aluguel = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.endereco} = {self.cidade}/{self.estado}"


# Modelo para Inquilinos

class Inquilino(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.imovel.endereco}"


# Modelo para Alugueis

class Aluguel(models.Model):
    inquilino = models.ForeignKey(Inquilino, on_delete=models.CASCADE)
    data_vencimento = models.DateField()
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return f"Aluguel de {self.inquilino.nome} - {self.data_vencimento}"
