<template>
  <div class="mistake-list">
    <div class="list-header">
      <span class="list-title">错题列表</span>
      <button v-if="list.length > 0" class="clear-btn" @click="$emit('clear')">清空全部</button>
    </div>

    <div v-if="list.length === 0" class="empty">
      <span class="empty-icon">&#9989;</span>
      <p>暂无错题，继续保持！</p>
    </div>

    <div v-for="item in list" :key="item.questionId" class="mistake-item" :class="{ expanded: expandedId === item.questionId }">
      <div class="mistake-item-header" @click="toggleExpand(item.questionId)">
        <div class="mistake-item-info">
          <span class="mistake-point">{{ item.point?.subject }} · {{ item.point?.name }}</span>
          <span class="mistake-count">错{{ item.wrongCount }}次 / 对{{ item.correctCount }}次</span>
        </div>
        <span class="mistake-arrow" :class="{ open: expandedId === item.questionId }">&#9662;</span>
      </div>

      <div v-if="expandedId === item.questionId" class="mistake-item-body">
        <div class="question-stem">{{ item.question.stem }}</div>
        <div class="question-options">
          <div
            v-for="(opt, idx) in item.question.options"
            :key="idx"
            class="option-item"
            :class="{
              'option-selected': selectedOption === idx && !answered,
              'option-correct': answered && idx === item.question.answer,
              'option-wrong': answered && selectedOption === idx && idx !== item.question.answer,
            }"
            @click="!answered && (selectedOption = idx)"
          >
            <span class="option-marker">{{ ['A', 'B', 'C', 'D'][idx] }}</span>
            <span class="option-text">{{ opt.replace(/^[A-D]\.\s*/, '') }}</span>
          </div>
        </div>

        <div v-if="!answered" class="answer-actions">
          <button class="submit-btn" :disabled="selectedOption === null" @click="submitAnswer(item)">提交答案</button>
        </div>

        <div v-if="answered" class="analysis-box" :class="lastResult === 'correct' ? 'analysis-correct' : 'analysis-wrong'">
          <div class="analysis-result">{{ lastResult === 'correct' ? '✓ 回答正确' : '✗ 回答错误' }}</div>
          <div class="analysis-text">{{ item.question.analysis }}</div>
          <div class="analysis-actions">
            <button class="retry-btn" @click="resetAnswer(item)">重新作答</button>
            <button class="remove-btn" @click="$emit('remove', item.questionId)">移出错题本</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  list: { type: Array, default: () => [] },
})

const emit = defineEmits(['correct', 'wrong', 'remove', 'clear'])

const expandedId = ref(null)
const selectedOption = ref(null)
const answered = ref(false)
const lastResult = ref(null)

function toggleExpand(id) {
  if (expandedId.value === id) { expandedId.value = null; return }
  expandedId.value = id
  selectedOption.value = null
  answered.value = false
  lastResult.value = null
}

function submitAnswer(item) {
  if (selectedOption.value === null) return
  answered.value = true
  if (selectedOption.value === item.question.answer) {
    lastResult.value = 'correct'
    emit('correct', item.questionId)
  } else {
    lastResult.value = 'wrong'
    emit('wrong', item.questionId)
  }
}

function resetAnswer(item) {
  selectedOption.value = null
  answered.value = false
  lastResult.value = null
  // keep expanded
}
</script>

<style lang="scss" scoped>
.mistake-list { margin-bottom: 32px; }
.list-header {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: 14px;
}
.list-title { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; }
.clear-btn {
  background: none; border: 1px solid #e0e4ea; padding: 4px 14px;
  border-radius: $radius-md; font-size: $font-size-xs; color: $color-text-tertiary; cursor: pointer;
  &:hover { border-color: $color-accent; color: $color-accent; }
}
.empty {
  text-align: center; padding: 48px 0; color: $color-text-muted;
  .empty-icon { font-size: 32px; display: block; margin-bottom: 8px; }
}
.mistake-item {
  background: #fff; border-radius: $radius-lg; margin-bottom: 10px;
  box-shadow: 0 1px 4px rgba(0,0,0,.04); overflow: hidden;
}
.mistake-item-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 14px 20px; cursor: pointer;
  &:hover { background: #fafbfc; }
}
.mistake-item-info { display: flex; gap: 12px; align-items: center; }
.mistake-point {
  font-size: $font-size-sm; color: $color-text-primary; font-weight: $font-weight-medium;
}
.mistake-count { font-size: $font-size-xs; color: $color-text-tertiary; }
.mistake-arrow {
  font-size: 14px; color: $color-text-muted; transition: transform $transition-fast;
  &.open { transform: rotate(180deg); }
}
.mistake-item-body { padding: 0 20px 20px; }
.question-stem {
  font-size: $font-size-sm; color: $color-text-primary; margin-bottom: 14px; line-height: 1.6;
}
.question-options { display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px; }
.option-item {
  display: flex; align-items: center; gap: 10px;
  padding: 10px 14px; border: 1.5px solid #e8ecf1; border-radius: $radius-md;
  cursor: pointer; transition: all $transition-fast;
  &:hover:not(.option-correct):not(.option-wrong) { border-color: $color-primary; }
  &.option-selected { border-color: $color-primary; background: #f0f4ff; }
  &.option-correct { border-color: #4caf50; background: #e8f5e9; }
  &.option-wrong { border-color: #f44336; background: #ffebee; }
}
.option-marker {
  width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
  background: #f5f6f8; font-size: $font-size-xs; font-weight: $font-weight-semibold; color: $color-text-secondary; flex-shrink: 0;
  .option-correct & { background: #4caf50; color: #fff; }
  .option-wrong & { background: #f44336; color: #fff; }
}
.option-text { font-size: $font-size-xs; color: $color-text-primary; line-height: 1.5; }
.answer-actions { text-align: center; }
.submit-btn {
  padding: 8px 40px; background: $color-primary; color: #fff; border: none;
  border-radius: $radius-md; font-size: $font-size-sm; font-weight: $font-weight-medium;
  cursor: pointer; transition: background $transition-fast;
  &:disabled { opacity: .5; cursor: not-allowed; }
  &:hover:not(:disabled) { background: $color-primary-dark; }
}
.analysis-box {
  padding: 14px; border-radius: $radius-md; margin-top: 8px;
  &.analysis-correct { background: #e8f5e9; }
  &.analysis-wrong { background: #ffebee; }
}
.analysis-result {
  font-size: $font-size-sm; font-weight: $font-weight-semibold; margin-bottom: 6px;
  .analysis-correct & { color: #2e7d32; }
  .analysis-wrong & { color: #c62828; }
}
.analysis-text { font-size: $font-size-xs; color: $color-text-secondary; line-height: 1.6; margin-bottom: 10px; }
.analysis-actions { display: flex; gap: 10px; }
.retry-btn, .remove-btn {
  padding: 5px 14px; border-radius: $radius-md; font-size: $font-size-xs; cursor: pointer;
}
.retry-btn { border: 1.5px solid $color-primary; color: $color-primary; background: #fff; }
.remove-btn { border: 1.5px solid $color-text-muted; color: $color-text-tertiary; background: #fff; }
</style>