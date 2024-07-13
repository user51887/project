from django.db import models

# Create your models here.

class Equipes(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='equipes/')    

    class Meta:
        verbose_name = 'equipe'
        verbose_name_plural = 'equipes'

    def __str__(self):
        return self.name