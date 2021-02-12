from django.db import models


class Produto(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Produto:')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Valor:', help_text='Ex.: 123.45')
    image_url = models.ImageField(verbose_name='Imagem:')

    def __str__(self):
        return self.name
