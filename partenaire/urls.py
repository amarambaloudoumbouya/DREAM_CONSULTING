from django.urls import path

from . import views

app_name = 'partenaire'

urlpatterns = [
    path('gestion/', views.admin_partenaire_list, name='admin_list'),
    path('gestion/ajouter/', views.admin_partenaire_create, name='admin_create'),
    path('gestion/<int:pk>/modifier/', views.admin_partenaire_update, name='admin_update'),
    path('gestion/<int:pk>/supprimer/', views.admin_partenaire_delete, name='admin_delete'),
]
