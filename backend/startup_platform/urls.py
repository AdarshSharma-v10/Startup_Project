"""
URL configuration for startup_platform project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # Redirect root URL ('/') to your frontend URL
    path('', lambda request: redirect('https://your-frontend-domain.com/')),  # Replace with your actual frontend URL
    
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
