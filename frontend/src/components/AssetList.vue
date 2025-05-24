<template>
  <section class="asset-list">
    <h2>Cached Assets</h2>
    <ul v-if="assets.length">
      <li v-for="asset in assets" :key="asset.id" class="asset-card">
        <strong>{{ asset.url }}</strong>
        <small>Hash: {{ asset.hash.substring(0, 10) }}...</small>
      </li>
    </ul>
    <p v-else class="no-assets">No assets found. Click "Load Offline Assets".</p>
  </section>
</template>

<script>
export default {
  name: 'AssetList',
  props: {
    assets: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
.asset-card {
  background: white;
  padding: 1rem;
  margin-bottom: 0.8rem;
  border-left: 5px solid #42b983;
  list-style: none;
  border-radius: 6px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.05);
}

.asset-card strong {
  display: block;
  color: #2c3e50;
}

.no-assets {
  text-align: center;
  color: #999;
  font-style: italic;
}
</style>