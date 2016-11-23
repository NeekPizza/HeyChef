from django.conf.urls import url
from . import views

#models--views--templates

urlpatterns = [
    url(r'^$', views.index),
    url(r'^recipes$',views.recipes),
    url(r'^details/(?P<uri>.+)$',views.details),
]
