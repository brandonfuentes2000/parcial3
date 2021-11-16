# Crear el modelo en el archivo cookbook/ingredients/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    dosis = models.TextField()
    category = models.ForeignKey(
        Category, related_name="vacunas", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
