from .models import Partenaire


def partenaires_actifs(request):
    return {
        'partenaires': Partenaire.objects.filter(is_active=True).order_by('ordre', 'nom'),
    }
