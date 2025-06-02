
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pwa_project.settings')
django.setup()

import requests
import numpy as np
from sklearn.cluster import KMeans
from celery import shared_task
from analytics.models import UsagePattern
from django.utils import timezone

@shared_task
def precache_asset(url):
    try:
        response = requests.get(url)
        print(f"Cached {url} | Size: {len(response.content)}")
    except Exception as e:
        print(f"Failed to cache {url}: {e}")

@shared_task
def analyze_usage():
    data = np.array([[5.2], [12.3], [2.1], [9.4]])  # [[temps passé]]
    
    kmeans = KMeans(n_clusters=2).fit(data)
    labels = kmeans.labels_

    for i, label in enumerate(labels):
        UsagePattern.objects.create(
            cluster_id=label,
            description=f"User {i+1} belongs to cluster {label}"
        )

    print("Clusters trouvés:", labels)
    return {"clusters": labels.tolist()}