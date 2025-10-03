from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Usuario(models.Model):
    usuario = models.CharField(max_length=50, primary_key=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)

    def __str__(self):
        return self.usuario

    def set_password(self, raw_password):
        self.contraseña = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.contraseña)
