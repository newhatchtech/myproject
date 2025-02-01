from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import ContactRequest


def index(request):
    return render(request, 'myapp/index.html')


from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages


def submit_form(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        investment = request.POST.get('investment')
        case_outline = request.POST.get('case_outline')

        # Save data to the database
        Consultation.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            investment=investment,
            case_outline=case_outline,
        )

        messages.success(request, "Form submitted successfully!")
        return redirect('form_page')  # Replace 'form_page' with the actual name of your URL pattern

    return render(request, "form_template.html")  # Replace 'form_template.html' with your template

def form_page(request):
    return render(request, 'form_page.html')  # Replace 'form_page.html'

def view_consultations(request):
    consultations = Consultation.objects.all()
    return render(request, 'view_consultations.html', {'consultations': consultations})


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import ContactRequest


def contact_page(request):
    return render(request, 'contact.html')
def faq(request):
    return render(request, 'myapp/faq.html')

def testimonials(request):
    
    return render(request, 'myapp/testimonials.html')

def contactinfos(request):
    
    return render(request, 'myapp/contactinfos.html')
def muea(request):
    
    return render(request, 'myapp/muea.html')
def cyberinvestigations(request):
    return render(request, 'myapp/cyberinvestigations.html')
def cryto(request):
    return render(request, 'myapp/cryto.html')

def adr(request):
    return render(request, 'myapp/adr.html')
def adradvance(request):
    return render(request, 'myapp/adradvance.html')
def ami(request):
    return render(request, 'myapp/ami.html')
def binary(request):
    return render(request, 'myapp/binary.html')
def claim(request):
    return render(request, 'myapp/claim.html')
def credit(request):
    return render(request, 'myapp/credit.html')
def digital(request):
    return render(request, 'myapp/digital.html')
def force(request):
    return render(request, 'myapp/force.html')
def forex(request):
    return render(request, 'myapp/forex.html')
def kyc(request):
    return render(request, 'myapp/kyc.html')
def others(request):
    return render(request, 'myapp/others.html')
def property(request):
    return render(request, 'myapp/property.html')
def regulatory(request):
    return render(request, 'myapp/regulatory.html')
def restituation(request):
    return render(request, 'myapp/restituation.html')
def romance(request):
    return render(request, 'myapp/romance.html')
def stock(request):
    return render(request, 'myapp/stock.html')


from django.shortcuts import render, redirect
from .models import ConsultationRequest
from django.shortcuts import render, redirect
from .models import ConsultationRequest

def submit_form(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        investment = request.POST.get("investment")
        case_details = request.POST.get("case_details")

        ConsultationRequest.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            investment=investment,
            case_details=case_details,
        )
        return redirect("success_page")  # Redirect to a success page after submission

    return render(request, "success_page.html")


def success_view(request):
    return render(request, 'myapp/success_template.html') 

from django.shortcuts import redirect
from .models import ContactRequest


from django.shortcuts import redirect, render
from django.urls import reverse

def contact_request_view(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        country_code = request.POST.get('country_code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        scam_type = request.POST.get('scam_type')
        amount_lost = request.POST.get('amount_lost') or None
        case_outline = request.POST.get('case_outline')

        # Save the data into the database
        ContactRequest.objects.create(
            purpose=purpose,
            country_code=country_code,
            phone=phone,
            email=email,
            scam_type=scam_type,
            amount_lost=amount_lost,
            case_outline=case_outline,
        )

        # Redirect to Muea page and scroll to #thank-you-section
        return redirect(reverse('muea') + '#thank-you-section')

    # If the request is not POST, render the contact form
    return render(request, 'contact_request_form.html')


from django.shortcuts import redirect, render
from django.urls import reverse

def contact_request_view(request):
    if request.method == 'POST':
        purpose = request.POST.get('purpose')
        country_code = request.POST.get('country_code')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        scam_type = request.POST.get('scam_type')
        amount_lost = request.POST.get('amount_lost') or None
        case_outline = request.POST.get('case_outline')

        # Save the data into the database
        ContactRequest.objects.create(
            purpose=purpose,
            country_code=country_code,
            phone=phone,
            email=email,
            scam_type=scam_type,
            amount_lost=amount_lost,
            case_outline=case_outline,
        )

        # Redirect to the Muea page and scroll to the #thank-you-section
        return redirect(reverse('muea') + '#thank-you-section')

    # If the request is not POST, render the contact form
    return render(request, 'contact_request_form.html')





from django.shortcuts import render, redirect
from .forms import InvestmentForm
from .models import InvestmentData

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InvestmentData
from django.shortcuts import render, redirect
from .models import InvestmentData
from .forms import InvestmentForm

def multi_step_form(request):
    if request.method == 'POST':
        # Handle the form submission (final step in the multi-step process)
        investment_data = InvestmentData(
            investment_amount=request.POST.get('investment_amount'),
            payment_method=request.POST.get('payment_method'),
            additional_info=request.POST.get('additional_info'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone_number=request.POST.get('phone_number')
        )
        investment_data.save()

        # After saving, redirect to a success or thank-you page
        return redirect('/muea/#thank-you-section')  #  # Adjust this URL based on your needs

    else:
        # If it's not a POST request, display the form (for the first step)
        form = InvestmentForm()

        # Make sure you render the form and return the response
        return render(request, 'myapp/multi_step_form.html', {'form': form})

def login(request):
    return render(request, 'myapp/login.html')