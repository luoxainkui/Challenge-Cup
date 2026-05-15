<template>
  <div class="mistake-charts" v-if="subjectData.length > 0 || typeData.length > 0">
    <div class="chart-card">
      <h4 class="chart-title">科目错题分布</h4>
      <div class="bar-chart">
        <div
          v-for="item in subjectData"
          :key="item.subject"
          class="bar-col"
        >
          <div class="bar-value">{{ item.count }}</div>
          <div class="bar-fill-wrap">
            <div
              class="bar-fill"
              :style="{ height: (item.count / subjectMax * 100) + '%', background: item.color }"
            ></div>
          </div>
          <div class="bar-label">{{ item.subject }}</div>
        </div>
      </div>
    </div>

    <div class="chart-card">
      <h4 class="chart-title">题型错题分布</h4>
      <div class="bar-chart">
        <div
          v-for="item in typeData"
          :key="item.type"
          class="bar-col"
        >
          <div class="bar-value">{{ item.count }}</div>
          <div class="bar-fill-wrap">
            <div
              class="bar-fill"
              :style="{ height: (item.count / typeMax * 100) + '%' }"
            ></div>
          </div>
          <div class="bar-label">{{ item.label }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  subjectData: { type: Array, default: () => [] },
  subjectMax: { type: Number, default: 1 },
  typeData: { type: Array, default: () => [] },
  typeMax: { type: Number, default: 1 },
})
</script>

<style lang="scss" scoped>
.mistake-charts {
  display: flex;
  gap: 16px;
  margin-bottom: 28px;
}
.chart-card {
  flex: 1;
  background: #fff;
  border-radius: $radius-lg;
  padding: 20px;
  box-shadow: 0 1px 6px rgba(0,0,0,.04);
}
.chart-title {
  font-size: $font-size-base;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
  margin-bottom: 16px;
}
.bar-chart {
  display: flex;
  align-items: flex-end;
  justify-content: space-around;
  gap: 8px;
  height: 160px;
  padding: 0 4px;
}
.bar-col {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  flex: 1;
  min-width: 0;
}
.bar-value {
  font-size: $font-size-xs;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}
.bar-fill-wrap {
  width: 100%;
  max-width: 48px;
  height: 120px;
  background: #f0f2f5;
  border-radius: $radius-sm $radius-sm 0 0;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
}
.bar-fill {
  width: 100%;
  background: linear-gradient(180deg, $color-primary, $color-primary-light);
  border-radius: $radius-sm $radius-sm 0 0;
  transition: height .5s ease;
  min-height: 4px;
}
.bar-label {
  font-size: 10px;
  color: $color-text-muted;
  text-align: center;
  line-height: 1.3;
}
</style>