<template>
  <div class="quiz-panel">
    <!-- 顶部信息栏 -->
    <div class="quiz-topbar">
      <div class="quiz-meta">
        <span class="quiz-type-badge" :class="'type-' + currentQuestion.type">
          {{ QUESTION_TYPES[currentQuestion.type]?.label || currentQuestion.type }}
        </span>
        <span class="quiz-progress">{{ currentIndex + 1 }} / {{ totalCount }}</span>
        <span class="quiz-difficulty" v-if="currentQuestion.difficulty">
          {{ '★'.repeat(currentQuestion.difficulty) }}{{ '☆'.repeat(3 - currentQuestion.difficulty) }}
        </span>
      </div>
      <div class="quiz-actions">
        <button class="btn-sm" @click="$emit('shuffle')">🔀 换一批</button>
      </div>
    </div>

    <!-- 进度条 -->
    <div class="progress-bar">
      <div class="progress-fill" :style="{ width: progress + '%' }"></div>
    </div>

    <!-- 题干 -->
    <div class="question-stem" v-html="renderLatex(currentQuestion.stem)"></div>

    <!-- 选项 -->
    <div class="question-options">
      <!-- 填空 -->
      <template v-if="currentQuestion.type === 'fill'">
        <div class="fill-input-wrap">
          <input
            class="fill-input"
            type="text"
            placeholder="请输入答案..."
            :value="fillText"
            :disabled="submitted[currentIndex]"
            @input="onFillInput"
            @keyup.enter="handleSubmit"
          />
        </div>
      </template>

      <!-- 判断 -->
      <template v-else-if="currentQuestion.type === 'truefalse'">
        <div
          v-for="(label, oi) in ['✓ 正确', '✗ 错误']" :key="oi"
          class="option-item"
          :class="optionClass(oi)"
          @click="selectOption(oi)"
        >
          <span class="option-marker">{{ oi === 0 ? '✓' : '✗' }}</span>
          <span class="option-text">{{ label }}</span>
        </div>
      </template>

      <!-- 单选/多选 -->
      <template v-else>
        <div
          v-for="(opt, oi) in currentQuestion.options" :key="oi"
          class="option-item"
          :class="optionClass(oi)"
          @click="selectOption(oi)"
        >
          <span class="option-marker" :class="{ multi: currentQuestion.type === 'multi' }">
            {{ currentQuestion.type === 'multi' ? (isSelected(oi) ? '☑' : '☐') : String.fromCharCode(65 + oi) }}
          </span>
          <span class="option-text" v-html="renderLatex(opt)"></span>
        </div>
      </template>
    </div>

    <!-- 解析区（提交后显示） -->
    <div v-if="submitted[currentIndex]" class="analysis-box" :class="{ correct: isCorrect(currentIndex), wrong: isCorrect(currentIndex) === false }">
      <div class="analysis-header">
        <span class="analysis-icon">{{ isCorrect(currentIndex) ? '✅ 回答正确' : '❌ 回答错误' }}</span>
        <span v-if="isCorrect(currentIndex) === false && currentQuestion.answer.length" class="correct-answer">
          正确答案：{{ formatAnswer(currentQuestion) }}
        </span>
      </div>
      <div class="analysis-body">{{ currentQuestion.analysis }}</div>
    </div>

    <!-- AI 解题解析模块（提交后显示） -->
    <AiSolutionPanel v-if="submitted[currentIndex]" />

    <!-- 底部导航 -->
    <div class="quiz-nav">
      <button :disabled="isFirst" @click="$emit('prev')" class="nav-btn">← 上一题</button>
      <button
        v-if="!submitted[currentIndex]"
        class="nav-btn submit-btn"
        @click="handleSubmit"
      >
        提交答案
      </button>
      <button v-else class="nav-btn" @click="$emit('next')">
        {{ isLast ? '完成' : '下一题 →' }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { QUESTION_TYPES } from '@/constants/quiz'
import AiSolutionPanel from './AiSolutionPanel.vue'

const props = defineProps({
  currentQuestion: { type: Object, required: true },
  currentIndex: { type: Number, required: true },
  totalCount: { type: Number, required: true },
  isFirst: { type: Boolean, default: true },
  isLast: { type: Boolean, default: false },
  progress: { type: Number, default: 0 },
  submitted: { type: Array, required: true },
  userAnswers: { type: Array, required: true },
  fillText: { type: String, default: '' },
})

const emit = defineEmits(['select', 'fillInput', 'submit', 'prev', 'next', 'shuffle'])

function selectOption(oi) {
  if (props.submitted[props.currentIndex]) return
  emit('select', oi)
}
function onFillInput(e) {
  emit('fillInput', e.target.value)
}
function handleSubmit() {
  emit('submit')
}
function isSelected(oi) {
  const arr = props.userAnswers[props.currentIndex]
  return arr ? arr.includes(oi) : false
}

function isCorrect(index) {
  return null // 由父组件提供
}

function optionClass(oi) {
  const submitted = props.submitted[props.currentIndex]
  const q = props.currentQuestion
  if (!submitted) {
    return isSelected(oi) ? 'selected' : ''
  }
  const ans = q.answer || []
  const isAns = ans.includes(oi)
  const isSel = isSelected(oi)
  if (isAns) return 'correct'
  if (isSel && !isAns) return 'wrong'
  return ''
}

function formatAnswer(q) {
  if (q.type === 'truefalse') return q.answer[0] === 0 ? '正确' : '错误'
  if (q.type === 'fill') return '(见解析)'
  return q.answer.map(i => q.options[i]?.replace(/^[A-E]\.\s*/, '')).join('；')
}

function renderLatex(text) {
  if (!text) return ''
  return text.replace(/\\\(([^)]+)\\\)/g, '<em class="latex">$1</em>')
}
</script>

<style lang="scss" scoped>
.quiz-panel { background: #fff; border-radius: $radius-xl; padding: 28px 24px; box-shadow: 0 2px 12px rgba(0,0,0,.04); }
.quiz-topbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }
.quiz-meta { display: flex; align-items: center; gap: 12px; }
.quiz-type-badge {
  padding: 2px 10px; font-size: 11px; font-weight: $font-weight-medium; border-radius: $radius-full;
  &.type-single { background: #e3f2fd; color: #1565c0; }
  &.type-multi { background: #fce4ec; color: #c62828; }
  &.type-truefalse { background: #e8f5e9; color: #2e7d32; }
  &.type-fill { background: #fff3e0; color: #e65100; }
}
.quiz-progress { font-size: $font-size-sm; color: $color-text-muted; }
.quiz-difficulty { font-size: 11px; color: #f5a623; letter-spacing: 1px; }
.btn-sm { padding: 4px 14px; font-size: 11px; border: 1px solid #e0e0e0; background: #fff; border-radius: $radius-md; color: $color-text-secondary; cursor: pointer; }
.progress-bar { height: 4px; background: #eef1f5; border-radius: $radius-full; margin-bottom: 24px; overflow: hidden;
  .progress-fill { height: 100%; background: $color-primary; transition: width .3s; }
}
.question-stem { font-size: $font-size-base; color: $color-text-primary; line-height: 1.8; margin-bottom: 24px; white-space: pre-wrap;
  :deep(.latex) { font-style: italic; color: $color-primary; font-family: 'Times New Roman', serif; }
}
.question-options { display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px; }
.option-item {
  display: flex; align-items: flex-start; gap: 10px; padding: 12px 14px;
  border: 1.5px solid #eef1f5; border-radius: $radius-md; cursor: pointer; transition: all .15s;
  &:hover { border-color: $color-primary-light; background: #f5f8ff; }
  &.selected { border-color: $color-primary; background: #eef3ff; }
  &.correct { border-color: #4caf50; background: #e8f5e9; .option-marker { background: #4caf50; color: #fff; } }
  &.wrong { border-color: #f44336; background: #ffebee; .option-marker { background: #f44336; color: #fff; } }
}
.option-marker {
  width: 28px; height: 28px; display: flex; align-items: center; justify-content: center;
  border-radius: $radius-sm; background: #f5f6f8; font-size: $font-size-xs; font-weight: $font-weight-semibold; color: $color-text-muted; flex-shrink: 0;
  &.multi { font-size: 16px; }
}
.option-text { font-size: $font-size-sm; color: $color-text-primary; line-height: 28px;
  :deep(.latex) { font-style: italic; color: $color-primary; }
}
.fill-input-wrap { padding: 4px 0; }
.fill-input {
  width: 100%; padding: 12px 14px; border: 1.5px solid #e0e0e0; border-radius: $radius-md; font-size: $font-size-sm; outline: none;
  &:focus { border-color: $color-primary; }
  &:disabled { background: #f5f6f8; }
}
.analysis-box {
  padding: 16px; border-radius: $radius-md; margin-bottom: 20px;
  &.correct { background: #e8f5e9; border: 1px solid #a5d6a7; }
  &.wrong { background: #ffebee; border: 1px solid #ef9a9a; }
}
.analysis-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
.analysis-icon { font-size: $font-size-sm; font-weight: $font-weight-medium; }
.correct-answer { font-size: $font-size-xs; color: $color-text-secondary; }
.analysis-body { font-size: $font-size-xs; color: $color-text-tertiary; line-height: 1.6; }
.quiz-nav { display: flex; justify-content: space-between; gap: 12px; padding-top: 8px; }
.nav-btn {
  flex: 1; padding: 10px; font-size: $font-size-sm; font-weight: $font-weight-medium;
  border: 1.5px solid #e0e0e0; background: #fff; border-radius: $radius-md; cursor: pointer; color: $color-text-secondary;
  &:hover:not(:disabled) { border-color: $color-primary; color: $color-primary; }
  &:disabled { opacity: .4; cursor: not-allowed; }
  &.submit-btn { border-color: $color-primary; background: $color-primary; color: #fff; }
}

</style>
