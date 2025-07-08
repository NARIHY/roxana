# narix/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class AccueilAPIView(APIView):
    """
    Vue d'accueil qui renvoie toujours du JSON.
    """
    def get(self, request, format=None):
        _ = request  # Mark as used
        _ = format   # Mark as used
        data = {
            "message": "Bienvenue sur l'API !",
            "status": "OK"
        }
        return Response(data, status=status.HTTP_200_OK)

def custom_page_not_found(request, exception):
    """
    Vue personnalisée pour les 404 qui renvoie du JSON.
    """
    _ = exception  # Mark as used
    data = {
        "error": "Page non trouvée",
        "status": 404,
        "path": request.path,
    }
    return JsonResponse(data, status=404)