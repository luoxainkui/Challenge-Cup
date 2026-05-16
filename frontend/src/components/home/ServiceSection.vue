<template>
  <section id="services" class="featured-courses">
    <h2 class="section-title">核心服务</h2>
    <p class="section-subtitle">精选优质课程，覆盖公共课与专业课，助你高效备考</p>
    <div class="course-grid">
      <div
        class="course-card"
        v-for="c in courses"
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
</template>

<script setup>
defineProps({ courses: { type: Array, required: true } })
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.featured-courses {
  padding: 80px 0;
  max-width: $max-width;
  margin: 0 auto;
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

.course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  margin-bottom: 36px;
  @media (max-width: 768px) {
    grid-template-columns: 1fr;
  }
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

@media (min-width: 1024px) {
  .featured-courses {
    padding-left: 20px;
    padding-right: 20px;
  }
}
</style>