from rest_framework import serializers
from .models import UsagePattern

class UsagePatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsagePattern
        fields = ['cluster_id', 'description', 'timestamp']