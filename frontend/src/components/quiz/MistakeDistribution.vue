<template>
  <div class="distribution" v-if="distribution.length > 0">
    <h4 class="distribution-title">考点错题分布</h4>
    <div class="distribution-chart">
      <div
        v-for="item in distribution"
        :key="item.point.id"
        class="chart-row"
      >
        <span class="chart-label" :title="item.point.subject + '·' + item.point.name">{{ item.point.name }}</span>
        <div class="chart-bar-wrap">
          <div
            class="chart-bar"
            :style="{ width: (item.count / maxCount * 100) + '%' }"
          >
            <span class="chart-bar-num">{{ item.count }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  distribution: { type: Array, default: () => [] },
  maxCount: { type: Number, default: 1 },
})
</script>

<style lang="scss" scoped>
.distribution {
  background: #fff;
  border-radius: $radius-lg;
  padding: 20px;
  margin-bottom: 28px;
  box-shadow: 0 1px 6px rgba(0,0,0,.04);
}
.distribution-title {
  font-size: $font-size-base;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
  margin-bottom: 16px;
}
.distribution-chart {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.chart-row {
  display: flex;
  align-items: center;
  gap: 12px;
}
.chart-label {
  width: 120px;
  text-align: right;
  font-size: $font-size-xs;
  color: $color-text-secondary;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  flex-shrink: 0;
}
.chart-bar-wrap {
  flex: 1;
  background: #f0f2f5;
  border-radius: $radius-full;
  height: 24px;
  overflow: hidden;
}
.chart-bar {
  height: 100%;
  background: linear-gradient(90deg, $color-primary, $color-primary-light);
  border-radius: $radius-full;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  padding-right: 8px;
  min-width: 36px;
  transition: width .5s ease;
}
.chart-bar-num {
  font-size: 11px;
  color: #fff;
  font-weight: $font-weight-semibold;
}
</style>