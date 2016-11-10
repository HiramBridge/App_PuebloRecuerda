# -*- coding: utf-8 -*-

# Librerias Django:
from django.conf.urls import url

# Vistas Home
from .views import Index


urlpatterns = [
    url(r'^$',Index.as_view(),name='home.index'),
]
