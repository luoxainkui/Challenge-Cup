<template>
  <div class="home-page">
    <!-- 英雄区域 -->
    <section class="hero">
      <div class="hero-bg"></div>
      <div class="hero-gradient-rect"></div>
      <div class="hero-content">
        <h1>广西专升本<br/>从这里开始</h1>
        <p>精讲课程 · 智能题库 · 伴学服务<br/>为广西学子量身打造的专升本一站式解决方案</p>
        <div class="hero-btns">
          <a href="/courses" class="btn-primary" @click.prevent="$router.push('/courses')">开始学习</a>
          <a href="#services" class="btn-outline" @click.prevent="scrollToSection('services')">了解更多</a>
        </div>
      </div>
      <div class="hero-stats">
        <div class="stat-item" v-for="s in HOME_STATS" :key="s.num">
          <span class="stat-num">{{ s.num }}</span>
          <span class="stat-label">{{ s.label }}</span>
        </div>
      </div>
    </section>

    <!-- 精选课程 -->
    <section id="services" class="featured-courses">
      <h2 class="section-title">核心服务</h2>
      <p class="section-subtitle">精选优质课程，覆盖公共课与专业课，助你高效备考</p>
      <div class="course-grid">
        <div
          class="course-card"
          v-for="c in FEATURED_COURSES"
          :key="c.id"
          @click="$router.push('/courses')"
        >
          <div class="card-cover" :style="{ background: c.color }">
            <span class="card-hot" v-if="c.hot">🔥 热报</span>
            <span class="card-category">{{ c.category }}</span>
          </div>
          <div class="card-body">
            <h4 class="card-subject">{{ c.subject }}</h4>
            <p class="card-name">{{ c.name }}</p>
            <div class="card-meta">
              <span>👨‍🏫 {{ c.teacher }}</span>
              <span>⭐ {{ c.rating }}</span>
            </div>
            <div class="card-footer">
              <span class="card-lessons">{{ c.lessons }}课时 · {{ c.duration }}</span>
              <span class="card-price" :class="{ free: c.price === 0 }">
                {{ c.price === 0 ? '免费' : '¥' + c.price }}
              </span>
            </div>
          </div>
        </div>
      </div>
      <div class="view-all">
        <a href="/courses" class="view-all-link" @click.prevent="$router.push('/courses')">
          查看全部课程 →
        </a>
      </div>
    </section>

    <!-- 为什么选择我们 -->
    <section class="why-us">
      <div class="why-us-bg-rect"></div>
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
import { HOME_STATS, ADVANTAGES } from '@/constants/home'
import { COURSES } from '@/constants/courses'
import { computed } from 'vue'

const FEATURED_COURSES = computed(() => COURSES.slice(0, 6))

function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}
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

/* Featured Courses */
.featured-courses {
  padding: 80px 0;
  max-width: $max-width;
  margin: 0 auto;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 36px;
}

.course-card {
  background: #fff;
  border-radius: $radius-xl;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: all $transition-base;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.1);

    .card-cover {
      filter: brightness(1.05);
    }
  }
}

.card-cover {
  height: 120px;
  position: relative;
  display: flex;
  align-items: flex-end;
  padding: 12px 16px;
}

.card-hot {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(255, 59, 48, 0.9);
  color: #fff;
  padding: 2px 10px;
  border-radius: $radius-full;
  font-size: 11px;
  font-weight: $font-weight-medium;
}

.card-category {
  background: rgba(255, 255, 255, 0.85);
  color: $color-text-secondary;
  padding: 3px 12px;
  border-radius: $radius-full;
  font-size: 11px;
}

.card-body {
  padding: 16px;
}

.card-subject {
  font-size: $font-size-sm;
  color: $color-primary;
  font-weight: $font-weight-semibold;
  margin-bottom: 4px;
}

.card-name {
  font-size: $font-size-base;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  margin-bottom: 10px;
  line-height: 1.4;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-meta {
  display: flex;
  gap: 16px;
  font-size: $font-size-xs;
  color: $color-text-tertiary;
  margin-bottom: 12px;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 10px;
  border-top: 1px solid #f0f0f0;
}

.card-lessons {
  font-size: $font-size-xs;
  color: $color-text-muted;
}

.card-price {
  font-size: $font-size-md;
  font-weight: $font-weight-bold;
  color: $color-accent;

  &.free {
    color: $color-success;
  }
}

.view-all {
  text-align: center;
}

.view-all-link {
  color: $color-primary;
  font-weight: $font-weight-medium;
  font-size: $font-size-base;
  text-decoration: none;

  &:hover {
    text-decoration: underline;
  }
}

/* Why us */
.why-us {
  padding: 80px 0;
  background: #f8f9fb;
  position: relative;
  overflow: hidden;
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
  .featured-courses,
  .advantage-list {
    padding-left: 20px;
    padding-right: 20px;
  }
}

@include respond-to('tablet') {
  .course-grid {
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