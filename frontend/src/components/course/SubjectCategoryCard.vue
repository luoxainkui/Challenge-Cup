<script setup>
defineProps({
  category: {
    type: Object,
    required: true,
  },
  courseCount: {
    type: Number,
    default: 0,
  },
})

const emit = defineEmits(['select'])
</script>

<template>
  <div
    class="subject-category-card"
    @click="emit('select', category)"
    :style="{ '--card-gradient': category.color }"
  >
    <div class="sc-card-bg" :style="{ background: category.color }">
      <span class="sc-card-icon">{{ category.icon }}</span>
    </div>
    <div class="sc-card-body">
      <h3 class="sc-card-name">{{ category.name }}</h3>
      <p class="sc-card-desc">{{ category.desc }}</p>
      <span class="sc-card-count">{{ courseCount }} 门课程</span>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.subject-category-card {
  background: #fff;
  border-radius: $radius-2xl;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.06);
  cursor: pointer;
  transition: all $transition-base;
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.12);

    .sc-card-bg {
      filter: brightness(1.08);
    }
  }
}

.sc-card-bg {
  height: 120px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  transition: filter $transition-fast;
}

.sc-card-icon {
  font-size: 44px;
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.15));
}

.sc-card-body {
  padding: 20px;
  text-align: center;
}

.sc-card-name {
  font-size: $font-size-2xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  margin-bottom: 8px;
}

.sc-card-desc {
  font-size: $font-size-sm;
  color: $color-text-muted;
  margin-bottom: 12px;
  line-height: 1.5;
}

.sc-card-count {
  display: inline-block;
  padding: 4px 16px;
  background: $color-primary-light;
  color: $color-primary;
  font-size: $font-size-xs;
  font-weight: $font-weight-medium;
  border-radius: $radius-full;
}
</style>