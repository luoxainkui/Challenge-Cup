<template>
  <aside class="directory-panel">
    <div class="directory-header">
      <h3>课程目录</h3>
      <span class="chapter-count">{{ chapters.length }} 节</span>
    </div>
    <ul class="chapter-list">
      <li
        v-for="(ch, idx) in chapters"
        :key="idx"
        :class="{ active: activeIdx === idx, done: ch.done }"
        @click="$emit('play', idx)"
      >
        <span class="ch-num">{{ ch.done ? '✓' : idx + 1 }}</span>
        <p class="ch-title">{{ ch.title }}</p>
      </li>
    </ul>
  </aside>
</template>

<script setup>
defineProps({
  chapters: { type: Array, default: () => [] },
  activeIdx: { type: Number, default: 0 },
})

defineEmits(['play'])
</script>

<style lang="scss" scoped>
.directory-panel {
  width: 240px;
  flex-shrink: 0;
  background: #fff;
  border-radius: $radius-lg;
  box-shadow: 0 1px 8px rgba(0, 0, 0, 0.05);
  display: flex;
  flex-direction: column;
  max-height: 500px;
}

.directory-header {
  padding: 14px 16px 12px;
  border-bottom: 1px solid #f2f4f7;
  display: flex;
  justify-content: space-between;
  align-items: baseline;

  h3 {
    font-size: $font-size-base;
    font-weight: $font-weight-bold;
  }

  .chapter-count {
    font-size: $font-size-xs;
    color: $color-text-tertiary;
  }
}

.chapter-list {
  flex: 1;
  overflow-y: auto;
  padding: 4px 0;
  list-style: none;
  margin: 0;

  &::-webkit-scrollbar {
    width: 3px;
  }
  &::-webkit-scrollbar-thumb {
    background: #d0d5dd;
    border-radius: 10px;
  }
}

.chapter-list li {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 16px;
  cursor: pointer;
  transition: all $transition-fast;
  border-left: 2px solid transparent;

  &:hover {
    background: #f7f9fc;
  }

  &.active {
    background: #eef5ff;
    border-left-color: $color-primary;

    .ch-num {
      background: $color-primary;
      color: #fff;
    }
    .ch-title {
      color: $color-primary;
    }
  }

  &.done .ch-num {
    background: #e8f5e9;
    color: #4caf50;
  }
}

.ch-num {
  width: 26px;
  height: 26px;
  border-radius: 50%;
  background: #f2f4f7;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 11px;
  font-weight: $font-weight-bold;
  flex-shrink: 0;
}

.ch-title {
  font-size: $font-size-sm;
  color: $color-text-primary;
  line-height: 1.3;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

@include respond-to('tablet') {
  .directory-panel {
    width: 100%;
    max-height: 280px;
  }
}
</style>
