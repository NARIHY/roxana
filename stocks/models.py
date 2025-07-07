import uuid
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Materiel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='materiels')
    description = models.TextField(blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    qr_code_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nom} - {self.categorie.nom}"
