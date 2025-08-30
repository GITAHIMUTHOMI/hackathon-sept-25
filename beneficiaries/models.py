from django.db import models

class Beneficiary(models.Model):
    unique_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')
    fingerprint_hash = models.CharField(max_length=255)
    boundary_partner = models.CharField(max_length=255)
    progress_marker_status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.unique_id})"

# Create your models here.
