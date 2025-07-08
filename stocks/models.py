import uuid
from django.db import models
from io import BytesIO
import qrcode
from django.core.files.base import ContentFile
from datetime import datetime

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

    def save(self, *args, **kwargs):
        if not self.qr_code_image:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(str(self.uid))
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            date_str = datetime.now().strftime('%Y-%m-%d')
            model_name = self.__class__.__name__
            action = 'create' if self._state.adding else 'update'
            file_name = f'qrcode_{self.uid}.png'
            upload_path = f'images/{model_name}/{date_str}/{action}/{file_name}'
            self.qr_code_image.save(upload_path, ContentFile(buffer.getvalue()), save=False)
        super().save(*args, **kwargs)

    @property
    def qr_code_image_url(self):
        if self.qr_code_image:
            return self.qr_code_image.url
        return None
