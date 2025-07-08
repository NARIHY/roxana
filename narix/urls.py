"""
URL configuration for narix project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.apps import apps
from .views import AccueilAPIView  # Make sure AccueilAPIView is defined in narix/views.py

# URL patterns for the API
# This includes the URLs for the contacts, stocks, and accounts apps,
# Dynamically include URLs for each installed app that has a urls.py
api_patterns = []
resources = ['contacts', 'stocks', 'accounts']
for resource in resources:
    if apps.is_installed(resource):
        api_patterns.append(path(f'{resource}/', include(f'{resource}.urls')))

# Main URL patterns for the project
# This includes the API patterns and the admin interface.
urlpatterns = [
    path('', AccueilAPIView.as_view(), name='accueil'),
    path('admin/', admin.site.urls),
    path('api/', include((api_patterns, 'api'))),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # ← nécessaire pour Swagger
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# En bas du fichier, après urlpatterns :
handler404 = 'narix.views.custom_page_not_found'