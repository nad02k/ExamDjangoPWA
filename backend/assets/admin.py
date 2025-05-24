from django.contrib import admin
from .models import OfflineAsset

@admin.register(OfflineAsset)
class OfflineAssetAdmin(admin.ModelAdmin):
    list_display = ('url', 'hash', 'size', 'last_cached')
    search_fields = ('url',)
    readonly_fields = ('hash', 'last_cached')