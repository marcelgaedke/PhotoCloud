from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('' ,views.welcome, name='welcome'),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^upload/(?P<album_id>(\d+))/$', views.upload, name='upload'),
    url(r'^album/(?P<album_id>(\d+))/$', views.album, name='album'),
    path('start/', views.start, name='start'),
    path('create_album/', views.create_album, name='create_album'),
]