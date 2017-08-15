from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^getapplications', views.get_applications, name='get_applications'),
    url(r'^apply', views.main_interface, name='main_interface'),
]
