"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_.urls')),
    path('accounts/', include('accounts.urls')),
    path('formations/', include('formation.urls')),
    path('devis/', include('devis.urls')),
    path('partenaires/', include('partenaire.urls')),
    path('temoignages/', include('temoignage.urls')),
    path('collaborateurs/', include('collaborateur.urls')),
]

# Important: django.conf.urls.static.static() ne fait RIEN si DEBUG=False.
# Sur Passenger / cPanel, Django doit servir CSS/JS/images lui-même.
_static_dir = (
    settings.STATICFILES_DIRS[0]
    if getattr(settings, 'STATICFILES_DIRS', None)
    else settings.STATIC_ROOT
)
urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': str(_static_dir)}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': str(settings.MEDIA_ROOT)}),
]

handler404 = 'site_.views.page_not_found'
