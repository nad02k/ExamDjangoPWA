<template>
  <div id="app">
    <!-- Header -->
    <header class="app-header">
      <h1>📚 Offline Asset Manager</h1>
      <p>Your Progressive Web App is Ready!</p>
    </header>

    <!-- Main Content -->
    <main class="app-content">
      <!-- Action Buttons -->
      <div class="action-buttons">
        <button v-if="showInstallPrompt" @click="installPWA" class="btn install-btn">📥 Install App</button>
        <button @click="fetchAssets" class="btn fetch-btn">📦 Load Offline Assets</button>
        <button @click="subscribeToPush" class="btn notify-btn">🔔 Enable Push Notifications</button>
      </div>

      <!-- Asset List -->
      <section class="asset-list">
        <h2>Cached Assets</h2>
        <ul v-if="assets.length">
          <li v-for="asset in assets" :key="asset.id" class="asset-card">
            <strong>{{ asset.url }}</strong>
            <small>Hash: {{ asset.hash.substring(0, 10) }}...</small>
          </li>
        </ul>
        <p v-else class="no-assets">No assets found. Click "Load Offline Assets"</p>
      </section>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      assets: [],
      showInstallPrompt: false,
      deferredPrompt: null
    };
  },
  mounted() {
    // Register Service Worker
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/service-worker.js')
        .then(reg => console.log('Service Worker registered', reg))
        .catch(err => console.error('SW registration failed:', err));
    }

    // Detect PWA install prompt
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      this.deferredPrompt = e;
      this.showInstallPrompt = true;
    });
  },
  methods: {
    // Trigger PWA Install Prompt
    installPWA() {
      if (this.deferredPrompt) {
        this.deferredPrompt.prompt();
        this.deferredPrompt.userChoice.then((choice) => {
          if (choice.outcome === 'accepted') {
            console.log('User accepted the install prompt.');
          }
          this.deferredPrompt = null;
          this.showInstallPrompt = false;
        });
      }
    },

    // Fetch cached assets from Django REST API
    async fetchAssets() {
      try {
        const response = await fetch('http://localhost:8000/api/assets/');
        const data = await response.json();
        this.assets = data;
      } catch (error) {
        alert("Failed to load assets. Is Django running?");
        console.error(error);
      }
    },

    // Helper: Convert Base64URL string to Uint8Array
    urlBase64ToUint8Array(base64String) {
      const padding = '='.repeat((4 - base64String.length % 4) % 4);
      const base64 = (base64String + padding)
        .replace(/-/g, '+')
        .replace(/_/g, '/');

      const rawData = window.atob(base64);
      const outputArray = new Uint8Array(rawData.length);

      for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
      }

      return outputArray;
    },

    // Subscribe to Push Notifications
    async subscribeToPush() {
      if (!('serviceWorker' in navigator)) {
        alert("Service workers not supported.");
        return;
      }

      const registration = await navigator.serviceWorker.ready;

      const existingSubscription = await registration.pushManager.getSubscription();
      if (existingSubscription) {
        alert("Already subscribed!");
        return;
      }

      try {
        const response = await fetch('http://localhost:8000/api/get_vapid_public_key/');
        if (!response.ok) throw new Error("Failed to load VAPID key");

        const { publicKey } = await response.json();

        const convertedKey = this.urlBase64ToUint8Array(publicKey);

        const subscription = await registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: convertedKey
        });

        // Send to backend
        const res = await fetch('http://localhost:8000/api/save_subscribe/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(subscription),
          credentials: 'include'
        });

        const result = await res.json();
        console.log("Subscription saved:", result);
        alert("✅ You're now subscribed to push notifications!");

      } catch (err) {
        console.error("Subscription failed:", err);
        alert("❌ Failed to subscribe. Check console for details.");
      }
    }
  }
};
</script>

<style>
/* Global styles */
:root {
  --primary-color: #42b983;
  --secondary-color: #2c3e50;
  --bg-color: #f5f5f5;
  --card-bg: white;
  --text-color: #333;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--bg-color);
}

#app {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.app-header {
  text-align: center;
  padding: 2rem 1rem;
  background: linear-gradient(to right, #2c3e50, #34495e);
  color: white;
  border-radius: 10px;
  margin-bottom: 2rem;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.app-header h1 {
  margin: 0;
  font-size: 2rem;
}

.app-header p {
  margin-top: 0.5rem;
  font-weight: 300;
}

.action-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.btn {
  padding: 12px 20px;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.install-btn {
  background-color: #3498db;
  color: white;
}

.fetch-btn {
  background-color: #2ecc71;
  color: white;
}

.notify-btn {
  background-color: #e67e22;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}

.asset-list {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.asset-list h2 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: var(--secondary-color);
}

.asset-card {
  background: var(--card-bg);
  padding: 1rem;
  margin-bottom: 0.8rem;
  border-left: 5px solid var(--primary-color);
  list-style: none;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.asset-card strong {
  display: block;
  color: var(--secondary-color);
}

.asset-card small {
  display: block;
  color: #888;
  margin-top: 0.4rem;
}

.no-assets {
  text-align: center;
  color: #999;
  font-style: italic;
}
</style>
