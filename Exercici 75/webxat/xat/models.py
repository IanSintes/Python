from django.db import models
from django.contrib.auth.models import User

class Missatge(models.Model):
    usuari = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuari.username}: {self.text[:20]}'


# Create your models here.

