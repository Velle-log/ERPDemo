from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^getapplications', views.get_applications, name='get_applications'),
    url(r'^getleaves', views.get_leaves, name='get_leaves'),
    url(r'^apply', views.main_interface, name='main_interface'),
    url(r'^process_request/(?P<id>[0-9]+)/', views.process_request, name='process_request'),
    url(r'^notifications/', views.notifications, name='notifications'),
    # url(r'^approve/(?P<id>[0-9]+)/$', views.approve_application, name='approve_application'),
    # url(r'^reject/(?P<id>[0-9]+)/$', views.reject_application, name='reject_application'),
    # url(r'^forward/(?P<id>[0-9]+)/$', views.forward_application, name='forward_application'),

]
