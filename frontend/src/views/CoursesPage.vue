<template>
  <div class="courses-page">
    <!-- Hero -->
    <section class="courses-hero">
      <h1>课程中心</h1>
      <p>精选优质课程，助你高效备考</p>
    </section>

    <!-- 分类筛选 -->
    <CategoryBar v-model="activeCategory" />

    <!-- 课程列表 -->
    <section class="courses-grid-section">
      <div class="course-grid">
        <CourseCard
          v-for="c in filteredCourses"
          :key="c.id"
          :course="c"
          @click="goToCourse"
        />
      </div>
      <div class="empty-state" v-if="filteredCourses.length === 0">
        <p>暂无相关课程</p>
      </div>
    </section>

    <!-- 课程详情/学习页弹层 -->
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
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { COURSES } from '@/constants/courses'
import { useCoursePlayer } from '@/composables/useCoursePlayer'
import CategoryBar from '@/components/course/CategoryBar.vue'
import CourseCard from '@/components/course/CourseCard.vue'
import CourseTabs from '@/components/course/CourseTabs.vue'
import ChapterDirectory from '@/components/course/ChapterDirectory.vue'
import VideoPlayer from '@/components/course/VideoPlayer.vue'
import CourseDetail from '@/components/course/CourseDetail.vue'
import PaymentModal from '@/components/course/PaymentModal.vue'

const activeCategory = ref('all')
const selectedCourse = ref(null)

const filteredCourses = computed(() => {
  if (activeCategory.value === 'all') return COURSES
  return COURSES.filter(c => {
    if (activeCategory.value === 'public') return c.category === '公共课'
    if (activeCategory.value === 'major') return c.category === '专业课'
    return true
  })
})

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

function goToCourse(course) {
  selectedCourse.value = course
  switchCourse(course)
}

function onPaySuccess(course) {
  showPayment.value = false
  console.log('支付成功:', course.name)
}

// 从精讲课程跳转过来时自动打开对应课程详情
const route = useRoute()
onMounted(() => {
  const courseId = route.query.id
  if (courseId) {
    const course = COURSES.find(c => c.id === Number(courseId))
    if (course) {
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

.courses-grid-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 32px 20px 60px;
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

@include respond-to('desktop') {
  .courses-grid-section {
    padding-left: 20px;
    padding-right: 20px;
  }
}

@include respond-to('tablet') {
  .course-grid {
    grid-template-columns: 1fr;
  }
  .courses-main {
    flex-direction: column;
    padding: 20px;
  }
}

@include respond-to('mobile') {
  .courses-main {
    padding: 16px;
  }
}
</style>