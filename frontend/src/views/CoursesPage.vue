<template>
  <div class="courses-page">
    <section class="courses-hero">
      <h1>课程中心</h1>
      <p>精选优质课程，助你高效备考</p>
    </section>

    <section class="courses-body">
      <!-- 搜索 -->
      <div class="courses-toolbar">
        <input v-model="searchQuery" type="text" class="search-input" placeholder="搜索课程名称..." />
        <div class="filter-tabs">
          <button
            v-for="cat in categories"
            :key="cat"
            :class="{ active: activeFilter === cat }"
            @click="activeFilter = cat"
          >
            {{ cat === 'all' ? '全部' : cat }}
          </button>
        </div>
      </div>

      <!-- 课程列表 -->
      <div class="course-grid">
        <div class="course-card" v-for="course in filteredList" :key="course.id" @click="goDetail(course.id)">
          <div class="course-cover" :style="{ background: course.color }">
            <span class="course-subject">{{ course.subject }}</span>
          </div>
          <div class="course-info">
            <h3>{{ course.name }}</h3>
            <p class="course-desc">{{ course.desc }}</p>
            <div class="course-meta">
              <span>{{ course.duration }}</span>
              <span class="dot">·</span>
              <span>{{ course.lessons }}课时</span>
            </div>
            <div class="course-footer">
              <span class="course-price">{{ course.price === 0 ? '免费' : '¥' + course.price }}</span>
              <span class="course-btn">查看详情</span>
            </div>
          </div>
        </div>
      </div>

      <div v-if="filteredList.length === 0" class="empty-state">
        暂无匹配课程，请调整筛选条件
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { COURSES } from '@/constants/courses'

const router = useRouter()
const searchQuery = ref('')
const activeFilter = ref('all')

const categories = computed(() => {
  const cats = new Set(COURSES.map((c) => c.category))
  return ['all', ...cats]
})

const filteredList = computed(() => {
  let result = COURSES
  if (searchQuery.value.trim()) {
    const kw = searchQuery.value.trim().toLowerCase()
    result = result.filter((c) => c.name.toLowerCase().includes(kw))
  }
  if (activeFilter.value !== 'all') {
    result = result.filter((c) => c.category === activeFilter.value)
  }
  return result
})

function goDetail(id) {
  router.push(`/courses/${id}`)
}
</script>

<style lang="scss" scoped>
.courses-hero {
  padding: 100px 0 40px;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  h1 {
    font-size: $font-size-4xl;
    margin-bottom: 8px;
  }
  p {
    opacity: 0.85;
    font-size: $font-size-md;
  }
}

.courses-body {
  width: $max-width;
  margin: 0 auto;
  padding: 40px 0 80px;
}

.courses-toolbar {
  margin-bottom: 32px;
}

.search-input {
  width: 100%;
  max-width: 400px;
  padding: 12px 20px;
  border: 2px solid #eee;
  border-radius: $radius-full;
  font-size: $font-size-base;
  outline: none;
  transition: border-color $transition-fast;
  margin-bottom: 16px;

  &:focus {
    border-color: $color-primary;
  }
}

.filter-tabs {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;

  button {
    padding: 8px 20px;
    border-radius: $radius-full;
    border: 2px solid #eee;
    background: #fff;
    cursor: pointer;
    font-size: $font-size-base;
    transition: all $transition-fast;

    &:hover {
      border-color: $color-primary;
      color: $color-primary;
    }

    &.active {
      background: $color-primary;
      border-color: $color-primary;
      color: #fff;
    }
  }
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.course-card {
  background: #fff;
  border-radius: $radius-xl;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.06);
  transition: all $transition-base;
  cursor: pointer;

  &:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.1);
  }
}

.course-cover {
  height: 160px;
  display: flex;
  align-items: flex-end;
  padding: 16px;
}

.course-subject {
  background: rgba(255, 255, 255, 0.25);
  color: #fff;
  padding: 4px 12px;
  border-radius: $radius-full;
  font-size: $font-size-xs;
}

.course-info {
  padding: 20px;

  h3 {
    font-size: $font-size-lg;
    margin-bottom: 8px;
  }
}

.course-desc {
  font-size: $font-size-sm;
  color: $color-text-quaternary;
  line-height: 1.5;
  margin-bottom: 12px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.course-meta {
  font-size: $font-size-xs;
  color: $color-text-tertiary;
  margin-bottom: 16px;

  .dot {
    margin: 0 6px;
  }
}

.course-footer {
  @include flex-between;
}

.course-price {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
  color: $color-accent;
}

.course-btn {
  color: $color-primary;
  font-size: $font-size-sm;
  font-weight: $font-weight-medium;
}

.empty-state {
  text-align: center;
  padding: 60px 0;
  color: $color-text-tertiary;
  font-size: $font-size-md;
}

@include respond-to('desktop') {
  .courses-body {
    width: 100%;
    padding-left: 20px;
    padding-right: 20px;
  }
}

@include respond-to('tablet') {
  .course-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@include respond-to('mobile') {
  .course-grid {
    grid-template-columns: 1fr;
  }
}
</style>