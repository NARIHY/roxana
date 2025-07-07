from django.urls import path
from .views import CategorieListCreateAPIView, MaterielListCreateAPIView, MaterielDetailAPIView

urlpatterns = [
    path('categories/', CategorieListCreateAPIView.as_view(), name='categories'),
    path('materiels/', MaterielListCreateAPIView.as_view(), name='materiels'),
    path('materiels/<uuid:uid>/', MaterielDetailAPIView.as_view(), name='materiel-detail'),
]
