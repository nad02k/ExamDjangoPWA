<template>
  <div id="app" class="app-container">
    <!-- Header -->
    <header class="app-header" role="banner">
      <h1>📚 Offline Asset Manager</h1>
      <p>Welcome to our Progressive Web Application !</p>
    </header>

    <!-- Main Content -->
    <main class="app-content" role="main">
      <!-- Action Buttons -->
      <div class="action-buttons">
        <button v-if="showInstallPrompt" @click="installPWA" class="btn install-btn">📥 Install App</button>
        <button @click="fetchAssets" class="btn fetch-btn">📦 Load Cached Assets</button>
        <PushNotificationButton />
      </div>

      <!-- Loading Spinner -->
      <div v-if="loading" class="spinner">🔄 Loading assets...</div>

      <!-- Asset List -->
      <AssetList :assets="assets" />

      <!-- Footer -->
      <footer class="app-footer" role="contentinfo">
        <p>&copy; 2025 Offline Asset Manager</p>
      </footer>
    </main>
  </div>
</template>

<script>
import AssetList from './components/AssetList.vue';
import PushNotificationButton from './components/PushNotificationButton.vue';

export default {
  name: 'App',
  components: {
    AssetList,
    PushNotificationButton
  },
  data() {
    return {
      assets: [],
      showInstallPrompt: false,
      deferredPrompt: null,
      loading: false
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
            console.log("User accepted the install prompt.");
          }
          this.deferredPrompt = null;
          this.showInstallPrompt = false;
        });
      }
    },

    // Fetch cached assets from Django REST API
    async fetchAssets() {
      this.loading = true;
      try {
        const response = await fetch('http://localhost:8000/api/assets/');
        const data = await response.json();
        this.assets = data;
      } catch (error) {
        alert("❌ Failed to load assets. Is Django running?");
        console.error(error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>
<style>
/* Global styles */
:root {
  --primary-color: #4f46e5;     /* Indigo */
  --secondary-color: #7c3aed;   /* Violet */
  --accent-color: #ec4899;     /* Hot pink */
  --bg-color: #f9f9fb;
  --card-bg: #ffffff;
  --text-color: #111827;
  --shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Poppins', sans-serif;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
  line-height: 1.6;
}

#app {
  max-width: 900px;
  margin: auto;
  padding: 2rem;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background: white;
  border-radius: 12px;
  box-shadow: var(--shadow);
  transition: all 0.3s ease;
}

.app-container {
  padding: 2rem;
  background: linear-gradient(to bottom right, #f3f4f6, #ffffff);
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

/* Header */
.app-header {
  text-align: center;
  padding: 2.5rem 1.5rem;
  background: linear-gradient(to right, #7c3aed, #ec4899);
  color: white;
  border-radius: 10px;
  margin-bottom: 2rem;
  box-shadow: var(--shadow);
}

.app-header h1 {
  font-size: 2.2rem;
  margin-bottom: 0.5rem;
}

.app-header p {
  font-weight: 300;
  opacity: 0.9;
}

/* Buttons */
.action-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.btn {
  padding: 14px 20px;
  font-size: 1rem;
  font-weight: bold;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: var(--shadow);
  text-align: center;
}

.install-btn {
  background: var(--secondary-color);
  color: white;
}

.fetch-btn {
  background: var(--primary-color);
  color: white;
}

.notify-btn {
  background: var(--accent-color);
  color: white;
}

.btn:hover {
  transform: translateY(-3px);
  opacity: 0.9;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Spinner */
.spinner {
  text-align: center;
  color: var(--accent-color);
  font-weight: bold;
  margin-bottom: 1rem;
}

/* Footer */
.app-footer {
  text-align: center;
  margin-top: auto;
  padding: 1.5rem 0 0 0;
  font-size: 0.9rem;
  color: #6b7280;
}
</style>