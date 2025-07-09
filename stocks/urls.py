from django.urls import path
from .views import CategorieListCreateAPIView, MaterielListCreateAPIView, MaterielDetailAPIView,StatusListCreateAPIView, StatusDetailAPIView

urlpatterns = [
    path('categories/', CategorieListCreateAPIView.as_view(), name='categories'),
    path('materiels/', MaterielListCreateAPIView.as_view(), name='materiels'),
    path('materiels/<uuid:uid>/', MaterielDetailAPIView.as_view(), name='materiel-detail'),
    path('status/', StatusListCreateAPIView.as_view(), name='status-list-create'),
    path('status/<int:id>/', StatusDetailAPIView.as_view(), name='status-detail'),
]
