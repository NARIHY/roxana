from rest_framework import generics
from .models import Categorie, Materiel, Status
from .serializers import CategorieSerializer, MaterielSerializer, StatusSerializer
from rest_framework import viewsets

from .permissions import IsAdminRole
from .models import Categorie, Materiel, Status as MyModel
from .serializers import CategorieSerializer, MaterielSerializer, StatusSerializer as MySerializer
from rest_framework.permissions import IsAuthenticated


class CategorieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

class CategorieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    lookup_field = 'pk'

class MaterielListCreateAPIView(generics.ListCreateAPIView):
    queryset = Materiel.objects.all().order_by('-date_ajout')
    serializer_class = MaterielSerializer

class MaterielDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materiel.objects.all()
    serializer_class = MaterielSerializer
    lookup_field = 'uid'

class StatusListCreateAPIView(generics.ListCreateAPIView):
    queryset = Status.objects.all().order_by('nom')
    serializer_class = StatusSerializer

class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = 'id'


# For demonstration purposes, a protected viewset that requires admin permissions

class SomeProtectedViewSet(viewsets.ModelViewSet):
    """
    Exemple de ViewSet réservé aux admins.
    """
    queryset = MyModel.objects.all()
    serializer_class = MySerializer
    permission_classes = [IsAuthenticated, IsAdminRole]