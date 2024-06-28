from django.db import models

class Vendas(models.Model):
    ano = models.IntegerField(null=False, blank=False)
    vendas = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Vendas em {self.ano}"

class Revistas(models.Model):
    ano = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    tema = models.CharField(max_length=255)
    secao = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    genero_textual = models.CharField(max_length=255)
    palavra_chave1 = models.CharField(max_length=100)
    palavra_chave2 = models.CharField(max_length=100, blank=True, null=True)
    palavra_chave3 = models.CharField(max_length=100, blank=True, null=True)
    sexo_autor = models.CharField(max_length=50)

    # dados.xlsx -> até 22.1 OK

    def __str__(self):
        return f"Volume nº {self.volume}"