<template>
  <div class="video-wrapper">
    <div
      class="video-screen"
      :style="{ background: bgStyle }"
      :key="activeChapter?.title"
    >
      <div class="video-overlay">
        <div class="play-btn" @click="$emit('toggle')">
          {{ isPlaying ? '⏸' : '▶' }}
        </div>
        <div class="video-chapter-info" v-if="activeChapter">
          <span class="chapter-badge">第 {{ activeIdx + 1 }} 节</span>
          <p class="video-hint">{{ activeChapter.title }}</p>
          <span class="chapter-duration">⏱ {{ activeChapter.duration }}</span>
        </div>
        <p class="video-hint placeholder" v-else>点击左侧目录选择章节开始学习</p>
      </div>
      <div class="progress-bar" v-if="isPlaying">
        <div class="progress-fill" :style="{ animationDuration: activeChapter ? '2s' : '3s' }"></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const GRADIENTS = [
  'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
  'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
  'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
  'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
  'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
  'linear-gradient(135deg, #a18cd1 0%, #fbc2eb 100%)',
  'linear-gradient(135deg, #fccb90 0%, #d57eeb 100%)',
  'linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%)',
]

const props = defineProps({
  course: { type: Object, default: null },
  isPlaying: { type: Boolean, default: false },
  activeChapter: { type: Object, default: null },
  activeIdx: { type: Number, default: 0 },
})

defineEmits(['toggle'])

const bgStyle = computed(() => {
  if (props.activeChapter) {
    return GRADIENTS[props.activeIdx % GRADIENTS.length]
  }
  return props.course?.color || GRADIENTS[0]
})
</script>

<style lang="scss" scoped>
.video-wrapper {
  margin-bottom: 20px;
}

.video-screen {
  width: 100%;
  height: 360px;
  border-radius: $radius-xl;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.video-overlay {
  text-align: center;
  color: #fff;
  z-index: 1;
}

.play-btn {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.22);
  backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 34px;
  margin: 0 auto 16px;
  cursor: pointer;
  transition: all $transition-base;

  &:hover {
    background: rgba(255, 255, 255, 0.35);
    transform: scale(1.08);
  }
}

.video-chapter-info {
  text-align: center;
}

.chapter-badge {
  display: inline-block;
  padding: 4px 16px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: $radius-full;
  font-size: 12px;
  margin-bottom: 10px;
}

.video-hint {
  font-size: $font-size-lg;
  font-weight: $font-weight-semibold;
  opacity: 0.95;
  margin-bottom: 4px;

  &.placeholder {
    font-size: $font-size-base;
    font-weight: $font-weight-normal;
    opacity: 0.75;
  }
}

.chapter-duration {
  display: inline-block;
  font-size: $font-size-xs;
  opacity: 0.75;
  margin-top: 4px;
}

.progress-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: rgba(255, 255, 255, 0.2);
}

.progress-fill {
  height: 100%;
  width: 35%;
  background: #fff;
  border-radius: 0 2px 2px 0;
  animation: grow 3s ease-in-out infinite alternate;
}

@keyframes grow {
  from { width: 20%; }
  to { width: 70%; }
}

@include respond-to('tablet') {
  .video-screen {
    height: 280px;
  }
}
</style>