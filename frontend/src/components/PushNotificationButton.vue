<template>
  <button @click="subscribeToPush" class="btn notify-btn">🔔 Enable Push Notifications</button>
</template>

<script>
export default {
  name: 'PushNotificationButton',
  methods: {
    async subscribeToPush() {
      if (!('serviceWorker' in navigator)) {
        alert("Service workers are not supported.");
        return;
      }

      const registration = await navigator.serviceWorker.ready;

      const existingSubscription = await registration.pushManager.getSubscription();
      if (existingSubscription) {
        alert("Already subscribed!");
        return;
      }

      try {
        const response = await fetch('http://localhost:8000/api/vapid-public-key/');
        const { key } = await response.json();

        const convertedKey = this.urlBase64ToUint8Array(key);

        const subscription = await registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey: convertedKey
        });

        const res = await fetch('http://localhost:8000/api/subscribe/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(subscription),
          credentials: 'include'
        });

        const result = await res.json();
        console.log("Subscription saved:", result);
        alert("✅ Subscribed to push notifications!");

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