from django.urls import path

from . import views

app_name = 'collaborateur'

urlpatterns = [
    path('gestion/', views.admin_collaborateur_list, name='admin_list'),
    path('gestion/ajouter/', views.admin_collaborateur_create, name='admin_create'),
    path('gestion/<int:pk>/modifier/', views.admin_collaborateur_update, name='admin_update'),
    path('gestion/<int:pk>/supprimer/', views.admin_collaborateur_delete, name='admin_delete'),
]
