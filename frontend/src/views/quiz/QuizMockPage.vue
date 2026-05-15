<template>
  <div class="qp-sub-page">
    <header class="qp-sub-header">
      <button class="qp-sub-back" @click="router.push({ name: 'service-quiz' })">← 返回题库</button>
      <h1 class="qp-sub-title">模拟考试</h1>
      <span class="qp-sub-count">{{ MOCK_PAPERS.length }} 套试卷</span>
    </header>

    <div class="qp-sub-body">
      <div v-for="p in MOCK_PAPERS" :key="p.id" class="paper-card" @click="startExam(p)">
        <span class="paper-icon">📝</span>
        <h3 class="paper-name">{{ p.name }}</h3>
        <div class="paper-meta">
          <span>科目：{{ p.subject }}</span>
          <span>⏱ {{ p.duration }} 分钟</span>
          <span>📋 {{ p.total }} 题</span>
        </div>
        <button class="paper-btn">开始考试</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { MOCK_PAPERS } from '@/constants/quiz'

const router = useRouter()

function startExam(p) {
  router.push({ name: 'quiz-practice', query: { mode: 'mock', paper: p.name, duration: p.duration } })
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
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
.paper-card {
  background: #fff;
  padding: 32px 24px;
  border-radius: $radius-xl;
  text-align: center;
  cursor: pointer;
  transition: all $transition-base;
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
  &:hover { transform: translateY(-3px); box-shadow: 0 8px 28px rgba(0,0,0,.08); }
}
.paper-icon { font-size: 40px; display: block; margin-bottom: 10px; }
.paper-name { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 12px; }
.paper-meta {
  display: flex;
  flex-direction: column;
  gap: 4px;
  font-size: 11px;
  color: $color-text-tertiary;
  margin-bottom: 20px;
}
.paper-btn {
  padding: 8px 32px;
  border: 1.5px solid $color-primary;
  background: #fff;
  color: $color-primary;
  border-radius: $radius-md;
  font-size: $font-size-xs;
  font-weight: $font-weight-medium;
  cursor: pointer;
  &:hover { background: $color-primary; color: #fff; }
}

@media (max-width: 768px) {
  .qp-sub-body { grid-template-columns: 1fr; }
}
</style>