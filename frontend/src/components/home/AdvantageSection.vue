<template>
  <section class="why-us">
    <div class="why-us-bg-rect"></div>
    <h2 class="section-title">为什么选择桂升通</h2>
    <div class="advantage-list">
      <div class="advantage-item" v-for="adv in advantages" :key="adv.title">
        <div class="advantage-icon" :style="{ background: adv.color }">{{ adv.icon }}</div>
        <h4>{{ adv.title }}</h4>
        <p>{{ adv.desc }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({ advantages: { type: Array, required: true } })
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.why-us {
  padding: 80px 0;
  background: #f8f9fb;
  position: relative;
  overflow: hidden;
}

.section-title {
  text-align: center;
  font-size: $font-size-4xl;
  font-weight: $font-weight-bold;
  margin-bottom: 12px;
}

.why-us-bg-rect {
  position: absolute;
  bottom: 0;
  left: -80px;
  width: 500px;
  height: 320px;
  border-radius: 30px;
  background: linear-gradient(200deg, rgba(42, 110, 255, 0.05) 0%, rgba(108, 92, 231, 0.03) 50%, transparent 100%);
  z-index: 0;
  pointer-events: none;
}

.advantage-list {
  width: $max-width;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
  position: relative;
  z-index: 1;
  @media (min-width: 1024px) {
    padding-left: 20px;
    padding-right: 20px;
  }
  @media (max-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }
  @media (max-width: 480px) {
    grid-template-columns: 1fr;
  }
}

.advantage-item {
  text-align: center;
  padding: 30px 20px;
  background: #fff;
  border-radius: $radius-xl;
  transition: transform $transition-base;

  &:hover {
    transform: translateY(-4px);
  }

  h4 {
    font-size: $font-size-md;
    font-weight: $font-weight-semibold;
    margin-bottom: 8px;
  }
  p {
    font-size: $font-size-sm;
    color: $color-text-quaternary;
    line-height: 1.5;
  }
}

.advantage-icon {
  width: 64px;
  height: 64px;
  border-radius: $radius-xl;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 16px;
  color: #fff;
  font-size: $font-size-2xl;
}
</style>