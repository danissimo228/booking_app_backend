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
    path(
        'set-user-attr/', views.UsersModelViewSet.as_view({"patch": "set_user_attr"}), name='set profile'
    ),
    path(
        'upload-photo/', views.UsersModelViewSet.as_view({"post": "upload_photo"}), name='upload photo'
    ),
    path(
        'delete-photo/', views.UsersModelViewSet.as_view({"delete": "delete_photo"}), name='delete photo'
    ),
    path(
        'get-photo/', views.UsersModelViewSet.as_view({"get": "get_photo"}), name='get photo'
    ),
]
