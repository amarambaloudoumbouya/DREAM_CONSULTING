from django.urls import path

from . import views

app_name = 'slider'

urlpatterns = [
    path('gestion/', views.admin_slider_list, name='admin_list'),
    path('gestion/ajouter/', views.admin_slider_create, name='admin_create'),
    path('gestion/<int:pk>/modifier/', views.admin_slider_update, name='admin_update'),
    path('gestion/<int:pk>/supprimer/', views.admin_slider_delete, name='admin_delete'),
]
