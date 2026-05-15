<template>
  <div class="page-container">
    <!-- Hero -->
    <div class="service-hero">
      <span class="service-hero-icon">&#128202;</span>
      <h1 class="service-hero-title">智能题库</h1>
      <p class="service-hero-desc">海量真题及模拟题，智能组卷与错题分析，支持个性化定制训练，精确检测学习效果。</p>
    </div>

    <!-- 统计概览 -->
    <div class="quiz-stats">
      <div v-for="s in QUIZ_STATISTICS" :key="s.label" class="stat-card">
        <div class="stat-num">{{ s.num }}</div>
        <div class="stat-label">{{ s.label }}</div>
      </div>
    </div>

    <!-- 练习模式卡片 -->
    <section class="quiz-section">
      <h2 class="section-title">练习模式</h2>
      <div class="mode-cards">
        <div
          v-for="m in QUIZ_MODES"
          :key="m.id"
          class="mode-card"
          @click="handleModeClick(m)"
        >
          <div class="mode-icon">{{ m.icon }}</div>
          <h3>{{ m.name }}</h3>
          <p>{{ m.desc }}</p>
          <div class="mode-count">{{ m.count }}</div>
          <button class="mode-btn">进入{{ m.name }}</button>
        </div>
      </div>
    </section>

    <!-- 科目题库 -->
    <section class="quiz-section">
      <h2 class="section-title">科目题库</h2>
      <div class="subject-grid">
        <div v-for="s in QUIZ_SUBJECTS" :key="s.name" class="subject-card">
          <div class="subject-icon" :style="{ background: s.color }">{{ s.icon }}</div>
          <div class="subject-info">
            <h3 class="subject-name">{{ s.name }}</h3>
            <span class="subject-count">{{ s.count }} 道题</span>
          </div>
          <div class="subject-progress">
            <div class="progress-bar"><div class="progress-fill" :style="{ width: s.progress + '%' }"></div></div>
            <span class="progress-text">{{ s.progress }}%</span>
          </div>
          <button class="subject-btn" @click="startSubject(s)">开始练习</button>
        </div>
      </div>
    </section>

    <!-- AI 预留区 -->
    <div class="ai-placeholder">
      <div class="ai-placeholder-header">
        <span class="ai-icon">&#129302;</span>
        <h3>AI 智能组卷</h3>
        <span class="ai-badge">即将上线</span>
      </div>
      <p class="ai-placeholder-desc">AI 将根据您的历史答题数据，智能分析薄弱知识点，自动生成个性化定制试卷。</p>
      <div class="ai-feature-row">
        <div class="ai-feature-item"><span class="ai-feature-icon">&#127919;</span><span>精准定位薄弱点</span></div>
        <div class="ai-feature-item"><span class="ai-feature-icon">&#128260;</span><span>智能难度匹配</span></div>
        <div class="ai-feature-item"><span class="ai-feature-icon">&#128200;</span><span>学习趋势分析</span></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { QUIZ_STATISTICS, QUIZ_MODES, QUIZ_SUBJECTS } from '@/constants/quiz'

const router = useRouter()

// ---- 模式路由映射 ----
const modeRoutes = {
  chapter: 'quiz-chapter',
  mock: 'quiz-mock',
  real: 'quiz-real',
  mistake: 'quiz-mistake',
}

function handleModeClick(m) {
  const routeName = modeRoutes[m.id]
  if (routeName) {
    router.push({ name: routeName })
  }
}

function startSubject(s) {
  router.push({ name: 'quiz-practice', query: { mode: 'subject', subject: s.name } })
}
</script>

<style lang="scss" scoped>
.page-container {
  min-height: 100vh;
  background: #f5f6fa;
  padding: 0 20px 60px;
}

/* ---- Hero ---- */
.service-hero {
  text-align: center;
  padding: 40px 20px 24px;
  max-width: $max-width;
  margin: 0 auto;
}
.service-hero-icon { font-size: 48px; display: block; margin-bottom: 12px; }
.service-hero-title { font-size: $font-size-2xl; font-weight: $font-weight-bold; color: $color-text-primary; margin-bottom: 8px; }
.service-hero-desc { font-size: $font-size-sm; color: $color-text-secondary; max-width: 520px; margin: 0 auto; line-height: 1.6; }

/* ---- Stats ---- */
.quiz-stats {
  max-width: $max-width;
  margin: 0 auto 24px;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.stat-card {
  background: #fff;
  padding: 20px 12px;
  border-radius: $radius-xl;
  text-align: center;
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
}
.stat-num { font-size: $font-size-xl; font-weight: $font-weight-bold; color: $color-primary; margin-bottom: 4px; }
.stat-label { font-size: $font-size-xs; color: $color-text-tertiary; }

/* ---- Section ---- */
.quiz-section {
  max-width: $max-width;
  margin: 0 auto 24px;
}
.section-title {
  font-size: $font-size-base;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
  margin-bottom: 16px;
  padding-left: 4px;
}

/* ---- Mode Cards ---- */
.mode-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}
.mode-card {
  background: #fff;
  padding: 30px 16px 22px;
  border-radius: $radius-xl;
  text-align: center;
  cursor: pointer;
  transition: all $transition-base;
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
  border: 2px solid transparent;
  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 28px rgba(0,0,0,.08);
    border-color: $color-primary-light;
  }
  h3 { font-size: $font-size-sm; font-weight: $font-weight-semibold; color: $color-text-primary; margin: 10px 0 6px; }
  p { font-size: 11px; color: $color-text-tertiary; margin-bottom: 12px; line-height: 1.5; min-height: 32px; }
}
.mode-icon { font-size: 36px; margin-bottom: 4px; }
.mode-count {
  font-size: 10px;
  display: inline-block;
  padding: 2px 10px;
  background: #f0f2f5;
  border-radius: 50px;
  color: $color-text-tertiary;
  margin-bottom: 14px;
}
.mode-btn {
  padding: 8px 28px;
  border: 1.5px solid $color-primary;
  background: #fff;
  color: $color-primary;
  border-radius: $radius-md;
  font-size: $font-size-xs;
  font-weight: $font-weight-medium;
  cursor: pointer;
  transition: all .15s;
  &:hover { background: $color-primary; color: #fff; }
}

/* ---- Subject Grid ---- */
.subject-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
}
.subject-card {
  background: #fff;
  padding: 24px 18px;
  border-radius: $radius-xl;
  text-align: center;
  box-shadow: 0 2px 12px rgba(0,0,0,.04);
  transition: all $transition-base;
  &:hover { transform: translateY(-2px); box-shadow: 0 6px 22px rgba(0,0,0,.06); }
}
.subject-icon {
  width: 40px; height: 40px;
  display: flex; align-items: center; justify-content: center;
  border-radius: $radius-sm;
  color: #fff; font-size: 13px; font-weight: $font-weight-bold;
  margin: 0 auto 10px;
}
.subject-name { font-size: $font-size-xs; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 4px; }
.subject-count { font-size: 10px; color: $color-text-tertiary; }
.subject-progress {
  display: flex; align-items: center; gap: 8px;
  margin: 10px 0 12px;
}
.progress-bar {
  flex: 1; height: 5px;
  background: #f0f2f5; border-radius: 5px; overflow: hidden;
}
.progress-fill { height: 100%; background: $color-primary; border-radius: 5px; transition: width .3s; }
.progress-text { font-size: 10px; color: $color-text-tertiary; min-width: 30px; text-align: right; }
.subject-btn {
  padding: 6px 24px;
  border: 1px solid rgba($color-primary, .3);
  background: rgba($color-primary, .06);
  color: $color-primary;
  border-radius: $radius-md;
  font-size: 11px;
  font-weight: $font-weight-medium;
  cursor: pointer;
  &:hover { background: $color-primary; color: #fff; }
}

/* ---- AI Placeholder ---- */
.ai-placeholder {
  max-width: $max-width;
  margin: 0 auto;
  padding: 32px 24px;
  text-align: center;
  background: linear-gradient(135deg, #f8f4ff 0%, #eef0ff 100%);
  border-radius: $radius-xl;
  border: 1px dashed #c4b5fd;
}
.ai-placeholder-header {
  display: flex; align-items: center; justify-content: center; gap: 10px;
  margin-bottom: 10px;
}
.ai-icon { font-size: 30px; }
.ai-placeholder-header h3 { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; }
.ai-badge {
  font-size: 10px;
  padding: 2px 8px;
  background: #ede9fe; color: #7c3aed;
  border-radius: 50px;
}
.ai-placeholder-desc { font-size: $font-size-xs; color: $color-text-secondary; max-width: 480px; margin: 0 auto 16px; line-height: 1.6; }
.ai-feature-row { display: flex; justify-content: center; gap: 28px; }
.ai-feature-item {
  display: flex; align-items: center; gap: 6px;
  font-size: $font-size-xs; color: $color-text-tertiary;
}
.ai-feature-icon { font-size: 16px; }

/* ---- Responsive ---- */
@media (max-width: 900px) {
  .mode-cards, .subject-grid { grid-template-columns: repeat(2, 1fr); }
  .quiz-stats { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 520px) {
  .mode-cards, .subject-grid { grid-template-columns: 1fr; }
  .quiz-stats { grid-template-columns: 1fr 1fr; }
}
</style>