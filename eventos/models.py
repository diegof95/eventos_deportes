from django.db import models
from django.urls import reverse
from django.core import validators

from usuarios.models import Usuario

class Estadio(models.Model):
    nombre = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50, null=True,blank=True)
    max_capacidad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class TipoEvento(models.Model):
    nombre = models.CharField(max_length=16)

    class Meta:
        verbose_name_plural = "Tipos de Eventos"

    def __str__(self):
        return self.nombre

class Evento(models.Model):

    tipo = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=70, null=True, blank=True)
    fecha = models.DateField()
    hora = models.TimeField()
    imagen = models.ImageField(
        upload_to='eventos/imagenes',
        blank=True,
        null=True)

    ESTADOS = [
        ('no_publicado','No Publicado'),
        ('publicado','Publicado'),
        ('cancelado','Cancelado'),
        ('realizado','Realizado'),
    ]
    estado = models.CharField(max_length=12, choices=ESTADOS)

    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)

    creado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)
    
    creador = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        
        return reverse('eventos:detalles', kwargs={'pk': self.id})

    def __str__(self):
       return self.nombre

class LocalidadEvento(models.Model):

    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    localidad = models.CharField(max_length=20)
    aforo = models.PositiveIntegerField()
    
    # Representa desde 0 hasta ((10E15)-1),99 en pesos.
    precio = models.DecimalField(
        max_digits=17,
        decimal_places=2,
        validators=[validators.MinValueValidator(0)]
    )

    class Meta:
        unique_together = ('evento', 'localidad')
        verbose_name_plural = "Localidades Evento"

    def __str__(self):
        return "{}: {}".format(self.evento.__str__(), self.localidad)