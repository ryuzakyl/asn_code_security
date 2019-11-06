from django.urls import path

from . import views

urlpatterns = [
    path('form-validation', views.form_validation, name='form_validation'),
    path('csrf-protection', views.csrf_protection, name='csrf_protection'),
    path('xss-protection', views.xss_protection, name='xss_protection'),
]
