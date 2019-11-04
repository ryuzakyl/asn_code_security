from django.shortcuts import render


def example1(request):
    return render(request, 'poc/example1.html')
