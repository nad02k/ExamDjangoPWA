from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PushSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    endpoint = models.URLField()
    keys = models.JSONField()  # auth, p256dh
    created_at = models.DateTimeField(auto_now_add=True)