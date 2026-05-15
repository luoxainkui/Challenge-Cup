import { ref, computed, watch } from 'vue'
import { SAMPLE_QUESTIONS, EXAM_POINTS, ALL_QUESTIONS, QUIZ_SUBJECTS, INITIAL_MISTAKES } from '@/constants/quiz'

const STORAGE_KEY = 'quiz_mistake_book'
const STORAGE_KEY_SETTINGS = 'quiz_mistake_settings'

function loadMistakes() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : [...INITIAL_MISTAKES]
  } catch { return [...INITIAL_MISTAKES] }
}

function saveMistakes(list) { localStorage.setItem(STORAGE_KEY, JSON.stringify(list)) }

export function useMistakeBook() {
  // ---- 自动移除设置 ----
  const autoRemoveEnabled = ref(loadSettings().autoRemove ?? true)
  const autoRemoveThreshold = ref(loadSettings().autoRemoveThreshold ?? 3)

  function loadSettings() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY_SETTINGS)
      return raw ? JSON.parse(raw) : {}
    } catch { return {} }
  }
  function persistSettings() {
    localStorage.setItem(STORAGE_KEY_SETTINGS, JSON.stringify({
      autoRemove: autoRemoveEnabled.value,
      autoRemoveThreshold: autoRemoveThreshold.value,
    }))
  }
  watch([autoRemoveEnabled, autoRemoveThreshold], persistSettings, { deep: true })

  // ---- 错题表 ----
  const mistakes = ref(loadMistakes())
  watch(mistakes, (v) => saveMistakes(v), { deep: true })

  // ---- 统计 ----
  const totalQuestions = SAMPLE_QUESTIONS.length
  const mistakeList = computed(() => mistakes.value.map(m => {
    const q = SAMPLE_QUESTIONS.find(q => q.id === m.questionId)
    const point = EXAM_POINTS.find(p => p.id === q?.pointId)
    return { ...m, question: q, point }
  }).filter(m => m.question))
  const mistakeCount = computed(() => mistakeList.value.length)
  const mistakeRate = computed(() => totalQuestions ? Math.round(mistakeCount.value / totalQuestions * 100) : 0)
  const masteryRate = computed(() => totalQuestions ? Math.round((totalQuestions - mistakeCount.value) / totalQuestions * 100) : 100)

  // ---- 考点分布 ----
  const pointDistribution = computed(() => {
    const map = {}
    mistakeList.value.forEach(m => {
      if (!m.point) return
      const key = m.point.id
      if (!map[key]) map[key] = { point: m.point, count: 0 }
      map[key].count++
    })
    return Object.values(map).sort((a, b) => b.count - a.count)
  })
  const maxPointCount = computed(() => pointDistribution.value.length ? Math.max(...pointDistribution.value.map(p => p.count)) : 1)

  // ---- 科目分布（柱状图） ----
  const TYPE_LABELS = { single: '单选题', multi: '多选题', truefalse: '判断题', fill: '填空题' }
  const subjectDistribution = computed(() => {
    const map = {}
    mistakeList.value.forEach(m => {
      if (!m.point || !m.point.subject) return
      const subj = m.point.subject
      if (!map[subj]) {
        const subjectInfo = QUIZ_SUBJECTS.find(s => s.name === subj)
        map[subj] = { subject: subj, count: 0, color: subjectInfo?.color || '#2a6eff' }
      }
      map[subj].count++
    })
    return Object.values(map).sort((a, b) => b.count - a.count)
  })
  const subjectMax = computed(() => subjectDistribution.value.length ? Math.max(...subjectDistribution.value.map(s => s.count)) : 1)

  // ---- 题型分布（柱状图） ----
  const typeDistribution = computed(() => {
    const map = {}
    mistakeList.value.forEach(m => {
      const q = m.question
      if (!q || !q.type) return
      if (!map[q.type]) map[q.type] = { type: q.type, label: TYPE_LABELS[q.type] || q.type, count: 0 }
      map[q.type].count++
    })
    return Object.values(map).sort((a, b) => b.count - a.count)
  })
  const typeMax = computed(() => typeDistribution.value.length ? Math.max(...typeDistribution.value.map(t => t.count)) : 1)

  // ---- 记录答错 ----
  function recordWrong(questionId) {
    const idx = mistakes.value.findIndex(m => m.questionId === questionId)
    const today = new Date().toISOString().slice(0, 10)
    if (idx >= 0) {
      mistakes.value[idx].wrongCount++
      mistakes.value[idx].lastWrongAt = today
    } else {
      mistakes.value.push({ questionId, wrongCount: 1, correctCount: 0, lastWrongAt: today })
    }
  }

  // ---- 记录答对 ----
  function recordCorrect(questionId) {
    const idx = mistakes.value.findIndex(m => m.questionId === questionId)
    if (idx < 0) return
    mistakes.value[idx].correctCount++
    // 检查自动移除
    if (autoRemoveEnabled.value && mistakes.value[idx].correctCount >= autoRemoveThreshold.value) {
      mistakes.value.splice(idx, 1)
    }
  }

  // ---- 手动移除 ----
  function removeMistake(questionId) {
    const idx = mistakes.value.findIndex(m => m.questionId === questionId)
    if (idx >= 0) mistakes.value.splice(idx, 1)
  }

  // ---- 清空 ----
  function clearAll() { mistakes.value = [] }

  return {
    autoRemoveEnabled,
    autoRemoveThreshold,
    mistakes,
    mistakeList,
    totalQuestions,
    mistakeCount,
    mistakeRate,
    masteryRate,
    pointDistribution,
    maxPointCount,
    subjectDistribution,
    subjectMax,
    typeDistribution,
    typeMax,
    recordWrong,
    recordCorrect,
    removeMistake,
    clearAll,
  }
}