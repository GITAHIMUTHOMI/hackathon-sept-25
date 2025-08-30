from django import forms
from .models import Beneficiary

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ['name', 'photo', 'fingerprint_hash', 'boundary_partner', 'progress_marker_status']