from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('user_profile.urls', namespace='user_profile')),
    url(r'^leave/', include('leaveapplication.urls', namespace='leaveapplication')),
    url(r'^accounts/', include('allauth.urls')),
]
