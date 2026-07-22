from .models import Collaborateur


def collaborateurs_actifs(request):
    return {
        'collaborateurs': Collaborateur.objects.filter(is_active=True).order_by('ordre', 'titre'),
    }
