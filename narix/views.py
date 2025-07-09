from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .permissions import AllowAllIfDebug

class AccueilAPIView(APIView):
    """
    Vue d'accueil publique qui renvoie toujours du JSON.
    """
    permission_classes = []  # accessible sans authentification

    def get(self, request, format=None):
        data = {
            "message": "Bienvenue sur l'API !",
            "status": "OK"
        }
        return Response(data, status=status.HTTP_200_OK)


def custom_page_not_found(request, exception):
    """
    Vue personnalisée pour les 404 qui renvoie du JSON.
    """
    data = {
        "error": "Page non trouvée",
        "status": 404,
        "path": request.path,
    }
    return JsonResponse(data, status=status.HTTP_404_NOT_FOUND)



class MyView(generics.ListAPIView):
    permission_classes = [AllowAllIfDebug | IsAuthenticated]