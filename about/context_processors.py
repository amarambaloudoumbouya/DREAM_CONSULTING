from .models import AboutAccordion, AboutSection


def about_section(request):
    section = AboutSection.objects.filter(pk=1, is_active=True).first()
    panels = AboutAccordion.objects.filter(is_active=True).order_by('ordre', 'titre')
    return {
        'about_section': section,
        'about_panels': panels,
    }
