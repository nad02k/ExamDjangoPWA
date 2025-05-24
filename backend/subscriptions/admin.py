from django.contrib import admin
from .models import PushSubscription

@admin.register(PushSubscription)
class PushSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'created_at')