from rest_framework import generics
from .models import Categorie, Materiel
from .serializers import CategorieSerializer, MaterielSerializer

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
