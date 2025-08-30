import qrcode
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

from django.db import models

class Beneficiary(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    fingerprint_hash = models.CharField(max_length=255)
    boundary_partner = models.CharField(max_length=255, null=True, blank=True)
    progress_marker_status = models.JSONField(null=True, blank=True)

    # ✅ Add this field to store the QR code image
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.unique_id})"

    # ✅ Override the save method to generate QR code
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        qr_data = f"ID:{self.unique_id};Name:{self.name};Photo:{self.photo.url};Fingerprint:{self.fingerprint_hash}"
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        filename = f"{self.unique_id}_qr.png"
        self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)
# Create your models here.
