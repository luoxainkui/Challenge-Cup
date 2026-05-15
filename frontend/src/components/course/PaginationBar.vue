<template>
  <div class="pagination" v-if="totalPages > 1">
    <button
      class="page-btn"
      :class="{ disabled: currentPage === 1 }"
      :disabled="currentPage === 1"
      @click="$emit('change', currentPage - 1)"
    >上一页</button>
    <button
      v-for="p in displayPages"
      :key="p"
      class="page-btn"
      :class="{ active: p === currentPage }"
      :disabled="p === '...'"
      @click="p !== '...' && p !== currentPage && $emit('change', p)"
    >{{ p }}</button>
    <button
      class="page-btn"
      :class="{ disabled: currentPage === totalPages }"
      :disabled="currentPage === totalPages"
      @click="$emit('change', currentPage + 1)"
    >下一页</button>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  currentPage: { type: Number, required: true },
  totalPages: { type: Number, required: true },
})

defineEmits(['change'])

const displayPages = computed(() => {
  const pages = []
  const total = props.totalPages
  const current = props.currentPage
  const maxShow = 5

  if (total <= maxShow) {
    for (let i = 1; i <= total; i++) pages.push(i)
  } else {
    pages.push(1)
    const start = Math.max(2, current - 1)
    const end = Math.min(total - 1, current + 1)
    if (start > 2) pages.push('...')
    for (let i = start; i <= end; i++) pages.push(i)
    if (end < total - 1) pages.push('...')
    pages.push(total)
  }
  return pages
})
</script>

<style lang="scss" scoped>
.pagination {
  display: flex;
  justify-content: center;
  gap: 8px;
  padding: 24px 0 48px;
}

.page-btn {
  width: 40px;
  height: 40px;
  border: 1.5px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-md;
  font-size: $font-size-sm;
  color: $color-text-secondary;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover:not(.disabled) {
    border-color: $color-primary;
    color: $color-primary;
  }
  &.active {
    background: $color-primary;
    color: #fff;
    border-color: $color-primary;
  }
  &.disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
}
</style>