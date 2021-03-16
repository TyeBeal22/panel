

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index
from home import views

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', include('home.urls',  namespace='home')),
    path('user/', include('user_app.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)