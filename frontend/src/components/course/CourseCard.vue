<script setup>
defineProps({
  course: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['click'])
</script>

<template>
  <div class="course-card" @click="emit('click', course)">
    <div class="card-cover" :style="{ background: course.color }">
      <span v-if="course.hot" class="card-hot">🔥 热报</span>
      <span class="card-category">{{ course.category }}</span>
    </div>
    <div class="card-body">
      <h3 class="card-subject">{{ course.subject }}</h3>
      <p class="card-name">{{ course.name }}</p>
      <p class="card-desc">{{ course.desc }}</p>
      <div class="card-meta">
        <span>👨‍🏫 {{ course.teacher }}</span>
        <span>⭐ {{ course.rating }}</span>
        <span>{{ course.students }}人已学</span>
      </div>
      <div class="card-footer">
        <span class="card-lessons">{{ course.lessons }}课时 · {{ course.duration }}</span>
        <span class="card-price" :class="{ free: course.price === 0 }">
          {{ course.price === 0 ? '免费' : '¥' + course.price }}
        </span>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
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
  margin-bottom: 6px;
  line-height: 1.4;
}

.card-desc {
  font-size: $font-size-xs;
  color: $color-text-quaternary;
  line-height: 1.5;
  margin-bottom: 10px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-meta {
  display: flex;
  gap: 12px;
  font-size: $font-size-xs;
  color: $color-text-tertiary;
  margin-bottom: 12px;
  flex-wrap: wrap;
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
</style>