<template>
  <div class="qp-sub-page">
    <header class="qp-sub-header">
      <button class="qp-sub-back" @click="router.push({ name: 'service-quiz' })">← 返回题库</button>
      <h1 class="qp-sub-title">章节练习</h1>
      <span class="qp-sub-count">{{ CHAPTERS.length }} 门科目</span>
    </header>

    <div class="qp-sub-body">
      <div v-for="ch in CHAPTERS" :key="ch.name" class="chapter-card">
        <div class="chapter-header">
          <span class="chapter-icon" :style="{ background: ch.color }">{{ ch.icon }}</span>
          <h3 class="chapter-name">{{ ch.name }}</h3>
        </div>
        <div class="topic-list">
          <div v-for="t in ch.topics" :key="t.id" class="topic-item" @click="startChapter(ch, t)">
            <span class="topic-name">{{ t.name }}</span>
            <span class="topic-count">{{ t.count }} 题</span>
            <span class="topic-arrow">→</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { CHAPTERS } from '@/constants/quiz'

const router = useRouter()

function startChapter(ch, t) {
  router.push({ name: 'quiz-practice', query: { mode: 'chapter', chapter: ch.name, topic: t.name } })
}
</script>

<style lang="scss" scoped>
.qp-sub-page {
  min-height: 100vh;
  background: #f5f6fa;
  padding: 0 20px 60px;
}
.qp-sub-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 0;
  max-width: $max-width;
  margin: 0 auto;
}
.qp-sub-back {
  padding: 8px 18px;
  font-size: $font-size-xs;
  border: 1px solid #e0e0e0;
  background: #fff;
  border-radius: $radius-md;
  color: $color-text-secondary;
  cursor: pointer;
  &:hover { color: $color-primary; border-color: $color-primary; }
}
.qp-sub-title {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
}
.qp-sub-count {
  font-size: $font-size-sm;
  color: $color-text-muted;
}
.qp-sub-body {
  max-width: $max-width;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
.chapter-card {
  background: #fff;
  padding: 24px;
  border-radius: $radius-xl;
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
}
.chapter-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}
.chapter-icon {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: $radius-sm;
  color: #fff;
  font-size: 12px;
  font-weight: $font-weight-bold;
}
.chapter-name {
  font-size: $font-size-base;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}
.topic-item {
  display: flex;
  align-items: center;
  padding: 12px 0;
  border-top: 1px solid #f0f2f5;
  cursor: pointer;
  transition: all .15s;
  &:hover { color: $color-primary; .topic-arrow { transform: translateX(4px); } }
}
.topic-name { flex: 1; font-size: $font-size-xs; color: $color-text-secondary; }
.topic-count { font-size: 11px; color: $color-text-tertiary; margin-right: 8px; }
.topic-arrow { font-size: 14px; color: $color-text-muted; transition: transform .15s; }

@media (max-width: 768px) {
  .qp-sub-body { grid-template-columns: 1fr; }
}
</style>