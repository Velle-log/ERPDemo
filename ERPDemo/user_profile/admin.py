from django.contrib import admin

from .models import Designation, Designated, ExtraInfo

# Register your models here.
admin.site.register(Designation)
admin.site.register(Designated)
admin.site.register(ExtraInfo)
