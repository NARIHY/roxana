from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserListCreateAPIView, UserDetailAPIView,LogoutAndBlacklistRefreshTokenAPIView, ForgotPasswordAPIView

urlpatterns = [
    path('accounts/', UserListCreateAPIView.as_view(), name='accounts-list-create'),
    path('accounts/<int:pk>/', UserDetailAPIView.as_view(), name='account-detail'),
    path('roles/', views.RoleListCreateAPIView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', views.RoleDetailAPIView.as_view(), name='role-detail'),

    # Authentication URLs
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutAndBlacklistRefreshTokenAPIView.as_view(), name='auth_logout'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='auth_forgot_password'),
]
