from django.urls import path

from users.views import registration

from . import views

app_name = 'users'

urlpatterns = [
    path('users/registration/', views.registration, name='registration'),
    path('users/login/', views.login_request, name='login'),
    path('users/logout/', views.logout_request, name='logout'),
    path('users/account/', views.account, name='account'),
    path('users/manage-account/', views.manage_account, name='manage_account'),
   
]