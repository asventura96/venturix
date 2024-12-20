# accounts/urls.py

from django.urls import path
from .views import login_view, CustomPasswordResetView, UserListView, UserUpdateView, app_list_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/edit/', UserUpdateView.as_view(), name='user_edit'),
    path('apps/', app_list_view, name='app_list'),
]
