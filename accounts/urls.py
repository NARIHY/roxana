from django.urls import path
from . import views
from .views import UserListCreateAPIView, UserDetailAPIView

urlpatterns = [
    path('accounts/', UserListCreateAPIView.as_view(), name='accounts-list-create'),
    path('accounts/<int:pk>/', UserDetailAPIView.as_view(), name='account-detail'),
    path('roles/', views.RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleDetailAPIView.as_view(), name='role-detail'),
]
