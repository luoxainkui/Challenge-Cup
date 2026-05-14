<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="service-hero">
      <span class="service-hero-icon">&#128218;</span>
      <h1 class="service-hero-title">精讲课程</h1>
      <p class="service-hero-desc">覆盖公共课及专业课，由一线名师倾心打造，聚焦广西专升本考纲考点，系统梳理知识框架。</p>
    </div>

    <!-- 筛选栏 -->
    <div class="filter-bar">
      <div class="filter-group">
        <span class="filter-label">类别：</span>
        <button
          v-for="cat in categories"
          :key="cat.value"
          :class="['filter-tag', { active: activeCategory === cat.value }]"
          @click="activeCategory = cat.value"
        >{{ cat.label }}</button>
      </div>
      <div class="search-box">
        <input v-model="searchKeyword" type="text" class="search-input" placeholder="搜索课程..." />
        <button class="search-btn">&#128269;</button>
      </div>
    </div>

    <!-- 课程列表 -->
    <div class="course-grid">
      <div v-for="course in filteredCourses" :key="course.id" class="course-card">
        <div class="course-card-img" :style="{ background: course.bgColor }">
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
              <span class="stat-item">&#128101; {{ course.students }}</span>
              <span class="stat-item">&#11088; {{ course.rating }}</span>
            </div>
          </div>
          <div class="course-footer">
            <span class="course-price">¥{{ course.price }}</span>
            <button class="course-btn">立即报名</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 分页 -->
    <div class="pagination">
      <button class="page-btn disabled">上一页</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">3</button>
      <button class="page-btn">...</button>
      <button class="page-btn">8</button>
      <button class="page-btn">下一页</button>
    </div>

    <!-- ========== AI 功能预留区 ========== -->
    <!--
      后续 AI 功能接入接口：
      - 课程智能推荐：根据用户学习行为推荐适配课程
      - 学习路径规划：AI 生成个性化课程学习计划
      - 课程质量评分：基于学员反馈的智能评分系统
      - 智能答疑：课程内容相关的 AI 问答助手
      API 端点预留：
        POST /api/ai/course/recommend
        POST /api/ai/course/path-plan
        GET  /api/ai/course/qa?courseId=xxx
    -->
    <div class="ai-placeholder">
      <div class="ai-placeholder-header">
        <span class="ai-icon">&#129302;</span>
        <h3>AI 智能推荐</h3>
        <span class="ai-badge">即将上线</span>
      </div>
      <p class="ai-placeholder-desc">基于您的学习进度与薄弱环节，AI 将为您智能推荐最适合的课程组合，实现个性化高效备考。</p>
      <div class="ai-slot-row">
        <div class="ai-slot-card" v-for="i in 3" :key="i">
          <div class="ai-slot-thumb"></div>
          <div class="ai-slot-line w-60"></div>
          <div class="ai-slot-line w-40"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const searchKeyword = ref('')
const activeCategory = ref('all')

const categories = [
  { label: '全部', value: 'all' },
  { label: '公共课', value: 'public' },
  { label: '专业课', value: 'major' },
]

const courses = ref([
  { id: 1, subject: '大学英语', category: '公共课', name: '专升本大学英语精讲班', desc: '从词汇到写作，系统性提升英语综合能力，紧扣广西专升本英语考纲', teacher: '张雪峰教授', students: 3256, rating: 4.9, price: 299, hot: true, bgColor: 'linear-gradient(135deg, #e8f3ff, #d0e6ff)' },
  { id: 2, subject: '高等数学', category: '公共课', name: '专升本高等数学强化班', desc: '聚焦必考知识点，精讲精练，帮助零基础学员快速突破数学难关', teacher: '李明博士', students: 2187, rating: 4.8, price: 359, hot: true, bgColor: 'linear-gradient(135deg, #fff3e8, #ffe6d0)' },
  { id: 3, subject: '管理学', category: '专业课', name: '管理学原理精讲精练', desc: '结合广西专升本管理学考纲，深入浅出讲解管理理论与实践案例', teacher: '王红副教授', students: 1876, rating: 4.7, price: 259, hot: false, bgColor: 'linear-gradient(135deg, #f0ffe8, #d8ffc0)' },
  { id: 4, subject: '大学语文', category: '公共课', name: '专升本大学语文基础班', desc: '从文言文到现代文阅读，全面提升语文素养与应试技巧', teacher: '刘芳教授', students: 1567, rating: 4.8, price: 199, hot: false, bgColor: 'linear-gradient(135deg, #f3e8ff, #e0d0ff)' },
  { id: 5, subject: '会计学', category: '专业课', name: '会计学基础与实务', desc: '理论联系实际，掌握会计核心技能，轻松应对专业考试', teacher: '陈强讲师', students: 1342, rating: 4.6, price: 279, hot: false, bgColor: 'linear-gradient(135deg, #e8ffee, #c0ffd8)' },
  { id: 6, subject: '计算机', category: '专业课', name: '计算机应用基础速成班', desc: '零基础入门，涵盖Office操作与计算机基础理论，快速提分', teacher: '赵敏博士', students: 2103, rating: 4.7, price: 239, hot: false, bgColor: 'linear-gradient(135deg, #fff0e8, #ffe0c8)' },
  { id: 7, subject: '政治', category: '公共课', name: '专升本政治理论精讲班', desc: '紧扣时事热点，系统梳理政治理论考点，助力高分突破', teacher: '周华教授', students: 2890, rating: 4.9, price: 269, hot: true, bgColor: 'linear-gradient(135deg, #fff8e8, #ffeecc)' },
  { id: 8, subject: '经济学', category: '专业课', name: '经济学原理与实务', desc: '宏观微观经济学核心知识详解，配合同步习题巩固提升', teacher: '吴芳博士', students: 987, rating: 4.5, price: 289, hot: false, bgColor: 'linear-gradient(135deg, #e8f5ff, #cce5ff)' },
])

const filteredCourses = computed(() => {
  let result = courses.value
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
</script>