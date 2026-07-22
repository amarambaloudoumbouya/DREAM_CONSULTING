from django.urls import path

from . import views

app_name = 'formation'

urlpatterns = [
    path('', views.formation_list, name='list'),
    path('inscription/', views.inscription_formation, name='inscription'),
    path('gestion/', views.admin_formation_list, name='admin_list'),
    path('gestion/ajouter/', views.admin_formation_create, name='admin_create'),
    path('gestion/<int:pk>/modifier/', views.admin_formation_update, name='admin_update'),
    path('gestion/<int:pk>/supprimer/', views.admin_formation_delete, name='admin_delete'),
    path('gestion/inscrits/', views.admin_inscription_list, name='admin_inscriptions'),
    path('gestion/inscrits/<int:pk>/statut/', views.admin_inscription_update_statut, name='admin_inscription_statut'),
]
