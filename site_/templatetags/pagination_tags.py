from django import template

register = template.Library()


def get_page_window(page_obj, size=5):
    """Fenêtre glissante de numéros de page autour de la page courante."""
    current = page_obj.number
    total = page_obj.paginator.num_pages
    if total <= size:
        return list(range(1, total + 1))

    half = size // 2
    start = max(1, current - half)
    end = min(total, start + size - 1)
    start = max(1, end - size + 1)
    return list(range(start, end + 1))


@register.inclusion_tag('includes/gallery_pagination.html')
def gallery_pagination(page_obj, query_extra='', css_class='gallery-pagination', label='Pagination'):
    return {
        'page_obj': page_obj,
        'page_numbers': get_page_window(page_obj, size=5),
        'query_extra': query_extra,
        'css_class': css_class,
        'label': label,
    }
