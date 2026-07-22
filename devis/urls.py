from django.urls import path

from . import views

app_name = 'devis'

urlpatterns = [
    path('gestion/', views.admin_demande_list, name='admin_list'),
    path('gestion/<int:pk>/retour/', views.admin_demande_retour, name='admin_retour'),
]
