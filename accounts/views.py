from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from stocks import serializers
from .models import CustomUser, Role
from .serializers import CustomUserSerializer, RoleSerializer
from rest_framework import generics


# REST AUTENTICATION
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from .permissions import IsAdminOrReadOnly


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class RoleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all().order_by('name')
    serializer_class = RoleSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

class RoleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]



# Logout and blacklist refresh token
class LogoutAndBlacklistRefreshTokenAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class ForgotPasswordAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({'detail': 'Email inconnu.'}, status=status.HTTP_400_BAD_REQUEST)

        token = PasswordResetTokenGenerator().make_token(user)
        reset_link = f"https://votre-frontend/reset-password?uid={user.pk}&token={token}"
        # send_mail(...)
        # Envoyer le lien à l'utilisateur
        
        return Response({'detail': 'Email de réinitialisation envoyé.'}, status=status.HTTP_200_OK)