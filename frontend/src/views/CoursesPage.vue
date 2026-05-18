<template>
  <div class="courses-page">
    <!-- Hero -->
    <section class="courses-hero">
      <h1>课程中心</h1>
      <p>精选优质课程，助你高效备考</p>
    </section>

    <!-- ========== 首屏：一级学科大类卡片 ========== -->
    <template v-if="stage === 'categories'">
      <section class="category-grid-section">
        <div class="category-grid">
          <SubjectCategoryCard
            v-for="cat in SUBJECT_CATEGORIES"
            :key="cat.key"
            :category="cat"
            :courseCount="getCourseCount(cat)"
            @select="selectCategory"
          />
        </div>
      </section>
    </template>

    <!-- ========== 二级：学科课程列表 ========== -->
    <template v-if="stage === 'list'">
      <!-- 返回按钮 + 标题 -->
      <div class="list-header">
        <button class="list-back-btn" @click="stage = 'categories'">
          ← 返回全部学科
        </button>
        <div class="list-header-title">
          <span class="list-header-icon">{{ currentCategory.icon }}</span>
          <h2>{{ currentCategory.name }} · 课程列表</h2>
          <span class="list-header-badge">{{ currentCourses.length }} 门课程</span>
        </div>
        <!-- 搜索框 -->
        <div class="list-search">
          <input
            v-model="searchKeyword"
            type="text"
            placeholder="搜索课程名称..."
            class="list-search-input"
            @input="currentPage = 1"
          />
        </div>
      </div>

      <!-- 课程卡片列表 -->
      <section class="courses-grid-section">
        <div class="course-grid">
          <CourseCard
            v-for="c in pagedCourses"
            :key="c.id"
            :course="c"
            @click="goToCourse"
          />
        </div>
        <div class="empty-state" v-if="pagedCourses.length === 0">
          <p>暂无相关课程</p>
        </div>
      </section>

      <!-- 分页 -->
      <PaginationBar
        v-if="totalPages > 1"
        :current-page="currentPage"
        :total-pages="totalPages"
        @change="currentPage = $event"
      />

      <!-- 专业课教材配图区域 -->
      <ProfessionalBookSection
        v-if="currentCategory.key === 'zhuanyeke'"
        :subjects="currentCategory.subjects"
      />
    </template>

    <!-- ========== 课程详情弹层（保持原样） ========== -->
    <div class="course-overlay" v-if="selectedCourse" @click.self="selectedCourse = null">
      <div class="course-detail-panel">
        <button class="close-btn" @click="selectedCourse = null">✕</button>
        <CourseTabs
          :currentCourse="selectedCourse"
          @switch="switchCourse"
        />
        <section class="courses-main">
          <ChapterDirectory
            :chapters="chapters"
            :activeIdx="activeChapterIdx"
            @play="playChapter"
          />
          <main class="video-panel">
            <VideoPlayer
              :course="selectedCourse"
              :isPlaying="isPlaying"
              :activeChapter="activeChapter"
              :activeIdx="activeChapterIdx"
              @toggle="togglePlay"
            />
            <CourseDetail
              :course="selectedCourse"
              @enroll="handleEnroll"
            />
          </main>
        </section>
      </div>
    </div>

    <PaymentModal
      :show="showPayment"
      :course="selectedCourse"
      @close="showPayment = false"
      @success="onPaySuccess"
    />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { COURSES, SUBJECT_CATEGORIES } from '@/constants/courses'
import { useCoursePlayer } from '@/composables/useCoursePlayer'
import SubjectCategoryCard from '@/components/course/SubjectCategoryCard.vue'
import CourseCard from '@/components/course/CourseCard.vue'
import CourseTabs from '@/components/course/CourseTabs.vue'
import ChapterDirectory from '@/components/course/ChapterDirectory.vue'
import VideoPlayer from '@/components/course/VideoPlayer.vue'
import CourseDetail from '@/components/course/CourseDetail.vue'
import PaymentModal from '@/components/course/PaymentModal.vue'
import PaginationBar from '@/components/course/PaginationBar.vue'
import ProfessionalBookSection from '@/components/course/ProfessionalBookSection.vue'

const PAGE_SIZE = 4

// 阶段：categories（首屏大类）| list（课程列表）
const stage = ref('categories')
const currentCategory = ref(null)
const selectedCourse = ref(null)
const searchKeyword = ref('')
const currentPage = ref(1)

/** 当前学科大类下的所有课程 */
const currentCourses = computed(() => {
  if (!currentCategory.value) return []
  const subjects = currentCategory.value.subjects || []
  let result = COURSES.filter(c => subjects.includes(c.subject))
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

/** 分页后的课程 */
const pagedCourses = computed(() => {
  const start = (currentPage.value - 1) * PAGE_SIZE
  return currentCourses.value.slice(start, start + PAGE_SIZE)
})

/** 总页数 */
const totalPages = computed(() =>
  Math.ceil(currentCourses.value.length / PAGE_SIZE)
)

/** 统计某个大类下的课程数 */
function getCourseCount(cat) {
  return COURSES.filter(c => (cat.subjects || []).includes(c.subject)).length
}

/** 点击学科大类 → 进入课程列表 */
function selectCategory(cat) {
  currentCategory.value = cat
  currentPage.value = 1
  searchKeyword.value = ''
  stage.value = 'list'
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

const {
  activeChapterIdx,
  isPlaying,
  showPayment,
  chapters,
  activeChapter,
  switchCourse,
  playChapter,
  togglePlay,
  handleEnroll,
} = useCoursePlayer()

/** watch 停止函数 */
let stopDetailWatcher = null

/** 点击课程卡片 → 打开详情弹层 */
function goToCourse(course) {
  selectedCourse.value = course
  switchCourse(course)
  document.body.style.overflow = 'hidden'
  // 关闭弹层时恢复滚动
  stopDetailWatcher = watch(selectedCourse, (v) => {
    if (!v) {
      document.body.style.overflow = ''
    }
  })
}

onUnmounted(() => {
  if (stopDetailWatcher) stopDetailWatcher()
})

function onPaySuccess(course) {
  showPayment.value = false
  console.log('支付成功:', course.name)
}

// 从精讲课程跳转过来时自动选中课程
const route = useRoute()
onMounted(() => {
  const courseId = route.query.id
  if (courseId) {
    const course = COURSES.find(c => c.id === Number(courseId))
    if (course) {
      // 找到该课程所属学科大类
      const cat = SUBJECT_CATEGORIES.find(c =>
        (c.subjects || []).includes(course.subject)
      )
      if (cat) {
        currentCategory.value = cat
        stage.value = 'list'
      }
      selectedCourse.value = course
      switchCourse(course)
    }
  }
})
</script>

<style lang="scss" scoped>
.courses-page {
  min-height: 100vh;
  background: #f8f9fb;
}

.courses-hero {
  padding: 100px 0 32px;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  h1 {
    font-size: $font-size-4xl;
    font-weight: $font-weight-bold;
    margin-bottom: 8px;
  }
  p {
    opacity: 0.85;
    font-size: $font-size-md;
  }
}

// ===== 一级学科大类卡片网格 =====
.category-grid-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 40px 20px 60px;
}

.category-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 24px;
}

// ===== 二级课程列表头部 =====
.list-header {
  max-width: $max-width;
  margin: 0 auto;
  padding: 28px 20px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
}

.list-back-btn {
  padding: 8px 20px;
  border: 1.5px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  color: $color-text-secondary;
  cursor: pointer;
  transition: all $transition-fast;
  white-space: nowrap;

  &:hover {
    border-color: $color-primary;
    color: $color-primary;
  }
}

.list-header-title {
  display: flex;
  align-items: center;
  gap: 12px;

  h2 {
    font-size: $font-size-xl;
    font-weight: $font-weight-bold;
    color: $color-text-primary;
  }
}

.list-header-icon {
  font-size: 28px;
}

.list-header-badge {
  padding: 3px 12px;
  background: $color-primary-light;
  color: $color-primary;
  font-size: $font-size-xs;
  font-weight: $font-weight-medium;
  border-radius: $radius-full;
}

.list-search {
  display: flex;
  align-items: center;
}

.list-search-input {
  padding: 8px 16px;
  border: 1.5px solid #e0e4ea;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  outline: none;
  width: 200px;
  transition: border-color $transition-fast;

  &:focus {
    border-color: $color-primary;
  }
}

// ===== 课程卡片网格 =====
.courses-grid-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 16px 20px 40px;
}

.course-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.empty-state {
  text-align: center;
  padding: 60px 0;
  color: $color-text-muted;
}

// ===== 详情弹层 =====
.course-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 100;
  overflow-y: auto;
  padding: 20px;
}

.course-detail-panel {
  max-width: 1280px;
  margin: 40px auto;
  background: #fff;
  border-radius: $radius-xl;
  position: relative;
  overflow: hidden;
}

.close-btn {
  position: absolute;
  top: 16px;
  right: 20px;
  z-index: 20;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: rgba(0, 0, 0, 0.5);
  color: #fff;
  font-size: 18px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all $transition-fast;

  &:hover {
    background: rgba(0, 0, 0, 0.7);
  }
}

.courses-main {
  padding: 24px 40px 60px;
  display: flex;
  gap: 32px;
  min-height: calc(100vh - 340px);
}

.video-panel {
  flex: 1;
  min-width: 0;
}

// ===== 响应式 =====
@include respond-to('desktop') {
  .category-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .course-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .courses-grid-section {
    padding-left: 20px;
    padding-right: 20px;
  }
}

@include respond-to('tablet') {
  .category-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .course-grid {
    grid-template-columns: 1fr;
  }
  .courses-main {
    flex-direction: column;
    padding: 20px;
  }
  .list-header {
    flex-direction: column;
    align-items: flex-start;
  }
}

@include respond-to('mobile') {
  .category-grid {
    grid-template-columns: 1fr;
  }
  .courses-main {
    padding: 16px;
  }
}
</style>