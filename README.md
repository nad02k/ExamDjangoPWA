# 📦 Offline Asset Manager PWA

A Progressive Web App (PWA) that caches assets for offline use, analyzes user behavior with AI, and sends push notifications using Celery and Redis.

---

## 🔧 Features

- ✅ Django backend with offline asset caching
- ✅ Vue.js frontend with install prompt and service worker
- ✅ Background jobs powered by Celery + Redis
- ✅ AI-based usage analytics (KMeans clustering)
- ✅ GraphQL API for querying cached assets
- ✅ REST endpoints for asset management
- ✅ Push notifications via VAPID key

---

## 📋 Requirements

Make sure you have Python 3.10+ and Node.js installed.

### Backend (Django)

```bash
pip install django djangorestframework celery redis scikit-learn billiard graphene-django django-cors-headers