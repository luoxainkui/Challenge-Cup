import { ref, computed, watch } from 'vue'
import { ALL_QUESTIONS, QUESTION_TYPES } from '@/constants/quiz'

/**
 * 练题引擎
 * @param {'single'|'multi'|'truefalse'|'fill'} filterType - 按类型筛选，不传则全部
 * @param {number} pageSize - 每页题数
 */
export function useQuiz(filterType, pageSize = 5) {
  // 按类型筛选
  const pool = filterType
    ? ALL_QUESTIONS.filter(q => q.type === filterType)
    : ALL_QUESTIONS

  const questions = ref([...pool]) // 可打乱
  const currentIndex = ref(0)
  const userAnswers = ref([])       // 每题用户选中的索引数组
  const submitted = ref([])         // 每题是否已提交
  const startTime = ref(Date.now())

  // ---- 当前题目 ----
  const currentQuestion = computed(() => questions.value[currentIndex.value] || null)
  const totalCount = computed(() => questions.value.length)
  const isLast = computed(() => currentIndex.value >= totalCount.value - 1)
  const isFirst = computed(() => currentIndex.value <= 0)
  const progress = computed(() => totalCount.value ? Math.round((currentIndex.value + 1) / totalCount.value * 100) : 0)

  // ---- 初始化作答 ----
  function ensureAnswerSlot(index) {
    if (!userAnswers.value[index]) {
      userAnswers.value[index] = []
    }
  }

  // ---- 单选 / 填空 / 判断 ----
  function selectOption(optIndex) {
    ensureAnswerSlot(currentIndex.value)
    const q = currentQuestion.value
    if (!q) return
    if (q.type === 'multi') {
      const arr = userAnswers.value[currentIndex.value]
      const pos = arr.indexOf(optIndex)
      if (pos >= 0) arr.splice(pos, 1)
      else arr.push(optIndex)
    } else {
      userAnswers.value[currentIndex.value] = [optIndex]
    }
  }

  // 填空输入
  function setFillAnswer(val) {
    ensureAnswerSlot(currentIndex.value)
    userAnswers.value[currentIndex.value] = val ? [val] : []
  }

  function isSelected(optIndex) {
    const arr = userAnswers.value[currentIndex.value]
    return arr ? arr.includes(optIndex) : false
  }

  // ---- 提交当前题 ----
  function submitCurrent() {
    ensureAnswerSlot(currentIndex.value)
    if (userAnswers.value[currentIndex.value].length === 0) return false
    submitted.value[currentIndex.value] = true

    // 同步错题本
    const q = currentQuestion.value
    if (q) {
      const correct = checkAnswer(currentIndex.value)
      if (correct) {
        onCorrectCb?.(q.id)
      } else {
        onWrongCb?.(q.id)
      }
    }
    return true
  }

  // ---- 判题 ----
  function checkAnswer(index) {
    const q = questions.value[index]
    if (!q) return false
    const user = userAnswers.value[index] || []
    const ans = q.answer || []
    if (user.length !== ans.length) return false
    return user.slice().sort().every((v, i) => v === ans.slice().sort()[i])
  }

  function isCorrect(index) {
    if (!submitted.value[index]) return null
    return checkAnswer(index)
  }

  // ---- 导航 ----
  function next() { if (!isLast.value) currentIndex.value++ }
  function prev() { if (!isFirst.value) currentIndex.value-- }
  function jumpTo(index) { if (index >= 0 && index < totalCount.value) currentIndex.value = index }

  // ---- 统计 ----
  const stats = computed(() => {
    let correct = 0, wrong = 0, unanswered = 0
    for (let i = 0; i < totalCount.value; i++) {
      if (!submitted.value[i]) { unanswered++; continue }
      isCorrect(i) ? correct++ : wrong++
    }
    return { correct, wrong, unanswered, total: totalCount.value, score: totalCount.value ? Math.round(correct / totalCount.value * 100) : 0 }
  })

  const elapsed = computed(() => Math.floor((Date.now() - startTime.value) / 1000))

  // ---- 打乱题目 ----
  function shuffle() {
    const arr = [...questions.value]
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      ;[arr[i], arr[j]] = [arr[j], arr[i]]
    }
    questions.value = arr
    reset()
  }

  // ---- 重置 ----
  function reset() {
    currentIndex.value = 0
    userAnswers.value = []
    submitted.value = []
    startTime.value = Date.now()
  }

  // ---- 错题回调 ----
  let onCorrectCb = null, onWrongCb = null
  function bindMistakeCallbacks(correctFn, wrongFn) {
    onCorrectCb = correctFn
    onWrongCb = wrongFn
  }

  // ---- 题目列表（用于答题卡跳转） ----
  const questionList = computed(() => questions.value.map((q, i) => ({
    index: i,
    type: q.type,
    typeLabel: QUESTION_TYPES[q.type]?.label || '',
    submitted: !!submitted.value[i],
    correct: isCorrect(i),
  })))

  return {
    questions,
    currentIndex,
    currentQuestion,
    totalCount,
    isLast,
    isFirst,
    progress,
    userAnswers,
    submitted,
    stats,
    elapsed,
    selectOption,
    setFillAnswer,
    isSelected,
    submitCurrent,
    checkAnswer,
    isCorrect,
    next,
    prev,
    jumpTo,
    shuffle,
    reset,
    bindMistakeCallbacks,
    questionList,
  }
}