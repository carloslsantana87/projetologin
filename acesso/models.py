from django.conf import settings
from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    telefone = models.CharField(max_length=200)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.save()

    def __str__(self):
        return f"{self.usuario.username} - {self.telefone}"  # Retorna o nome do usuário e o telefone
