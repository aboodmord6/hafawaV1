
//HI am new

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [
    '/offline/',
    '/static/css/django-pwa-app.css',
    "/static/app/android/android-launchericon-512-512.png",
    "/static/app/android/android-launchericon-192-192.png",
    "/static/app/android/android-launchericon-144-144.png",
    "/static/app/android/android-launchericon-96-96.png",
    "/static/app/android/android-launchericon-72-72.png",
    "/static/app/android/android-launchericon-48-48.png",
    "/static/app/ios/16.png",
    "/static/app/ios/20.png",
    "/static/app/ios/29.png",
    "/static/app/ios/32.png",
    "/static/app/ios/40.png",
    "/static/app/ios/50.png",
    "/static/app/ios/57.png",
    "/static/app/ios/58.png",
    "/static/app/ios/60.png",
    "/static/app/ios/64.png",
    "/static/app/ios/72.png",
    "/static/app/ios/76.png",
    "/static/app/ios/80.png",
    "/static/app/ios/87.png",
    "/static/app/ios/100.png",
    "/static/app/ios/114.png",
    "/static/app/ios/120.png",
    "/static/app/ios/128.png",
    "/static/app/ios/144.png",
    "/static/app/ios/152.png",
    "/static/app/ios/167.png",
    "/static/app/ios/180.png",
    "/static/app/ios/192.png",
    "/static/app/ios/256.png",
    "/static/app/ios/512.png",
    "/static/app/ios/1024.png",
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});