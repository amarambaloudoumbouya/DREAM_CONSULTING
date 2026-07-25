from django.shortcuts import render

from about.models import AboutAccordion, AboutCounter, AboutTimeline
from contact_us.views import contact_public
from devis.views import demande_devis
from medias.models import Branding, Photographie, Video, WebDesign
from temoignage.views import donner_avis as temoignage_donner_avis


def dashboard(request):
    return render(request, 'backend/dashboard.html')


def index(request):
    return render(request, 'index.html')


def photographie(request):
    photographies = Photographie.objects.filter(is_active=True).order_by('ordre', 'id')
    categories = []
    seen = set()
    for photo in photographies:
        slug = photo.categorie_slug
        if slug not in seen:
            seen.add(slug)
            categories.append({'name': photo.categorie, 'slug': slug})
    return render(request, 'pages/photographie.html', {
        'photographies': photographies,
        'photo_categories': categories,
    })


def video(request):
    return render(request, 'pages/video.html', {
        'videos': Video.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def branding(request):
    return render(request, 'pages/branding.html', {
        'brandings': Branding.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def web_design(request):
    return render(request, 'pages/web_design.html', {
        'web_designs': WebDesign.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def contact(request):
    return contact_public(request)


def apropos(request):
    notre_histoire = AboutAccordion.objects.filter(
        titre__iexact='Notre Histoire',
        is_active=True,
    ).first()
    return render(request, 'pages/apropos.html', {
        'notre_histoire': notre_histoire,
        'about_timelines': AboutTimeline.objects.filter(is_active=True).order_by('ordre', 'id'),
        'about_counters': AboutCounter.objects.filter(is_active=True).order_by('ordre', 'id'),
    })


def demande_avis(request):
    return demande_devis(request)


def donner_avis(request):
    return temoignage_donner_avis(request)


def page_not_found(request, exception):
    return render(request, '404.html', status=404)
