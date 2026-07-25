from django.urls import path

from . import views

app_name = 'contact_us'

urlpatterns = [
    path('gestion/', views.admin_message_list, name='admin_list'),
    path('gestion/<int:pk>/repondre/', views.admin_message_reponse, name='admin_reponse'),
    path('gestion/<int:pk>/supprimer/', views.admin_message_delete, name='admin_delete'),
]
