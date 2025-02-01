from django.db import models


class ContactRequest(models.Model):
    PURPOSE_CHOICES = [
        ('report', 'Report a scam'),
        ('consult', 'Consult an expert'),
    ]

    SCAM_TYPE_CHOICES = [
        ('phishing', 'Phishing'),
        ('identity_theft', 'Identity Theft'),
        ('online_fraud', 'Online Fraud'),
    ]

    purpose = models.CharField(max_length=20, choices=PURPOSE_CHOICES, blank=True)
    country_code = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    scam_type = models.CharField(max_length=20, choices=SCAM_TYPE_CHOICES, blank=True)
    amount_lost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    case_outline = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.purpose} ({self.submitted_at})"



from django.db import models

class ConsultationRequest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    investment = models.CharField(max_length=20)
    case_details = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
from django.db import models


from django.db import models

from django.db import models

class InvestmentData(models.Model):
    investment_amount = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=255, null=True, blank=True)  # Allow null/blank
    additional_info = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.investment_amount}"
