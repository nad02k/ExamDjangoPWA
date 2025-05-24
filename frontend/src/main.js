import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// Mount Vue app
const app = createApp(App)
app.use(store).use(router).mount('#app')

// Helper to convert Base64 URL-safe string to Uint8Array
function urlBase64ToUint8Array(base64String) {
  const padding = '='.repeat((4 - base64String.length % 4) % 4)
  const base64 = (base64String + padding)
    .replace(/-/g, '+')
    .replace(/_/g, '/')

  const rawData = window.atob(base64)
  const outputArray = new Uint8Array(rawData.length)

  for (let i = 0; i < rawData.length; ++i) {
    outputArray[i] = rawData.charCodeAt(i)
  }
  return outputArray
}

// Fetch VAPID public key from your Django backend
async function getVapidPublicKey() {
  const response = await fetch('http://localhost:8000/api/get_vapid_public_key/')
  const data = await response.json()
  return data.publicKey
}

// Subscribe user to push notifications
async function subscribeUserToPush() {
  if ('serviceWorker' in navigator && 'PushManager' in window) {
    try {
      const registration = await navigator.serviceWorker.ready
      const vapidPublicKey = await getVapidPublicKey()
      const convertedVapidKey = urlBase64ToUint8Array(vapidPublicKey)

      const subscription = await registration.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: convertedVapidKey
      })

      // Send subscription to your backend to save it
      await fetch('http://localhost:8000/api/save_subscribe/', {  // <-- ici
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(subscription)
      })

      console.log('User is subscribed:', subscription)
    } catch (error) {
      console.error('Failed to subscribe the user:', error)
    }
  } else {
    console.warn('Push messaging is not supported')
  }
}

// Register Service Worker and subscribe to push
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js')
    .then(reg => {
      console.log('Service Worker registered', reg)
      subscribeUserToPush()  // Call subscription after registration success
    })
    .catch(err => console.error('SW registration failed:', err))
}
