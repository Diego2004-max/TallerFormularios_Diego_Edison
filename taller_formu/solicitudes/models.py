from django.db import models
from django.core.validators import RegexValidator

TIPO_CHOICES = [
    ('academica', 'Académica'),
    ('administrativa', 'Administrativa'),
    ('tecnica', 'Técnica'),
    ('otra', 'Otra'),
]

# Validador simple para teléfono: sólo dígitos entre 7 y 15
telefono_validator = RegexValidator(r'^\d{7,15}$', 'Ingrese entre 7 y 15 dígitos.')

class Solicitud(models.Model):
    nombre = models.CharField('Nombre solicitante', max_length=150)
    documento = models.CharField('Documento de identidad', max_length=50)
    correo = models.EmailField('Correo electrónico')
    telefono = models.CharField('Teléfono de contacto', max_length=20, validators=[telefono_validator])
    tipo = models.CharField('Tipo de solicitud', max_length=20, choices=TIPO_CHOICES)
    asunto = models.CharField('Asunto', max_length=200)
    descripcion = models.TextField('Descripción detallada')
    fecha = models.DateField('Fecha de la solicitud')
    archivo = models.FileField('Archivo adjunto', upload_to='solicitudes_adjuntos/', blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.asunto} ({self.tipo})"
