from django.urls import path
from . import views

urlpatterns = [
    # Beneficiary registration
    path('register/', views.register_beneficiary, name='register_beneficiary'),
    path('success/<int:beneficiary_id>/', views.registration_success, name='registration_success'),

    # QR code scanning and verification
    path('scan/', views.scan_qr_page, name='scan_qr'),
    path('verify/<str:unique_id>/', views.verify_beneficiary, name='verify_beneficiary'),

    # Test view
    path('test/', views.test_home, name='test_home'),
]