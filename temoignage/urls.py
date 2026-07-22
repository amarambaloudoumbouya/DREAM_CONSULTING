from django.urls import path

from . import views

app_name = 'temoignage'

urlpatterns = [
    path('gestion/', views.admin_temoignage_list, name='admin_list'),
    path('gestion/<int:pk>/modifier/', views.admin_temoignage_update, name='admin_update'),
    path('gestion/<int:pk>/publier/', views.admin_temoignage_publier, name='admin_publier'),
    path('gestion/<int:pk>/refuser/', views.admin_temoignage_refuser, name='admin_refuser'),
    path('gestion/<int:pk>/supprimer/', views.admin_temoignage_delete, name='admin_delete'),
]
