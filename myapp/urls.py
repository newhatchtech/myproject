from django.urls import path
from . import views  # Import your views
from .views import success_view
# myapp/urls.py
from .views import muea
from .views import multi_step_form
from .views import login
from .views import faq



urlpatterns = [
    path('submit-form/', views.submit_form, name='submit_form'),
    path('form-page/', views.form_page, name='form_page'),
    path('contact/', views.contact_request_view, name='contact_request_view'),
    path('consultations/', views.view_consultations, name='view_consultations'),
    path('contact-request/', views.contact_request_view, name='contact_request_view'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contactinfos/', views. contactinfos, name=' contactinfos'),
    path('cyberinvestigations/', views.cyberinvestigations, name='cyberinvestigations'),
    path('cryto/', views.cryto, name='cryto'),
     path('adr/', views.adr, name='adr'),
    path('adradvance/', views.adradvance, name='adradvance'),
    path('ami/', views.ami, name='ami'),
    path('binary/', views.binary, name='binary'),
    path('claim/', views.claim, name='claim'),
    path('credit/', views.credit, name='credit'),
    path('digital/', views.digital, name='digital'),
    path('force/', views.force, name='force'),
    path('forex/', views.forex, name='forex'),
    path('kyc/', views.kyc, name='kyc'),
    path('others/', views.others, name='others'),
    path('property/', views.property, name='property'),
    path('regulatory/', views.regulatory, name='regulatory'),
    path('restitution/', views.restituation, name='restitution'),
    path('romance/', views.romance, name='romance'),
    path('stock/', views.stock, name='stock'),
    path("submit-form/", views.submit_form, name="submit_form"),
    path('success/', success_view, name='success'),
    path('muea/', views.muea, name='muea'),
    path('contactinfos/', views.contactinfos, name='contactinfos'),
    path('success/', views.success_view, name='success_page'),  # The name must be 'success_page'
    path('login/', views.login, name='login'),
    path('faq/',views.faq, name='faq'),
    
    path('multi-step-form/', multi_step_form, name='multi_step_form'),
  
    
    
]
