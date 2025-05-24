from django.contrib import admin
from .models import UsagePattern

@admin.register(UsagePattern)
class UsagePatternAdmin(admin.ModelAdmin):
    list_display = ('cluster_id', 'timestamp')
    readonly_fields = ('cluster_id', 'description', 'timestamp')