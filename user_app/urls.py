from django.urls import path
from .views import profile, list_items, add_items

app_name = 'user_app'

urlpatterns = [
    path('', profile, name='profile'),
    path('inventory', list_items, name='list_items'),
    path('add_items', add_items, name='add_items')
]