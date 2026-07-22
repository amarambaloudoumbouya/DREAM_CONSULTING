from .models import Temoignage


def temoignages_publies(request):
    return {
        'temoignages': Temoignage.objects.filter(statut='publie').order_by('-publie_at', '-created_at'),
    }
