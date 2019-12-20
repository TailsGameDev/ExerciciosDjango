from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=150)
    senha = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploadedFiles')

    def __str__(self):
        return self.usuario