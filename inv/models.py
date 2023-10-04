from django.db import models

from bases.models import ClaseModelo

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='DESCRIPCION DE CATEGORIA',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria,self).save()

    class Meta:
        verbose_name_plural = "Categorias"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='DESCRIPCION DE CATEGORIA',
     
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion,self.descripcion)
    
    def save(self):
     self.descripcion = self.descripcion.upper()
     super(SubCategoria,self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria','descripcion')
#primero despuese se migra los datos

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la marca',
        unique=True
    )
    def __str__(self):
        return '{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca,self).save()

    class Meta:
        verbose_name_plural="Marca"
