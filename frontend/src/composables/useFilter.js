import { ref, computed } from 'vue'

/**
 * 通用过滤 composable
 */
export function useFilter(list, options = {}) {
  const { searchKey = 'name', filterKey = 'category' } = options

  const searchQuery = ref('')
  const activeFilter = ref('all')

  const filteredList = computed(() => {
    let result = list.value || list

    // 搜索过滤
    if (searchQuery.value.trim()) {
      const keyword = searchQuery.value.trim().toLowerCase()
      result = result.filter((item) =>
        item[searchKey].toLowerCase().includes(keyword)
      )
    }

    // 分类过滤
    if (activeFilter.value !== 'all') {
      result = result.filter((item) => item[filterKey] === activeFilter.value)
    }

    return result
  })

  return { searchQuery, activeFilter, filteredList }
}