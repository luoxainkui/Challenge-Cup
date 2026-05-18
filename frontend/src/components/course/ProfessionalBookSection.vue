<script setup>
import { computed } from 'vue'
import { PROFESSIONAL_BOOKS } from '@/constants/courses'

const props = defineProps({
  subjects: {
    type: Array,
    default: () => [],
  },
})

const books = computed(() => {
  return (props.subjects || [])
    .filter(s => PROFESSIONAL_BOOKS[s])
    .map(s => ({ subject: s, ...PROFESSIONAL_BOOKS[s] }))
})
</script>

<template>
  <div class="pro-book-section" v-if="books.length > 0">
    <div class="pro-book-header">
      <h3 class="pro-book-title">
        <span class="pro-book-icon">📘</span>
        配套专升本教材
      </h3>
      <p class="pro-book-subtitle">考纲同步 · 名师编著 · 正版授权</p>
    </div>
    <div class="pro-book-grid">
      <div v-for="book in books" :key="book.subject" class="pro-book-card">
        <div class="pro-book-cover-wrap">
          <img class="pro-book-cover" :src="book.cover" :alt="book.subject + '教材'" loading="lazy" />
        </div>
        <div class="pro-book-info">
          <span class="pro-book-subject">{{ book.subject }}</span>
          <span class="pro-book-price">{{ book.price }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.pro-book-section {
  max-width: $max-width;
  margin: 48px auto;
  padding: 32px 24px;
  background: #fafbfc;
  border-radius: $radius-6xl;
  border: 1px solid #edf0f5;
}

.pro-book-header {
  text-align: center;
  margin-bottom: 28px;
}

.pro-book-title {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  margin-bottom: 6px;
}

.pro-book-icon {
  font-size: 22px;
}

.pro-book-subtitle {
  font-size: $font-size-xs;
  color: $color-text-muted;
}

.pro-book-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.pro-book-card {
  width: 150px;
  background: #fff;
  border-radius: $radius-xl;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.06);
  overflow: hidden;
  transition: all $transition-base;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
  }
}

.pro-book-cover-wrap {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f5f5f5;
  overflow: hidden;
}

.pro-book-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.pro-book-info {
  padding: 10px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.pro-book-subject {
  font-size: $font-size-sm;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.pro-book-price {
  font-size: $font-size-sm;
  font-weight: $font-weight-bold;
  color: $color-accent;
}

/* Responsive */
@include respond-to('tablet') {
  .pro-book-grid {
    gap: 14px;
  }
  .pro-book-card {
    width: 130px;
  }
  .pro-book-cover-wrap {
    height: 155px;
  }
}

@include respond-to('mobile') {
  .pro-book-section {
    margin: 32px 12px;
    padding: 24px 16px;
  }
  .pro-book-grid {
    gap: 10px;
  }
  .pro-book-card {
    width: 110px;
  }
  .pro-book-cover-wrap {
    height: 135px;
  }
}
</style>