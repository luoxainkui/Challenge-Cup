import { ref, computed } from 'vue'
import { COURSES, TOPICS_MAP } from '@/constants/courses'

export function useCoursePlayer() {
  const currentCourse = ref(COURSES[0])
  const activeChapterIdx = ref(0)
  const isPlaying = ref(false)
  const showPayment = ref(false)

  const chapters = computed(() => {
    if (!currentCourse.value) return []
    const names = TOPICS_MAP[currentCourse.value.subject] || []
    return names.map((title, i) => ({
      title,
      duration: `${15 + i * 5}分钟`,
      done: i < 2,
    }))
  })

  const activeChapter = computed(() => {
    if (!chapters.value.length) return null
    return chapters.value[activeChapterIdx.value] || null
  })

  function switchCourse(course) {
    currentCourse.value = course
    activeChapterIdx.value = 0
    isPlaying.value = false
  }

  function playChapter(idx) {
    activeChapterIdx.value = idx
    isPlaying.value = true
  }

  function togglePlay() {
    if (activeChapter.value) {
      isPlaying.value = !isPlaying.value
    }
  }

  function handleEnroll(course) {
    if (course.price === 0) {
      currentCourse.value = course
    } else {
      showPayment.value = true
    }
  }

  return {
    currentCourse,
    activeChapterIdx,
    isPlaying,
    showPayment,
    chapters,
    activeChapter,
    switchCourse,
    playChapter,
    togglePlay,
    handleEnroll,
  }
}