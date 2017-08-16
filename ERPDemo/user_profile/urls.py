from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home/', views.index, name='index'),
    url(r'^profile/(?P<username>[a-zA-Z\.0-9]{3,30})/$', views.profile, name='profile'),
]
