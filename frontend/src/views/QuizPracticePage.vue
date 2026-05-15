<template>
  <div class="quiz-practice-page">
    <!-- 顶部 -->
    <header class="qp-header">
      <button class="qp-back" @click="router.push({ name: 'service-quiz' })">← 返回题库</button>
      <h1 class="qp-title">{{ quizTitle }}</h1>
      <span class="qp-count">{{ currentIndex + 1 }} / {{ totalCount }}</span>
    </header>

    <!-- 进度条 -->
    <div class="qp-progress">
      <div class="qp-progress-bar" :style="{ width: progress + '%' }"></div>
    </div>

    <!-- 答题面板 -->
    <QuizPanel
      v-if="!showResult"
      :current-question="currentQuestion"
      :current-index="currentIndex"
      :total-count="totalCount"
      :is-first="isFirst"
      :is-last="isLast"
      :progress="progress"
      :submitted="submitted"
      :user-answers="userAnswers"
      :fill-text="fillText"
      @select="selectOption"
      @fill-input="onFill"
      @submit="onSubmit"
      @prev="prev"
      @next="onNext"
      @shuffle="shuffle"
    />

    <!-- 成绩单 -->
    <QuizResult
      v-else
      :score="stats.score"
      :correct="stats.correct"
      :wrong="stats.wrong"
      :unanswered="stats.unanswered"
      :total="stats.total"
      :elapsed="elapsed"
      :questions="questions"
      :user-answers="userAnswers"
      :submitted="submitted"
      @retry="retry"
      @close="router.push({ name: 'service-quiz' })"
    />

    <!-- 底部占位 -->
    <div class="qp-footer-spacer"></div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useQuiz } from '@/composables/useQuiz'
import QuizPanel from '@/components/quiz/QuizPanel.vue'
import QuizResult from '@/components/quiz/QuizResult.vue'

const router = useRouter()
const route = useRoute()

// 从路由参数读取模式
const mode = computed(() => route.query.mode || 'free')
const quizTitle = computed(() => {
  const m = mode.value
  if (m === 'free') return '自由刷题'
  if (m === 'chapter') return `${route.query.chapter || ''} · ${route.query.topic || ''}`
  if (m === 'mock') return `${route.query.paper || '模拟考试'}（模拟考试 · ${route.query.duration || '120'}分钟）`
  if (m === 'real') return `${route.query.paper || '历年真题'}（历年真题 · ${route.query.duration || '120'}分钟）`
  if (m === 'subject') return `${route.query.subject || ''} 练习`
  return '刷题练习'
})

const {
  currentQuestion, currentIndex, totalCount, isLast, isFirst, progress,
  userAnswers, submitted, questions, stats, elapsed,
  selectOption, setFillAnswer, submitCurrent, next, prev, shuffle, reset,
} = useQuiz(null)

const showResult = ref(false)
const fillText = ref('')

function onFill(val) {
  fillText.value = val
  setFillAnswer(val)
}

function onSubmit() {
  fillText.value = ''
  submitCurrent()
}

function onNext() {
  if (isLast.value) {
    showResult.value = true
  } else {
    next()
    fillText.value = ''
  }
}

function retry() {
  showResult.value = false
  reset()
  fillText.value = ''
}

</script>

<style lang="scss" scoped>
.quiz-practice-page {
  min-height: 100vh;
  background: #f5f6fa;
  padding: $header-height 20px 40px;
}

.qp-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 0;
  max-width: 800px;
  margin: 0 auto;
}

.qp-back {
  padding: 6px 14px;
  font-size: $font-size-xs;
  border: 1px solid #e0e0e0;
  background: #fff;
  border-radius: $radius-md;
  color: $color-text-secondary;
  cursor: pointer;
  &:hover { color: $color-primary; border-color: $color-primary; }
}

.qp-title {
  font-size: $font-size-lg;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.qp-count {
  font-size: $font-size-sm;
  color: $color-text-muted;
}

.qp-progress {
  max-width: 800px;
  margin: 0 auto 20px;
  height: 4px;
  background: #eef1f5;
  border-radius: $radius-full;
  overflow: hidden;
}

.qp-progress-bar {
  height: 100%;
  background: $color-primary;
  transition: width .3s;
}

.qp-footer-spacer {
  height: 40px;
}

:deep(.quiz-panel) {
  max-width: 800px;
  margin: 0 auto;
}

:deep(.quiz-result) {
  max-width: 800px;
  margin: 0 auto;
}
</style>