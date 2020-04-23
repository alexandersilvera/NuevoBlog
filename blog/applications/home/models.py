from django.db import models
# apps terceros
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """ Modelo de página Principal """
    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'Email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono contacto',
        max_length=20
    )
    logo = models.ImageField(
        'Logo',
        upload_to='home/logo/',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'

    def __str__(self):
        return self.title

class Suscribers(TimeStampedModel):
    """ Modelo de Suscriptores """
    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    """ Modelo de Contacto """
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    messagge = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name



