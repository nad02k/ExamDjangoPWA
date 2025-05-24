# backend/assets/views.py
from django.http import JsonResponse
from .models import OfflineAsset

def get_assets(request):
    # Return all cached assets as JSON
    assets = list(OfflineAsset.objects.values('id', 'url', 'hash'))
    return JsonResponse(assets, safe=False)