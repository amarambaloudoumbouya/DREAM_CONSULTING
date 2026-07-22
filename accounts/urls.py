from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('connexion/', views.UserLoginView.as_view(), name='login'),
    path('deconnexion/', views.UserLogoutView.as_view(), name='logout'),
    path('utilisateurs/', views.users_list, name='users_list'),
    path('utilisateurs/ajouter/', views.user_create, name='user_create'),
    path('utilisateurs/<int:pk>/modifier/', views.user_update, name='user_update'),
    path('utilisateurs/<int:pk>/supprimer/', views.user_delete, name='user_delete'),
    path('membres/', views.membres_list, name='membres_list'),
    path('membres/ajouter/', views.membre_create, name='membre_create'),
    path('membres/<int:pk>/modifier/', views.membre_update, name='membre_update'),
    path('membres/<int:pk>/supprimer/', views.membre_delete, name='membre_delete'),
]
