
const CACHE_NAME = 'offline-cache-v2';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/css/app.css',
  '/js/chunk-vendors.js',
  '/img/icons/icon-192x192.png',
  '/img/badge.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(ASSETS_TO_CACHE)
  ));
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request).then(response => response || fetch(event.request))
  );
});

// Handle push notifications
self.addEventListener('push', event => {
  const data = event.data.json();
  self.registration.showNotification(data.title || 'Nouvelle notification', {
    body: data.body || 'Vous avez un nouveau message.',
    icon: '/img/icons/icon-192x192.png',
    badge: '/img/badge.png',
    vibrate: [100, 50, 100],
    data: { url: data.url || '/' }
  });
});