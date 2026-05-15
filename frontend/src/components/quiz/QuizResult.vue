<template>
  <div class="quiz-result">
    <!-- 结果卡片 -->
    <div class="result-card">
      <div class="result-ring" :style="{ '--pct': score }">
        <div class="ring-inner">
          <span class="ring-score">{{ score }}</span>
          <span class="ring-label">得分</span>
        </div>
      </div>
      <div class="result-stats">
        <div class="stat-row">
          <span class="stat-dot correct-dot"></span>
          <span>正确 <strong>{{ correct }}</strong> 题</span>
        </div>
        <div class="stat-row">
          <span class="stat-dot wrong-dot"></span>
          <span>错误 <strong>{{ wrong }}</strong> 题</span>
        </div>
        <div class="stat-row">
          <span class="stat-dot empty-dot"></span>
          <span>未答 <strong>{{ unanswered }}</strong> 题</span>
        </div>
        <div class="stat-row">
          <span class="stat-dot"></span>
          <span>用时 <strong>{{ formatTime(elapsed) }}</strong></span>
        </div>
      </div>
    </div>

    <!-- 评价语 -->
    <div class="result-comment">
      <span class="comment-emoji">{{ commentEmoji }}</span>
      <span class="comment-text">{{ commentText }}</span>
    </div>

    <!-- 错题列表 -->
    <div v-if="wrongQuestions.length" class="wrong-list">
      <h3 class="wrong-title">错题回顾（{{ wrongQuestions.length }} 题）</h3>
      <div v-for="(item, i) in wrongQuestions" :key="i" class="wrong-item">
        <div class="wrong-stem">{{ item.question.stem }}</div>
        <div class="wrong-meta">
          <span class="type-badge">{{ QUESTION_TYPES[item.question.type]?.label }}</span>
          <span class="wrong-answer">你的答案：{{ item.userAnswer }}</span>
          <span class="right-answer">正确答案：{{ item.correctAnswer }}</span>
        </div>
        <div class="wrong-analysis">{{ item.question.analysis }}</div>
      </div>
    </div>

    <!-- 全部题目回顾 -->
    <div class="review-list">
      <h3 class="review-title">全部题目回顾</h3>
      <div
        v-for="(item, i) in allQuestions"
        :key="i"
        class="review-item"
        :class="item.status"
      >
        <span class="review-no">{{ i + 1 }}</span>
        <span class="review-stem">{{ item.question.stem.slice(0, 40) }}{{ item.question.stem.length > 40 ? '...' : '' }}</span>
        <span class="review-status">
          <template v-if="item.status === 'correct'">✅</template>
          <template v-else-if="item.status === 'wrong'">❌</template>
          <template v-else>⭕</template>
        </span>
      </div>
    </div>

    <!-- 操作 -->
    <div class="result-actions">
      <button class="action-btn primary" @click="$emit('retry')">🔄 重新练习</button>
      <button class="action-btn secondary" @click="$emit('reviewWrong')">📋 加入错题本</button>
      <button class="action-btn" @click="$emit('close')">返回列表</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { QUESTION_TYPES } from '@/constants/quiz'

const props = defineProps({
  score: { type: Number, default: 0 },
  correct: { type: Number, default: 0 },
  wrong: { type: Number, default: 0 },
  unanswered: { type: Number, default: 0 },
  total: { type: Number, default: 0 },
  elapsed: { type: Number, default: 0 },
  questions: { type: Array, default: () => [] },
  userAnswers: { type: Array, default: () => [] },
  submitted: { type: Array, default: () => [] },
})

defineEmits(['retry', 'reviewWrong', 'close'])

const wrongQuestions = computed(() => {
  return props.questions
    .map((q, i) => {
      const isRight = props.submitted[i] && arraysEqual((props.userAnswers[i] || []).slice().sort(), (q.answer || []).slice().sort())
      if (props.submitted[i] && !isRight) {
        return {
          question: q,
          userAnswer: formatUserAnswer(q, props.userAnswers[i]),
          correctAnswer: formatAnswer(q),
        }
      }
      return null
    })
    .filter(Boolean)
})

const allQuestions = computed(() => {
  return props.questions.map((q, i) => {
    let status = 'unanswered'
    if (props.submitted[i]) {
      status = arraysEqual((props.userAnswers[i] || []).slice().sort(), (q.answer || []).slice().sort()) ? 'correct' : 'wrong'
    }
    return { question: q, status }
  })
})

const commentEmoji = computed(() => {
  if (props.score >= 90) return '🎉'
  if (props.score >= 70) return '👍'
  if (props.score >= 50) return '💪'
  return '📚'
})

const commentText = computed(() => {
  if (props.score >= 90) return '太棒了！知识掌握非常扎实！'
  if (props.score >= 70) return '表现不错，继续巩固薄弱环节！'
  if (props.score >= 50) return '还需要加把劲，多做练习提升！'
  return '别灰心，错题是最宝贵的进步资源！'
})

function formatTime(sec) {
  const m = Math.floor(sec / 60)
  const s = sec % 60
  return `${m}分${s}秒`
}

function arraysEqual(a, b) {
  if (a.length !== b.length) return false
  return a.every((v, i) => v === b[i])
}

function formatAnswer(q) {
  if (q.type === 'truefalse') return q.answer[0] === 0 ? '正确' : '错误'
  if (q.type === 'fill') return '(见解析)'
  return q.answer.map(i => q.options[i]?.replace(/^[A-E]\.\s*/, '')).join('；')
}

function formatUserAnswer(q, arr) {
  if (!arr || !arr.length) return '未作答'
  if (q.type === 'fill') return arr[0]
  if (q.type === 'truefalse') return arr[0] === 0 ? '正确' : '错误'
  return arr.map(i => q.options[i]?.replace(/^[A-E]\.\s*/, '')).join('；')
}
</script>

<style lang="scss" scoped>
.quiz-result { padding: 20px 0; }
.result-card { display: flex; align-items: center; gap: 40px; background: #fff; padding: 32px; border-radius: $radius-xl; box-shadow: 0 2px 12px rgba(0,0,0,.04); margin-bottom: 16px; }
.result-ring {
  --pct: 0;
  width: 120px; height: 120px; border-radius: 50%; flex-shrink: 0;
  background: conic-gradient($color-primary calc(var(--pct) * 3.6deg), #eef1f5 0deg);
  display: flex; align-items: center; justify-content: center;
  .ring-inner {
    width: 90px; height: 90px; border-radius: 50%; background: #fff;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
  }
  .ring-score { font-size: 28px; font-weight: $font-weight-bold; color: $color-primary; }
  .ring-label { font-size: 11px; color: $color-text-tertiary; }
}
.result-stats { display: flex; flex-direction: column; gap: 10px; }
.stat-row { display: flex; align-items: center; gap: 8px; font-size: $font-size-sm; color: $color-text-secondary; }
.stat-dot { width: 8px; height: 8px; border-radius: 50%; background: #e0e0e0; }
.correct-dot { background: #4caf50; }
.wrong-dot { background: #f44336; }
.empty-dot { background: #bdbdbd; }
.result-comment { text-align: center; padding: 16px; background: #fff; border-radius: $radius-xl; margin-bottom: 16px; box-shadow: 0 2px 8px rgba(0,0,0,.03); }
.comment-emoji { font-size: 28px; display: block; margin-bottom: 6px; }
.comment-text { font-size: $font-size-sm; color: $color-text-secondary; }
.wrong-list { margin-bottom: 20px; }
.wrong-title { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 12px; }
.wrong-item { background: #fff; padding: 16px; border-radius: $radius-md; margin-bottom: 10px; border-left: 3px solid #f44336; box-shadow: 0 1px 6px rgba(0,0,0,.03); }
.wrong-stem { font-size: $font-size-sm; color: $color-text-primary; line-height: 1.6; margin-bottom: 8px; }
.wrong-meta { display: flex; gap: 16px; font-size: 11px; margin-bottom: 6px; }
.type-badge { padding: 1px 8px; background: #fce4ec; color: #c62828; border-radius: $radius-full; }
.wrong-answer { color: #f44336; }
.right-answer { color: #4caf50; }
.wrong-analysis { font-size: 11px; color: $color-text-tertiary; }
.review-list { margin-bottom: 24px; }
.review-title { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 12px; }
.review-item {
  display: flex; align-items: center; gap: 10px; padding: 10px 12px; background: #fff; border-radius: $radius-sm; margin-bottom: 4px;
  &.correct { background: #e8f5e9; }
  &.wrong { background: #ffebee; }
}
.review-no { width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; background: #f5f6f8; border-radius: $radius-sm; font-size: 11px; font-weight: $font-weight-medium; color: $color-text-muted; flex-shrink: 0; }
.review-stem { flex: 1; font-size: $font-size-xs; color: $color-text-secondary; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.review-status { font-size: 16px; }
.result-actions { display: flex; gap: 12px; justify-content: center; }
.action-btn {
  padding: 10px 28px; font-size: $font-size-sm; font-weight: $font-weight-medium;
  border: 1.5px solid #e0e0e0; background: #fff; border-radius: $radius-md; cursor: pointer; color: $color-text-secondary;
  &:hover { border-color: $color-primary; color: $color-primary; }
  &.primary { background: $color-primary; color: #fff; border-color: $color-primary; }
  &.secondary { background: #fff; color: $color-primary; border-color: $color-primary; }
}
</style>