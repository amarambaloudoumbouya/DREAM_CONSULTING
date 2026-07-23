from .models import Slider


def sliders_actifs(request):
    return {
        'sliders': Slider.objects.filter(is_active=True).order_by('ordre', 'id'),
    }
