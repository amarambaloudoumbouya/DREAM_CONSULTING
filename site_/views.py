from django.shortcuts import render

from devis.views import demande_devis
from medias.models import Branding, Photographie, Video
from temoignage.views import donner_avis as temoignage_donner_avis


def dashboard(request):
    return render(request, 'backend/dashboard.html')


def index(request):
    return render(request, 'index.html')


def photographie(request):
    return render(request, 'pages/photographie.html', {
        'photographies': Photographie.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def video(request):
    return render(request, 'pages/video.html', {
        'videos': Video.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def branding(request):
    return render(request, 'pages/branding.html', {
        'brandings': Branding.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def contact(request):
    return render(request, 'pages/contact.html')


def apropos(request):
    return render(request, 'pages/apropos.html')


def demande_avis(request):
    return demande_devis(request)


def donner_avis(request):
    return temoignage_donner_avis(request)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
