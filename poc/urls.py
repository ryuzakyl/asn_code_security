from django.urls import path

from . import views

urlpatterns = [
    path('csrf-protection', views.csrf_protection, name='csrf_protection'),
]
