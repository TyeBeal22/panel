from .models import Setting
from django.shortcuts import get_object_or_404


# get the settings model
def get_settings(model):
    settings = get_object_or_404(model, pk=1)

    return settings


def setting(request):
    """ the context processor function."""

    config = get_settings(Setting)

    return {
    'config': config,
    'request': request,
    }
