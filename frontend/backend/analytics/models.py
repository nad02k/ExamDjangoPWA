# analytics/models.py
from django.db import models

class UsagePattern(models.Model):
    cluster_id = models.IntegerField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)