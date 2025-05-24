from django.db import models
import hashlib

def generate_hash(url):
    return hashlib.sha256(url.encode()).hexdigest()

class OfflineAsset(models.Model):
    url = models.URLField(unique=True)
    hash = models.CharField(max_length=64, blank=True)
    size = models.PositiveIntegerField(default=0)
    last_cached = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.hash:
            self.hash = generate_hash(self.url)
        super().save(*args, **kwargs)