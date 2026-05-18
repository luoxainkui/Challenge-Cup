<template>
  <div class="admission-page">
    <!-- Hero -->
    <section class="admission-hero">
      <h1>志愿智能填报</h1>
      <p>数据驱动，科学填报，助你精准定位目标院校</p>
    </section>

    <!-- 统计数据 -->
    <section class="admission-stats-section">
      <div class="stats-grid">
        <div v-for="s in ADMISSION_STATS" :key="s.label" class="stat-card">
          <span class="stat-num">{{ s.num }}</span>
          <span class="stat-label">{{ s.label }}</span>
        </div>
      </div>
    </section>

    <!-- 报考流程 -->
    <section class="admission-steps-section">
      <h2 class="section-title">📋 报考流程</h2>
      <div class="steps-grid">
        <div v-for="item in ADMISSION_STEPS" :key="item.step" class="step-card">
          <span class="step-badge">0{{ item.step }}</span>
          <span class="step-icon">{{ item.icon }}</span>
          <h3>{{ item.title }}</h3>
          <p>{{ item.desc }}</p>
        </div>
      </div>
    </section>

    <!-- 院校报考指南 -->
    <section class="school-guide-section">
      <h2 class="section-title">🏫 院校报考指南</h2>
      <div class="school-grid">
        <div v-for="school in SCHOOL_GUIDE" :key="school.id" class="school-card" :class="{ top: school.isTop }">
          <div class="school-header">
            <span class="school-badge" :style="{ background: school.color }">{{ school.icon }}</span>
            <div class="school-info">
              <h3>{{ school.name }} <span v-if="school.isTop" class="top-tag">重点</span></h3>
              <span class="school-meta">{{ school.category }} · {{ school.location }}</span>
            </div>
          </div>
          <p class="school-desc">{{ school.desc }}</p>
          <div class="school-features">
            <span v-for="f in school.features" :key="f" class="feature-tag">{{ f }}</span>
          </div>
          <div class="school-stats">
            <span>📊 参考分: <strong>{{ school.admissionScore }}</strong></span>
            <span>📋 计划: <strong>{{ school.planCount }}</strong>人</span>
          </div>
        </div>
      </div>
    </section>

    <!-- 历年分数线 -->
    <section class="score-line-section">
      <h2 class="section-title">📈 历年分数线参考</h2>
      <div class="score-table-wrap">
        <table class="score-table">
          <thead>
            <tr>
              <th>年份</th>
              <th>科类</th>
              <th>最低分</th>
              <th>平均分</th>
              <th>最高分</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(r, i) in SCORE_LINES" :key="i">
              <td>{{ r.year }}</td>
              <td>{{ r.subject }}</td>
              <td class="score-min">{{ r.minScore }}</td>
              <td>{{ r.avgScore }}</td>
              <td class="score-max">{{ r.maxScore }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 适配预测 -->
    <section class="predict-section">
      <h2 class="section-title">🎯 院校适配预测</h2>
      <p class="predict-subtitle">输入预估分数与意向专业，智能匹配最适合你的院校</p>
      <div class="predict-features">
        <div v-for="f in PREDICT_FEATURES" :key="f.title" class="predict-card">
          <span class="predict-icon">{{ f.icon }}</span>
          <h3>{{ f.title }}</h3>
          <p>{{ f.desc }}</p>
        </div>
      </div>
      <div class="predict-cta">
        <div class="predict-form-preview">
          <div class="form-row">
            <input class="form-input" placeholder="输入预估分数" type="number" />
            <select class="form-select"><option>选择意向科类</option><option>文史类</option><option>理工类</option><option>医学类</option></select>
          </div>
          <button class="predict-btn">开始智能匹配</button>
        </div>
        <p class="predict-hint">* 智能预测结果仅供参考，最终以官方公布为准</p>
      </div>
    </section>

    <!-- 常见问题 -->
    <section class="faq-section">
      <h2 class="section-title">❓ 常见问题</h2>
      <div class="faq-list">
        <details v-for="(item, i) in ADMISSION_FAQ" :key="i" class="faq-item">
          <summary class="faq-q">{{ item.q }}</summary>
          <p class="faq-a">{{ item.a }}</p>
        </details>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ADMISSION_STATS, ADMISSION_STEPS, SCHOOL_GUIDE, SCORE_LINES, PREDICT_FEATURES, ADMISSION_FAQ } from '@/constants/admission'
</script>

<style lang="scss" scoped>
.admission-page { min-height: 100vh; background: $color-bg-page; }

.admission-hero {
  padding: 100px 0 32px; text-align: center;
  background: $color-gradient-primary; color: #fff;
  h1 { font-size: $font-size-4xl; font-weight: $font-weight-bold; margin-bottom: 8px; }
  p { opacity: 0.85; font-size: $font-size-md; }
}

// 统计
.admission-stats-section { max-width: $max-width; margin: 0 auto; padding: 32px 20px 0; }
.stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.stat-card {
  background: #fff; border-radius: $radius-xl; padding: 24px; text-align: center;
  box-shadow: $shadow-sm; transition: transform $transition-fast;
  &:hover { transform: translateY(-3px); }
}
.stat-num { display: block; font-size: $font-size-6xl; font-weight: $font-weight-bold; color: $color-primary; }
.stat-label { font-size: $font-size-sm; color: $color-text-muted; margin-top: 4px; }

// 公共标题
.section-title {
  font-size: $font-size-3xl; font-weight: $font-weight-bold; color: $color-text-primary;
  text-align: center; margin-bottom: 32px;
}

// 流程
.admission-steps-section { max-width: $max-width; margin: 0 auto; padding: 60px 20px 0; }
.steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; }
.step-card {
  background: #fff; border-radius: $radius-2xl; padding: 28px 20px; text-align: center;
  box-shadow: $shadow-sm; position: relative;
  h3 { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; margin: 10px 0 6px; }
  p { font-size: $font-size-xs; color: $color-text-muted; line-height: 1.5; }
}
.step-badge {
  position: absolute; top: -12px; left: 20px;
  background: $color-primary; color: #fff; font-size: $font-size-xs; font-weight: $font-weight-bold;
  padding: 3px 12px; border-radius: $radius-full;
}
.step-icon { font-size: 32px; display: block; margin-top: 6px; }

// 院校指南
.school-guide-section { max-width: $max-width; margin: 0 auto; padding: 60px 20px 0; }
.school-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.school-card {
  background: #fff; border-radius: $radius-2xl; padding: 24px;
  box-shadow: $shadow-sm; transition: all $transition-fast;
  &.top { border-left: 4px solid $color-primary; }
  &:hover { box-shadow: $shadow-md; transform: translateY(-2px); }
}
.school-header { display: flex; align-items: center; gap: 12px; margin-bottom: 12px; }
.school-badge {
  width: 44px; height: 44px; border-radius: $radius-lg;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 18px; font-weight: $font-weight-bold; flex-shrink: 0;
}
.school-info {
  h3 { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; }
}
.school-meta { font-size: $font-size-xs; color: $color-text-muted; }
.top-tag {
  font-size: $font-size-xs; color: $color-primary; border: 1px solid $color-primary;
  padding: 1px 6px; border-radius: $radius-sm; margin-left: 6px;
}
.school-desc { font-size: $font-size-sm; color: $color-text-body; line-height: 1.6; margin-bottom: 10px; }
.school-features { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px; }
.feature-tag {
  padding: 2px 10px; background: $color-primary-light; color: $color-primary;
  font-size: $font-size-xs; border-radius: $radius-full;
}
.school-stats {
  display: flex; gap: 20px; font-size: $font-size-sm; color: $color-text-muted;
  strong { color: $color-text-primary; }
}

// 分数线
.score-line-section { max-width: $max-width; margin: 0 auto; padding: 60px 20px 0; }
.score-table-wrap { overflow-x: auto; }
.score-table {
  width: 100%; border-collapse: collapse; background: #fff;
  border-radius: $radius-xl; overflow: hidden; box-shadow: $shadow-sm;
  th, td { padding: 12px 16px; text-align: center; font-size: $font-size-sm; }
  th { background: $color-primary; color: #fff; font-weight: $font-weight-medium; }
  td { border-bottom: 1px solid #f0f0f0; color: $color-text-body; }
  tr:hover td { background: #f8f9fb; }
}
.score-min { color: $color-success; font-weight: $font-weight-semibold; }
.score-max { color: $color-danger; font-weight: $font-weight-semibold; }

// 适配预测
.predict-section { max-width: $max-width; margin: 0 auto; padding: 60px 20px 0; }
.predict-subtitle { text-align: center; font-size: $font-size-sm; color: $color-text-muted; margin-top: -20px; margin-bottom: 32px; }
.predict-features { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.predict-card {
  background: #fff; border-radius: $radius-xl; padding: 24px 16px; text-align: center;
  box-shadow: $shadow-sm;
  h3 { font-size: $font-size-sm; font-weight: $font-weight-semibold; color: $color-text-primary; margin: 8px 0 6px; }
  p { font-size: $font-size-xs; color: $color-text-muted; line-height: 1.5; }
}
.predict-icon { font-size: 32px; }
.predict-cta {
  margin-top: 32px; background: #fff; border-radius: $radius-2xl; padding: 28px;
  box-shadow: $shadow-sm; text-align: center;
}
.form-row { display: flex; gap: 12px; justify-content: center; margin-bottom: 16px; }
.form-input, .form-select {
  padding: 10px 16px; border: 1.5px solid #e0e4ea; border-radius: $radius-lg;
  font-size: $font-size-sm; outline: none;
  &:focus { border-color: $color-primary; }
}
.predict-btn {
  padding: 12px 40px; background: $color-primary; color: #fff; border: none;
  border-radius: $radius-full; font-size: $font-size-md; cursor: pointer;
  transition: background $transition-fast;
  &:hover { background: $color-primary-dark; }
}
.predict-hint { margin-top: 12px; font-size: $font-size-xs; color: $color-text-light; }

// FAQ
.faq-section { max-width: $max-width; margin: 0 auto; padding: 60px 20px 80px; }
.faq-list { max-width: 800px; margin: 0 auto; }
.faq-item {
  background: #fff; border-radius: $radius-lg; margin-bottom: 10px;
  padding: 16px 20px; box-shadow: $shadow-sm;
}
.faq-q {
  font-size: $font-size-md; font-weight: $font-weight-medium; color: $color-text-primary;
  cursor: pointer; list-style: none;
  &::-webkit-details-marker { display: none; }
  &::before { content: '▶ '; font-size: 10px; color: $color-primary; margin-right: 6px; }
}
details[open] .faq-q::before { content: '▼ '; }
.faq-a {
  margin-top: 12px; padding-top: 12px; border-top: 1px solid #f0f0f0;
  font-size: $font-size-sm; color: $color-text-body; line-height: 1.7;
}

@include respond-to('tablet') {
  .stats-grid, .steps-grid, .predict-features { grid-template-columns: repeat(2, 1fr); }
  .school-grid { grid-template-columns: 1fr; }
  .form-row { flex-direction: column; align-items: center; }
}

@include respond-to('mobile') {
  .stats-grid, .steps-grid, .predict-features, .school-grid { grid-template-columns: 1fr; }
}
</style>