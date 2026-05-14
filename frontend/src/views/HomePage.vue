<template>
  <div class="home-page">
    <!-- 英雄区域 -->
    <section class="hero">
      <div class="hero-bg"></div>
      <div class="hero-content">
        <h1>广西专升本<br/>从这里开始</h1>
        <p>精讲课程 · 智能题库 · 伴学服务<br/>为广西学子量身打造的专升本一站式解决方案</p>
        <div class="hero-btns">
          <a href="/courses" class="btn-primary" @click.prevent="$router.push('/courses')">开始学习</a>
          <a href="/about" class="btn-outline" @click.prevent="$router.push('/about')">了解更多</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-item" v-for="s in HOME_STATS" :key="s.num">
          <span class="stat-num">{{ s.num }}</span>
          <span class="stat-label">{{ s.label }}</span>
        </div>
      </div>
    </section>

    <!-- 服务模块 -->
    <section class="services">
      <h2 class="section-title">核心服务</h2>
      <p class="section-subtitle">三大产品矩阵，覆盖专升本备考全流程</p>
      <div class="service-cards">
        <div class="service-card" v-for="svc in HOME_SERVICES" :key="svc.title" @click="$router.push(svc.link)">
          <div class="service-icon" v-html="svc.icon"></div>
          <h3>{{ svc.title }}</h3>
          <p>{{ svc.desc }}</p>
          <span class="service-link">了解详情 →</span>
        </div>
      </div>
    </section>

    <!-- 为什么选择我们 -->
    <section class="why-us">
      <h2 class="section-title">为什么选择桂升通</h2>
      <div class="advantage-list">
        <div class="advantage-item" v-for="adv in ADVANTAGES" :key="adv.title">
          <div class="advantage-icon" :style="{ background: adv.color }">{{ adv.icon }}</div>
          <h4>{{ adv.title }}</h4>
          <p>{{ adv.desc }}</p>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="cta">
      <h2>准备好开启你的本科之路了吗？</h2>
      <p>加入桂升通，让专业团队助你圆梦本科</p>
      <a href="/courses" class="btn-primary" @click.prevent="$router.push('/courses')">立即开始</a>
    </section>
  </div>
</template>

<script setup>
import { HOME_STATS, HOME_SERVICES, ADVANTAGES } from '@/constants/home'
</script>

<style lang="scss" scoped>
.home-page {
  padding-top: $header-height;
}

.section-title {
  text-align: center;
  font-size: $font-size-4xl;
  font-weight: $font-weight-bold;
  margin-bottom: 12px;
}

.section-subtitle {
  text-align: center;
  color: $color-text-quaternary;
  margin-bottom: 48px;
}

/* Hero */
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

/* Services */
.services {
  padding: 80px 0;
  width: $max-width;
  margin: 0 auto;
}

.service-cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.service-card {
  background: #fff;
  border-radius: $radius-xl;
  padding: 40px 30px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  transition: all $transition-base;
  cursor: pointer;
  text-align: center;

  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
  }
}

.service-icon {
  font-size: 48px;
  margin-bottom: 20px;
}

.service-card h3 {
  font-size: $font-size-xl;
  font-weight: $font-weight-semibold;
  margin-bottom: 12px;
}

.service-card p {
  color: $color-text-quaternary;
  font-size: $font-size-base;
  line-height: 1.6;
  margin-bottom: 16px;
}

.service-link {
  color: $color-primary;
  font-weight: $font-weight-medium;
}

/* Why us */
.why-us {
  padding: 80px 0;
  background: #f8f9fb;
}

.advantage-list {
  width: $max-width;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
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

.advantage-item h4 {
  font-size: $font-size-md;
  font-weight: $font-weight-semibold;
  margin-bottom: 8px;
}

.advantage-item p {
  font-size: $font-size-sm;
  color: $color-text-quaternary;
  line-height: 1.5;
}

/* CTA */
.cta {
  padding: 80px 0;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  h2 {
    font-size: $font-size-3xl;
    margin-bottom: 12px;
  }
  p {
    font-size: $font-size-md;
    opacity: 0.85;
    margin-bottom: 28px;
  }
}

@include respond-to('desktop') {
  .services,
  .advantage-list {
    width: 100%;
    padding-left: 20px;
    padding-right: 20px;
  }
}

@include respond-to('tablet') {
  .service-cards {
    grid-template-columns: 1fr;
  }
  .advantage-list {
    grid-template-columns: repeat(2, 1fr);
  }
  .hero-content h1 {
    font-size: 32px;
  }
}

@include respond-to('mobile') {
  .advantage-list {
    grid-template-columns: 1fr;
  }
}
</style>