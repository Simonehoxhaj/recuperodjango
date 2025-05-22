from django.db import models

# Create your models here.

class Autore(models.Model):
    username = models.CharField(max_length=50)


class Commento(models.Model):
    data = models.DateField(auto_now_add=True)
    testo = models.TextField()
    autore = models.ForeignKey(Autore,on_delete=models.CASCADE)
