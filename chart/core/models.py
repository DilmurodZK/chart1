from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Postlar"

    nomi = models.CharField(max_length=50)
    korsatkichi = models.IntegerField()
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.nomi

class Population(models.Model):

    nomi = models.CharField(max_length=50)
    soni = models.IntegerField()

    def __str__(self):
        return self.nomi

class Area(models.Model):

    nomi = models.CharField(max_length=50)
    miqdori = models.IntegerField()

    def __str__(self):
        return self.nomi