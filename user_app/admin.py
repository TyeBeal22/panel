from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUseradmin
from django.contrib import admin
from .models import CustomUserProfile, Stock
from .forms import StockCreateForm
# Register your models here.

# admin.site.register(CustomUserProfile)

@admin.register(CustomUserProfile)
class CustomUserdmin(BaseUseradmin):
    """ Custom user admin display."""

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal Information'), {'fields' :('email', 'first_name', 'last_name')}),
        (_('Additiona Information'), {'fields': ('date_of_birth', 'gender', 'country', 'occupation',
            'phone_number', 'photo')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2',)
        }),
    )

    ordering = ['email', 'first_name', 'last_name']
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    list_filters = ['email', 'first_name', 'last_name']
    filter_horizontal = ['groups', 'user_permissions']




class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateAdmin)