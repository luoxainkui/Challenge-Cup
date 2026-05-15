<template>
  <div class="course-detail" v-if="course">
    <div class="detail-header">
      <h2>{{ course.name }}</h2>
      <span class="detail-price">{{ course.price === 0 ? '免费' : '¥' + course.price }}</span>
    </div>
    <div class="detail-tags">
      <span class="tag">{{ course.teacher }}</span>
      <span class="tag">⏱ {{ course.duration }}</span>
      <span class="tag rating">⭐ {{ course.rating }}</span>
    </div>
    <p class="detail-desc">{{ course.desc }}</p>
    <button class="btn-primary" @click="$emit('enroll', course)">
      {{ course.price === 0 ? '开始学习' : '加入学习' }}
    </button>
  </div>
</template>

<script setup>
defineProps({
  course: { type: Object, default: null },
})

defineEmits(['enroll'])
</script>

<style lang="scss" scoped>
.course-detail {
  padding-top: 20px;
}

.detail-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 8px;

  h2 {
    font-size: $font-size-xl;
    font-weight: $font-weight-bold;
  }
}

.detail-price {
  font-size: $font-size-lg;
  font-weight: $font-weight-bold;
  color: $color-accent;
}

.detail-tags {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.tag {
  padding: 3px 10px;
  background: #f5f6f8;
  border-radius: $radius-full;
  font-size: $font-size-xs;
  color: $color-text-tertiary;

  &.rating {
    color: #f5a623;
    background: #fffbf0;
  }
}

.detail-desc {
  font-size: $font-size-sm;
  color: $color-text-quaternary;
  line-height: 1.6;
  margin-bottom: 16px;
}

.btn-primary {
  padding: 10px 28px;
  background: $color-primary;
  color: #fff;
  border: none;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  font-weight: $font-weight-semibold;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover {
    background: #4758e0;
  }
}
</style>
