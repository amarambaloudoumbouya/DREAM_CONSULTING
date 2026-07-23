from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('gestion/', views.admin_about, name='admin_list'),
    path('gestion/section/', views.admin_section_update, name='admin_section_update'),
    path('gestion/panneaux/ajouter/', views.admin_accordion_create, name='admin_create'),
    path('gestion/panneaux/<int:pk>/modifier/', views.admin_accordion_update, name='admin_update'),
    path('gestion/panneaux/<int:pk>/supprimer/', views.admin_accordion_delete, name='admin_delete'),
]
