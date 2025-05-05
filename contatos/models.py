from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return  self.nome

class Contato(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='picture/%y/%m/')
    categoria = models.ForeignKey(Categoria, 
                                  on_delete=models.SET_NULL, 
                                  blank=True, 
                                  null=True)

    def __str__(self) -> str:
        return  f'{self.first_name} {self.last_name}'
