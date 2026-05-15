<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="service-hero">
      <span class="service-hero-icon">📚</span>
      <h1 class="service-hero-title">精讲课程</h1>
      <p class="service-hero-desc">覆盖公共课及专业课，由一线名师倾心打造，聚焦广西专升本考纲考点，系统梳理知识框架。</p>
    </div>

    <!-- 筛选栏 -->
    <div class="filter-bar">
      <div class="filter-group">
        <span class="filter-label">类别：</span>
        <button
          v-for="cat in COURSE_CATEGORIES"
          :key="cat.value"
          :class="['filter-tag', { active: activeCategory === cat.value }]"
          @click="setCategory(cat.value)"
        >{{ cat.label }}</button>
      </div>
      <div class="search-box">
        <input
          v-model="searchKeyword"
          type="text"
          class="search-input"
          placeholder="搜索课程..."
          @input="onSearchChange"
        />
        <button class="search-btn">🔍</button>
      </div>
    </div>

    <!-- 课程列表（每页4门） -->
    <div class="course-grid">
      <div v-for="course in pagedCourses" :key="course.id" class="course-card">
        <div class="course-card-img" :style="{ background: course.color }">
          <span class="course-card-subject">{{ course.subject }}</span>
          <span class="course-card-badge" v-if="course.hot">热门</span>
        </div>
        <div class="course-card-body">
          <span class="course-tag">{{ course.category }}</span>
          <h3 class="course-name">{{ course.name }}</h3>
          <p class="course-desc">{{ course.desc }}</p>
          <div class="course-meta">
            <div class="course-teacher">
              <span class="teacher-dot"></span>
              <span>{{ course.teacher }}</span>
            </div>
            <div class="course-stats">
              <span class="stat-item">👥 {{ course.students }}</span>
              <span class="stat-item">⭐ {{ course.rating }}</span>
            </div>
          </div>
          <div class="course-footer">
            <span class="course-price">¥{{ course.price }}</span>
            <button class="course-btn" @click="goToCourseDetail(course)">立即报名</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 分页 -->
    <PaginationBar
      :current-page="currentPage"
      :total-pages="totalPages"
      @change="goToPage"
    />

    <!-- AI 智能推荐 -->
    <AiRecommend />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { COURSE_CATEGORIES } from '@/constants/courses'
import { useCourseFilter } from '@/composables/useCourseFilter'
import PaginationBar from '@/components/course/PaginationBar.vue'
import AiRecommend from '@/components/course/AiRecommend.vue'

const router = useRouter()

const {
  searchKeyword,
  activeCategory,
  currentPage,
  totalPages,
  pagedCourses,
  goToPage,
  setCategory,
  onSearchChange,
} = useCourseFilter()

const goToCourseDetail = (course) => {
  router.push({ name: 'courses', query: { id: course.id } })
}
</script>

<style lang="scss" scoped>
.page-container {
  min-height: 100vh;
  background: #f8f9fb;
}

/* Hero */
.service-hero {
  padding: 100px 0 32px;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  .service-hero-icon { font-size: 48px; display: block; margin-bottom: 12px; }
  .service-hero-title { font-size: $font-size-4xl; font-weight: $font-weight-bold; margin-bottom: 8px; }
  .service-hero-desc { opacity: .85; font-size: $font-size-md; max-width: 640px; margin: 0 auto; }
}

/* Filter Bar */
.filter-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  padding: 20px 0;
  background: #fff;
  border-bottom: 1px solid #edf0f5;
  position: sticky;
  top: 64px;
  z-index: 10;
  flex-wrap: wrap;
}

.filter-group { display: flex; align-items: center; gap: 8px; }
.filter-label { font-size: $font-size-sm; color: $color-text-secondary; font-weight: $font-weight-medium; }

.filter-tag {
  padding: 6px 20px;
  border: 1.5px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-full;
  font-size: $font-size-xs;
  color: $color-text-tertiary;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover { border-color: $color-primary; color: $color-primary; }
  &.active { background: $color-primary; color: #fff; border-color: $color-primary; }
}

.search-box {
  display: flex; align-items: center;
  border: 1.5px solid #e0e4ea;
  border-radius: $radius-full;
  overflow: hidden; background: #fff;
  transition: border-color $transition-fast;
  &:focus-within { border-color: $color-primary; }
}
.search-input {
  border: none; outline: none;
  padding: 8px 16px; font-size: $font-size-sm;
  width: 200px; color: $color-text-primary;
}
.search-btn {
  border: none; background: $color-primary; color: #fff;
  padding: 8px 16px; cursor: pointer; font-size: $font-size-sm;
}

/* Course Grid */
.course-grid {
  max-width: $max-width; margin: 0 auto; padding: 32px 20px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

.course-card {
  background: #fff; border-radius: $radius-xl; overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, .06);
  transition: all $transition-base;
  &:hover { transform: translateY(-4px); box-shadow: 0 8px 28px rgba(0, 0, 0, .1); }
}
.course-card-img {
  height: 100px; display: flex; align-items: flex-end; justify-content: space-between;
  padding: 10px 16px; position: relative;
}
.course-card-subject {
  color: rgba(255, 255, 255, .9); font-weight: $font-weight-semibold;
  font-size: $font-size-sm; text-shadow: 0 1px 3px rgba(0, 0, 0, .2);
}
.course-card-badge {
  position: absolute; top: 10px; right: 10px;
  background: rgba(255, 59, 48, .9); color: #fff;
  padding: 2px 10px; border-radius: $radius-full; font-size: 11px; font-weight: $font-weight-medium;
}
.course-card-body { padding: 16px; }
.course-tag {
  display: inline-block; padding: 2px 10px;
  background: #f0f3ff; color: $color-primary;
  border-radius: $radius-full; font-size: 11px; margin-bottom: 8px;
}
.course-name { font-size: $font-size-base; font-weight: $font-weight-bold; color: $color-text-primary; margin-bottom: 6px; line-height: 1.4; }
.course-desc {
  font-size: $font-size-xs; color: $color-text-quaternary; line-height: 1.5; margin-bottom: 12px;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.course-meta { display: flex; justify-content: space-between; align-items: center; font-size: $font-size-xs; color: $color-text-tertiary; margin-bottom: 12px; }
.course-teacher { display: flex; align-items: center; gap: 4px; }
.teacher-dot { width: 6px; height: 6px; border-radius: 50%; background: $color-primary; }
.course-stats { display: flex; gap: 10px; }
.stat-item { color: $color-text-muted; }
.course-footer { display: flex; justify-content: space-between; align-items: center; padding-top: 10px; border-top: 1px solid #f0f0f0; }
.course-price { font-size: $font-size-md; font-weight: $font-weight-bold; color: $color-accent; }
.course-btn {
  padding: 6px 16px; background: $color-primary; color: #fff; border: none;
  border-radius: $radius-md; font-size: $font-size-xs; font-weight: $font-weight-medium;
  cursor: pointer; transition: all $transition-fast;
  &:hover { background: $color-primary-dark; }
}

/* Responsive */
@include respond-to('desktop') {
  .course-grid { grid-template-columns: repeat(3, 1fr); }
}
@include respond-to('tablet') {
  .course-grid { grid-template-columns: repeat(2, 1fr); }
}
@include respond-to('mobile') {
  .course-grid { grid-template-columns: 1fr; }
  .filter-bar { flex-direction: column; gap: 12px; }
}
</style>