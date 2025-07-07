import qrcode
from io import BytesIO
from django.core.files import File
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Materiel

@receiver(post_save, sender=Materiel)
def generate_qr_code(sender, instance, created, **kwargs):
    if created and not instance.qr_code_image:
        data = f"http://localhost:8000/stocks/materiels/{instance.uid}/"
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        instance.qr_code_image.save(f"qr_{instance.uid}.png", File(buffer), save=True)
