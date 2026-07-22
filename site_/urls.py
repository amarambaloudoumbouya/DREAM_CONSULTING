from django.urls import path

from . import views

app_name = 'site_'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('photographie/', views.photographie, name='photographie'),
    path('video/', views.video, name='video'),
    path('branding/', views.branding, name='branding'),
    path('contact/', views.contact, name='contact'),
    path('a-propos/', views.apropos, name='apropos'),
    path('demande-avis/', views.demande_avis, name='demande_avis'),
    path('donner-avis/', views.donner_avis, name='donner_avis'),
]
