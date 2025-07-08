from django.urls import path
from . import views

urlpatterns = [
    path('', views.users_list, name='accounts-list'),
    path('detail/<int:id>/', views.user_detail, name='accounts-detail'),
]
