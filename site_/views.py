from django.core.paginator import Paginator
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
    qs = Photographie.objects.filter(is_active=True).order_by('ordre', '-id')

    categories = []
    seen = set()
    for photo in qs:
        slug = photo.categorie_slug
        if slug not in seen:
            seen.add(slug)
            categories.append({'name': photo.categorie, 'slug': slug})

    selected_categorie = request.GET.get('categorie', '').strip()
    if selected_categorie:
        matching = [c['name'] for c in categories if c['slug'] == selected_categorie]
        if matching:
            qs = qs.filter(categorie=matching[0])
        else:
            selected_categorie = ''

    # Une carte = un lot de photos ajoutées ensemble (même groupe_id)
    albums = []
    groups = {}
    for photo in qs:
        key = str(photo.groupe_id)
        if key not in groups:
            album = {
                'groupe_id': key,
                'cover': photo,
                'photos': [],
                'categorie': photo.categorie,
                'categorie_slug': photo.categorie_slug,
                'titre': photo.titre_album,
            }
            groups[key] = album
            albums.append(album)
        groups[key]['photos'].append(photo)

    for album in albums:
        album['count'] = len(album['photos'])

    paginator = Paginator(albums, 9)
    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'pages/photographie.html', {
        'albums': page_obj,
        'page_obj': page_obj,
        'photo_categories': categories,
        'selected_categorie': selected_categorie,
        'pagination_query': f'categorie={selected_categorie}' if selected_categorie else '',
    })


def video(request):
    qs = Video.objects.filter(is_active=True).order_by('ordre', '-id')
    page_obj = Paginator(qs, 9).get_page(request.GET.get('page'))
    return render(request, 'pages/video.html', {
        'videos': page_obj,
        'page_obj': page_obj,
    })


def branding(request):
    qs = Branding.objects.filter(is_active=True).order_by('ordre', '-id')
    page_obj = Paginator(qs, 9).get_page(request.GET.get('page'))
    return render(request, 'pages/branding.html', {
        'brandings': page_obj,
        'page_obj': page_obj,
    })


def web_design(request):
    qs = WebDesign.objects.filter(is_active=True).order_by('ordre', 'id')
    page_obj = Paginator(qs, 9).get_page(request.GET.get('page'))
    return render(request, 'pages/web_design.html', {
        'web_designs': page_obj,
        'page_obj': page_obj,
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
