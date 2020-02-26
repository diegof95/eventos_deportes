from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=25, blank=True, null=True)
    
    foto = models.ImageField(
        upload_to='usuarios/fotos',
        blank=True,
        null=True)

    ROLES = [
        ('Cliente', 'Cliente'),
        ('Vendedor', 'Vendedor'),
        ('Gerente', 'Gerente'),
        ('Administrador', 'Administrador')
    ]
    rol = models.CharField(
        max_length=15,
        choices=ROLES
    )

    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.username)