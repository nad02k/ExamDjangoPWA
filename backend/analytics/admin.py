from django.contrib import admin
from .models import UsagePattern

@admin.register(UsagePattern)
class UsagePatternAdmin(admin.ModelAdmin):
    list_display = ('id', 'cluster_id', 'description', 'timestamp')
    list_filter = ('cluster_id',)
    search_fields = ('description',)
