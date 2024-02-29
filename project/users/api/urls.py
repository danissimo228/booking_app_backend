from django.urls import path
from project.users.api import views

urlpatterns = [
    path(
        'register/', views.UsersModelViewSet.as_view({"post": "create_user"}), name='create'
    ),
    path(
        'recover-password/', views.UsersModelViewSet.as_view({"post": "recover"}), name='recover'
    ),
    path(
        'change-password/', views.UsersModelViewSet.as_view({"patch": "change_password"}), name='change password'
    ),
    path(
        'get-user-profile/', views.UsersModelViewSet.as_view({"get": "get_user_profile"}), name='profile'
    ),
]
