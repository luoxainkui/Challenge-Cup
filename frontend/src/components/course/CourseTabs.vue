<template>
  <section class="courses-tabs">
    <div class="tabs-inner">
      <button
        v-for="c in COURSES"
        :key="c.id"
        :class="{ active: currentCourse?.id === c.id }"
        @click="$emit('switch', c)"
        class="tab-btn"
      >
        <span class="tab-dot" :style="{ background: c.color }"></span>
        {{ c.subject }}
      </button>
    </div>
  </section>
</template>

<script setup>
import { COURSES } from '@/constants/courses'

defineProps({
  currentCourse: { type: Object, default: null },
})

defineEmits(['switch'])
</script>

<style lang="scss" scoped>
.courses-tabs {
  background: #fff;
  border-bottom: 1px solid #edf0f5;
  position: sticky;
  top: 64px;
  z-index: 10;
}

.tabs-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  gap: 4px;
  overflow-x: auto;
  padding: 6px 40px;

  &::-webkit-scrollbar {
    height: 0;
  }
}

.tab-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 18px;
  border: none;
  background: transparent;
  font-size: $font-size-sm;
  font-weight: $font-weight-medium;
  color: $color-text-tertiary;
  cursor: pointer;
  white-space: nowrap;
  border-radius: $radius-full;
  transition: all $transition-fast;

  &:hover {
    color: $color-primary;
    background: #f3f6ff;
  }

  &.active {
    color: #fff;
    background: $color-primary;
  }
}

.tab-dot {
  display: inline-block;
  width: 8px;
  height: 8px;
  border-radius: $radius-round;
}

@include respond-to('mobile') {
  .tabs-inner {
    padding: 4px 16px;
  }
  .tab-btn {
    padding: 6px 14px;
    font-size: $font-size-xs;
  }
}
</style>