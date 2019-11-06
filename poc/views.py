from django.shortcuts import render
from django.middleware import csrf

from .forms import CsrfForm, XssForm, RenewBookForm


def form_validation(request):
    # get form instance
    form = RenewBookForm(request.POST or None, request.FILES or None)

    # set context for templates
    context = {'form': form}

    # handle POST request
    if request.method == 'POST':
        if form.is_valid():
            return render(request, 'poc/form_posted.html', context)

    return render(request, 'poc/form_validation.html', context)


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
