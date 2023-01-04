from django.contrib import admin
from .models import playlist,song,list,user

# Register your models here.
admin.site.register(playlist)
admin.site.register(song)
admin.site.register(list)
admin.site.register(user)