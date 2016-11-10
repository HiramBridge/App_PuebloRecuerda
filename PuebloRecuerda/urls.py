
# Librerias Django:
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('diputados.urls', namespace='diputados')),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^', include('seguridad.urls', namespace='seguridad')),
    url(r'^', include('leyes.urls', namespace='leyes')),
]

if settings.DEBUG:

    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)