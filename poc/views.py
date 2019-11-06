from django.shortcuts import render
from django.middleware import csrf

from .forms import CsrfForm, XssForm


def csrf_protection(request):
    context = {}

    if request.method == 'GET':
        csrf_token = csrf.get_token(request)
        context['csrf_token'] = csrf_token

    # handle form post on view
    if request.method == 'POST':
        csrf_form = CsrfForm(request.POST)
        if csrf_form.is_valid():
            context['form_data'] = csrf_form.data

    return render(request, 'poc/csrf_protection.html', context)


def xss_protection(request):
    context = {}

    if request.method == 'GET':
        context['malicious_data'] = "<script>alert('You have been hacked!!!')</script>"

    if request.method == 'POST':
        xss_form = XssForm(request.POST)
        if xss_form.is_valid():
            context['form_data'] = xss_form.data

    return render(request, 'poc/xss_protection.html', context)
