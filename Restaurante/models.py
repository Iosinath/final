from django.db import models

# Create your models here.
class Menu(models.Model):
    ID = models.AutoField (primary_key = True)
    Título = models.CharField(max_length = 100, verbose_name='Título')
    Imagen = models.ImageField(upload_to ='imagenes/',verbose_name = "Imagen", null = True)
    Descripción = models.TextField(verbose_name = "Descripción", null =True)

    def __str__(self):
        fila = "Título: " + self.Título + " - " + " Descripción: " + self.Descripción
        return fila

    def delete(self, using=None, keep_parent=False):
        self.Imagen.storage.delete(self.Imagen.name)
        super().delete()

