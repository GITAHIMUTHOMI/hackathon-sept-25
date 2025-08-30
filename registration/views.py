from django.shortcuts import render, redirect
from .forms import BeneficiaryRegistrationForm
from .models import Beneficiary
import qrcode
from io import BytesIO
from django.core.files import File

def register_beneficiary(request):
    if request.method == 'POST':
        form = BeneficiaryRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            beneficiary = form.save()

            # Generate QR code
            qr_data = beneficiary.unique_id
            qr = qrcode.make(qr_data)
            buffer = BytesIO()
            qr.save(buffer)
            filename = f'{beneficiary.unique_id}_qr.png'
            beneficiary.qr_code.save(filename, File(buffer), save=True)

            return redirect('registration_success', beneficiary_id=beneficiary.id)
    else:
        form = BeneficiaryRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# ✅ Paste the success view here
def registration_success(request, beneficiary_id):
    beneficiary = Beneficiary.objects.get(id=beneficiary_id)
    return render(request, 'registration/success.html', {'beneficiary': beneficiary})
    from django.shortcuts import render, get_object_or_404
from .models import Beneficiary

def verify_beneficiary(request, unique_id):
    beneficiary = get_object_or_404(Beneficiary, unique_id=unique_id)
    return render(request, 'registration/verify.html', {'beneficiary': beneficiary})
    def scan_qr_page(request):
    return render(request, 'registration/scan_qr.html')
    def test_home(request):
    return HttpResponse("DART PMEARL System is up and running!")