from django.contrib import admin
from .models import Leave, RemainingLeaves, ApplicationRequest
# Register your models here.

admin.site.register(Leave)
admin.site.register(RemainingLeaves)
admin.site.register(ApplicationRequest)
