from .models import CustomerUser


def equipe_membres(request):
    return {
        'equipe_membres': CustomerUser.objects.filter(
            role='membre',
            is_active=True,
        ).order_by('prenoms', 'nom'),
    }
