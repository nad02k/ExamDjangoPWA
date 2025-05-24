<template>
  <button @click="subscribeToPush" class="btn notify-btn">🔔 Enable Push Notifications</button>
</template>

<script>
export default {
  name: 'PushNotificationButton',
  methods: {
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
        const response = await fetch('http://127.0.0.1:8000/api/vapid-public-key/');
        if (!response.ok) throw new Error("Failed to load VAPID key");

        const { key } = await response.json();
        const convertedKey = this.urlBase64ToUint8Array(key);

        const subscription = await registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: convertedKey
        });

        console.log("Subscription created:", subscription);

        const res = await fetch('http://127.0.0.1:8000/api/subscribe/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(subscription)
        });

        const result = await res.json();
        console.log("Subscription saved:", result);
        alert("✅ You're now subscribed to push notifications!");

      } catch (err) {
        console.error("Subscription failed:", err);
        alert("❌ Failed to subscribe. Check console for details.");
      }
    },

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
    }
  }
};
</script>

<style scoped>
.notify-btn {
  background-color: #e67e22;
  color: white;
  padding: 12px 20px;
  border-radius: 8px;
  font-weight: bold;
  border: none;
  cursor: pointer;
}
.notify-btn:hover {
  opacity: 0.9;
}
</style>