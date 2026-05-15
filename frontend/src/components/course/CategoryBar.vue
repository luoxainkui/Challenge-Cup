<script setup>
import { COURSE_CATEGORIES } from '@/constants/courses'

defineProps({
  modelValue: {
    type: String,
    default: 'all',
  },
})

const emit = defineEmits(['update:modelValue'])
</script>

<template>
  <div class="category-bar">
    <button
      v-for="cat in COURSE_CATEGORIES"
      :key="cat.value"
      :class="{ active: modelValue === cat.value }"
      @click="emit('update:modelValue', cat.value)"
    >
      {{ cat.label }}
    </button>
  </div>
</template>

<style lang="scss" scoped>
.category-bar {
  display: flex;
  justify-content: center;
  gap: 12px;
  padding: 24px 0;
  background: #fff;
  border-bottom: 1px solid #edf0f5;
  position: sticky;
  top: 64px;
  z-index: 10;
}

button {
  padding: 10px 28px;
  border: 1.5px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  font-weight: $font-weight-medium;
  color: $color-text-tertiary;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover {
    border-color: $color-primary;
    color: $color-primary;
  }

  &.active {
    background: $color-primary;
    color: #fff;
    border-color: $color-primary;
  }
}
</style>