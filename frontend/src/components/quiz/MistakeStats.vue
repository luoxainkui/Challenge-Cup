<template>
  <div class="mistake-stats">
    <div class="stat-item">
      <div class="stat-num">{{ mistakeCount }}</div>
      <div class="stat-label">错题总数</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{{ mistakeRate }}%</div>
      <div class="stat-label">错题占比</div>
    </div>
    <div class="stat-item">
      <div class="stat-num">{{ masteryRate }}%</div>
      <div class="stat-label">掌握率</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  mistakeCount: { type: Number, default: 0 },
  mistakeRate: { type: Number, default: 0 },
  masteryRate: { type: Number, default: 100 },
})
</script>

<style lang="scss" scoped>
.mistake-stats {
  display: flex;
  gap: 16px;
  margin-bottom: 28px;
}
.stat-item {
  flex: 1;
  text-align: center;
  padding: 18px 12px;
  background: #fff;
  border-radius: $radius-lg;
  box-shadow: 0 1px 6px rgba(0,0,0,.04);
}
.stat-num {
  font-size: 28px;
  font-weight: $font-weight-bold;
  color: $color-primary;
  margin-bottom: 4px;
}
.stat-label {
  font-size: $font-size-xs;
  color: $color-text-tertiary;
}
</style>