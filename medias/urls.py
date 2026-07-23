from django.urls import path

from . import views

app_name = 'medias'

urlpatterns = [
    # Photographies
    path('photographies/', views.admin_photographie_list, name='photographie_list'),
    path('photographies/ajouter/', views.admin_photographie_create, name='photographie_create'),
    path('photographies/<int:pk>/modifier/', views.admin_photographie_update, name='photographie_update'),
    path('photographies/<int:pk>/supprimer/', views.admin_photographie_delete, name='photographie_delete'),
    # Branding
    path('branding/', views.admin_branding_list, name='branding_list'),
    path('branding/ajouter/', views.admin_branding_create, name='branding_create'),
    path('branding/<int:pk>/modifier/', views.admin_branding_update, name='branding_update'),
    path('branding/<int:pk>/supprimer/', views.admin_branding_delete, name='branding_delete'),
    # Vidéos
    path('videos/', views.admin_video_list, name='video_list'),
    path('videos/ajouter/', views.admin_video_create, name='video_create'),
    path('videos/<int:pk>/modifier/', views.admin_video_update, name='video_update'),
    path('videos/<int:pk>/supprimer/', views.admin_video_delete, name='video_delete'),
]
