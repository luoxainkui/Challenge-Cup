<template>
  <section class="hero">
    <div class="hero-bg"></div>
    <div class="hero-gradient-rect"></div>
    <div class="hero-content">
      <h1>广西专升本<br />从这里开始</h1>
      <p>精讲课程 · 智能题库 · 伴学服务<br />为广西学子量身打造的专升本一站式解决方案</p>
      <div class="hero-btns">
        <a href="/courses" class="btn-primary" @click.prevent="$router.push('/courses')">开始学习</a>
        <a href="#services" class="btn-outline" @click.prevent="$emit('scrollTo', 'services')">了解更多</a>
      </div>
    </div>
    <div class="hero-stats">
      <div class="stat-item" v-for="s in stats" :key="s.num">
        <span class="stat-num">{{ s.num }}</span>
        <span class="stat-label">{{ s.label }}</span>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({ stats: { type: Array, required: true } })
defineEmits(['scrollTo'])
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.hero {
  position: relative;
  min-height: 520px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  padding: 60px 20px;
}

.hero-bg {
  position: absolute;
  inset: 0;
  background: $color-gradient-primary;
  z-index: -1;

  &::after {
    content: '';
    position: absolute;
    inset: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 320"><path fill="white" fill-opacity="0.08" d="M0,160L48,176C96,192,192,224,288,240C384,256,480,256,576,224C672,192,768,128,864,122.7C960,117,1056,171,1152,181.3C1248,192,1344,160,1392,144L1440,128V320H0Z"/></svg>') no-repeat bottom;
    background-size: cover;
  }
}

.hero-gradient-rect {
  position: absolute;
  top: 40px;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 360px;
  border-radius: 40px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.08) 0%, rgba(255, 255, 255, 0.02) 50%, transparent 100%);
  z-index: 0;
  pointer-events: none;
}

.hero-content {
  text-align: center;
  color: #fff;
  z-index: 1;

  h1 {
    font-size: 48px;
    font-weight: $font-weight-bold;
    margin-bottom: 20px;
    line-height: 1.3;
  }
  p {
    font-size: $font-size-lg;
    opacity: 0.9;
    margin-bottom: 32px;
    line-height: 1.8;
  }
}

.hero-btns {
  display: flex;
  gap: 16px;
  justify-content: center;
}

.btn-primary {
  display: inline-block;
  padding: 14px 36px;
  background: #fff;
  color: $color-primary;
  border-radius: $radius-full;
  font-weight: $font-weight-semibold;
  font-size: $font-size-md;
  text-decoration: none;
  transition: all $transition-base;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }
}

.btn-outline {
  display: inline-block;
  padding: 14px 36px;
  border: 2px solid rgba(255, 255, 255, 0.6);
  color: #fff;
  border-radius: $radius-full;
  font-weight: $font-weight-semibold;
  font-size: $font-size-md;
  text-decoration: none;
  transition: all $transition-base;

  &:hover {
    background: rgba(255, 255, 255, 0.15);
    border-color: #fff;
  }
}

.hero-stats {
  display: flex;
  gap: 60px;
  margin-top: 48px;
  z-index: 1;
  flex-wrap: wrap;
  justify-content: center;
}

.stat-item {
  text-align: center;
  color: #fff;
}

.stat-num {
  display: block;
  font-size: $font-size-3xl;
  font-weight: $font-weight-bold;
}

.stat-label {
  font-size: $font-size-base;
  opacity: 0.8;
}

@media (max-width: 768px) {
  .hero-content h1 {
    font-size: 32px;
  }
}
</style>