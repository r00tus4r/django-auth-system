from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('profile/<int:id>/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('update/', views.update_profile_view, name='update-profile'),
    path('delete/', views.delete_account_view, name='delete-account'),
]
