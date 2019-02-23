from django.shortcuts import render


def get_company(request):
    return render(request, 'etc/company.html')


def get_guide(request):
    return render(request, 'etc/guide.html')


def get_term(request):
    return render(request, 'etc/term.html')


def get_privacy(request):
    return render(request, 'etc/privacy.html')
