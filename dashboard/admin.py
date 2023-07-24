from django.contrib import admin
from .models import resource
from django.contrib.auth.models import Group
admin.site.site_header='kasage adminstration'

class resourceAdmin(admin.ModelAdmin):
    list_display = ('formation', 'langue', 'description', 'liens')
# Register your models here.
admin.site.register(resource,resourceAdmin)
# admin.site.unregister(Group)