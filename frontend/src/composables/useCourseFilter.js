import { ref, computed } from 'vue'
import { COURSES } from '@/constants/courses'

const PAGE_SIZE = 4

export function useCourseFilter() {
  const searchKeyword = ref('')
  const activeCategory = ref('all')
  const currentPage = ref(1)

  const filteredCourses = computed(() => {
    let result = COURSES
    if (activeCategory.value !== 'all') {
      result = result.filter(c => {
        if (activeCategory.value === 'public') return c.category === '公共课'
        if (activeCategory.value === 'major') return c.category === '专业课'
        return true
      })
    }
    if (searchKeyword.value.trim()) {
      const kw = searchKeyword.value.trim().toLowerCase()
      result = result.filter(c =>
        c.name.toLowerCase().includes(kw) ||
        c.subject.toLowerCase().includes(kw) ||
        c.teacher.toLowerCase().includes(kw)
      )
    }
    return result
  })

  const totalPages = computed(() =>
    Math.ceil(filteredCourses.value.length / PAGE_SIZE)
  )

  const pagedCourses = computed(() => {
    const start = (currentPage.value - 1) * PAGE_SIZE
    return filteredCourses.value.slice(start, start + PAGE_SIZE)
  })

  const goToPage = (page) => {
    const p = Number(page)
    if (p >= 1 && p <= totalPages.value) {
      currentPage.value = p
    }
  }

  // reset page when filter changes
  const setCategory = (cat) => {
    activeCategory.value = cat
    currentPage.value = 1
  }

  const onSearchChange = () => {
    currentPage.value = 1
  }

  return {
    searchKeyword,
    activeCategory,
    currentPage,
    filteredCourses,
    totalPages,
    pagedCourses,
    goToPage,
    setCategory,
    onSearchChange,
  }
}