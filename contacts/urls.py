from django.urls import path
from .views import contacts_list

urlpatterns = [
    path('', contacts_list, name='api_contacts'),
]
