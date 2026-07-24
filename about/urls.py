from django.urls import path

from . import views

app_name = 'about'

urlpatterns = [
    path('gestion/', views.admin_about, name='admin_list'),
    path('gestion/section/', views.admin_section_update, name='admin_section_update'),
    path('gestion/panneaux/ajouter/', views.admin_accordion_create, name='admin_create'),
    path('gestion/panneaux/<int:pk>/modifier/', views.admin_accordion_update, name='admin_update'),
    path('gestion/panneaux/<int:pk>/supprimer/', views.admin_accordion_delete, name='admin_delete'),
    path('gestion/compteurs/ajouter/', views.admin_counter_create, name='counter_create'),
    path('gestion/compteurs/<int:pk>/modifier/', views.admin_counter_update, name='counter_update'),
    path('gestion/compteurs/<int:pk>/supprimer/', views.admin_counter_delete, name='counter_delete'),
    path('gestion/timeline/ajouter/', views.admin_timeline_create, name='timeline_create'),
    path('gestion/timeline/<int:pk>/modifier/', views.admin_timeline_update, name='timeline_update'),
    path('gestion/timeline/<int:pk>/supprimer/', views.admin_timeline_delete, name='timeline_delete'),
]
