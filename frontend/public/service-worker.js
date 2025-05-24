const CACHE_NAME = 'offline-asset-cache-v1';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/css/app.css',
  '/js/app.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(ASSETS_TO_CACHE);
    })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => {
      return response || fetch(event.request);
    })
  );
});

// 🔔 Handle push events
self.addEventListener('push', event => {
  const data = event.data.json();
  const title = data.title || 'New Message';
  const options = {
    body: data.body,
    icon: '/img/icons/icon-192x192.png',
    badge: '/img/badge.png',
    vibrate: [100, 50, 100],
    data: { url: data.url || '/' }
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});