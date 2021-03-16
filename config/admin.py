from django.contrib import admin
from .models import Setting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']

admin.site.register(Setting, SettingAdmin)