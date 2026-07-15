from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def photographie(request):
    return render(request, 'pages/photographie.html')


def video(request):
    return render(request, 'pages/video.html')


def branding(request):
    return render(request, 'pages/branding.html')


def contact(request):
    return render(request, 'pages/contact.html')


def apropos(request):
    return render(request, 'pages/apropos.html')


def demande_avis(request):
    return render(request, 'pages/demande_avis.html')
