from django.contrib import admin
from .models import Leave, RemainingLeaves
# Register your models here.

admin.site.register(Leave)
admin.site.register(RemainingLeaves)
