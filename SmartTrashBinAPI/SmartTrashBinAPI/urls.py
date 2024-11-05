from django.contrib import admin
from django.urls import path, include
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include(oauth2_urls, namespace='oauth2_provider')),
    path('api/', include('trash.urls')),
    path('user/', include('user.urls')),
]
