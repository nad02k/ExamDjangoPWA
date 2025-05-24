<template>
  <section class="asset-list" aria-labelledby="assets-title">
    <h2 id="assets-title">Cached Assets</h2>
    <ul v-if="assets.length" class="asset-grid">
      <li v-for="asset in assets" :key="asset.id" class="asset-card" role="listitem">
        <strong>{{ asset.url }}</strong>
        <small>Hash: {{ asset.hash.substring(0, 10) }}...</small>
      </li>
    </ul>
    <p v-else class="no-assets">No assets found. Click "Load Cached Assets"</p>
  </section>
</template>

<script>
export default {
  props: ['assets']
};
</script>

<style scoped>
.asset-list {
  background: var(--card-bg);
  padding: 1.5rem;
  border-radius: 10px;
  box-shadow: var(--shadow);
  transition: all 0.3s ease;
}

.asset-list h2 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: var(--secondary-color);
}

.asset-grid {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.asset-card {
  background: #fafafa;
  padding: 1rem;
  border-left: 5px solid var(--primary-color);
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s ease;
}

.asset-card:hover {
  transform: scale(1.01);
}

.asset-card strong {
  display: block;
  color: var(--text-color);
  font-size: 1rem;
}

.asset-card small {
  display: block;
  color: #6b7280;
  margin-top: 0.4rem;
  font-size: 0.85rem;
}

.no-assets {
  text-align: center;
  color: #9ca3af;
  font-style: italic;
}
</style>