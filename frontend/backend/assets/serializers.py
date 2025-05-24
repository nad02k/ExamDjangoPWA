from rest_framework import serializers
from .models import OfflineAsset

class OfflineAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfflineAsset
        fields = ['id', 'url', 'hash', 'size', 'last_cached']

    def validate_url(self, value):
        if "example.com" not in value:
            raise serializers.ValidationError("Only example.com assets allowed")
        return value