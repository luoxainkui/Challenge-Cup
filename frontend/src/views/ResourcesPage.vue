<template>
  <div class="resources-page">
    <!-- Hero -->
    <section class="resources-hero">
      <h1>备考资料库</h1>
      <p>一站式备考资源聚合，助你高效复习</p>
    </section>

    <!-- 三大栏目导航 -->
    <section class="resource-tabs-section">
      <div class="resource-tabs">
        <button
          v-for="sec in RESOURCE_SECTIONS"
          :key="sec.id"
          class="resource-tab"
          :class="{ active: activeTab === sec.id }"
          :style="{ '--tab-color': sec.color }"
          @click="activeTab = sec.id"
        >
          <span class="tab-icon">{{ sec.icon }}</span>
          <div class="tab-text">
            <span class="tab-title">{{ sec.title }}</span>
            <span class="tab-desc">{{ sec.desc }}</span>
          </div>
        </button>
      </div>
    </section>

    <!-- 栏目一：考试大纲 -->
    <section v-if="activeTab === 'syllabus'" class="content-section">
      <div class="section-header">
        <h2>📋 专升本考试大纲</h2>
        <p>权威官方考纲解读，明确复习方向</p>
      </div>
      <div class="resource-card-grid">
        <div v-for="item in SYLLABUS_ITEMS" :key="item.id" class="resource-card">
          <div class="card-icon-badge" :style="{ background: item.color }">{{ item.icon }}</div>
          <div class="card-body">
            <h3>{{ item.title }}</h3>
            <p class="card-desc">{{ item.desc }}</p>
            <div class="card-meta">
              <span class="meta-item">📄 {{ item.format }}</span>
              <span class="meta-item">📦 {{ item.fileSize }}</span>
              <span class="meta-item">⬇ {{ formatCount(item.downloadCount) }}次下载</span>
            </div>
          </div>
          <button class="card-download-btn">下载大纲</button>
        </div>
      </div>
    </section>

    <!-- 栏目二：电子资源文库 -->
    <section v-if="activeTab === 'library'" class="content-section">
      <div class="section-header">
        <h2>📚 电子资源文库</h2>
        <p>真题试卷 × 模拟试题 × 学霸笔记</p>
      </div>
      <div class="resource-card-grid">
        <div v-for="item in LIBRARY_ITEMS" :key="item.id" class="resource-card">
          <div class="card-icon-badge" :style="{ background: item.color }">{{ item.icon }}</div>
          <div class="card-body">
            <h3>{{ item.title }}</h3>
            <p class="card-desc">{{ item.desc }}</p>
            <div class="card-tags" v-if="item.tags?.length">
              <span v-for="t in item.tags" :key="t" class="card-tag">{{ t }}</span>
            </div>
            <div class="card-meta">
              <span class="meta-item">📄 {{ item.format }}</span>
              <span class="meta-item">📦 {{ item.fileSize }}</span>
            </div>
          </div>
          <button class="card-download-btn">下载资料</button>
        </div>
      </div>
    </section>

    <!-- 栏目三：核心知识点 -->
    <section v-if="activeTab === 'knowledge'" class="content-section">
      <div class="section-header">
        <h2>🧩 核心知识点梳理</h2>
        <p>按学科分类的知识精华，高效记忆</p>
      </div>
      <div class="knowledge-grid">
        <div v-for="item in KNOWLEDGE_ITEMS" :key="item.id" class="knowledge-card">
          <div class="k-card-badge" :style="{ background: item.color }">{{ item.icon }}</div>
          <div class="k-card-body">
            <h3>{{ item.title }}</h3>
            <p>{{ item.desc }}</p>
            <div class="k-card-stats">
              <div class="k-stat">
                <span class="k-stat-num">{{ item.itemCount }}</span>
                <span class="k-stat-label">条目</span>
              </div>
              <div class="k-stat">
                <span class="k-stat-num">{{ item.estimatedTime }}</span>
                <span class="k-stat-label">预计用时</span>
              </div>
              <div class="k-stat">
                <span class="k-stat-num" :class="'diff-' + item.difficulty">{{ item.difficulty }}</span>
                <span class="k-stat-label">难度</span>
              </div>
            </div>
          </div>
          <button class="k-card-btn">开始学习</button>
        </div>
      </div>
    </section>

    <!-- 嵌入智能题库子栏目 -->
    <section class="quiz-embed-section">
      <div class="section-header">
        <h2>🧠 配套智能题库</h2>
        <p>刷题练习 × 模拟考试 × 错题回顾</p>
      </div>
      <div class="quiz-link-cards">
        <router-link to="/quiz/chapter" class="quiz-link-card">
          <span class="qlc-icon">📖</span>
          <span class="qlc-name">章节练习</span>
          <span class="qlc-arrow">→</span>
        </router-link>
        <router-link to="/quiz/mock" class="quiz-link-card">
          <span class="qlc-icon">📝</span>
          <span class="qlc-name">模拟考试</span>
          <span class="qlc-arrow">→</span>
        </router-link>
        <router-link to="/quiz/real" class="quiz-link-card">
          <span class="qlc-icon">📄</span>
          <span class="qlc-name">历年真题</span>
          <span class="qlc-arrow">→</span>
        </router-link>
        <router-link to="/quiz/mistake" class="quiz-link-card">
          <span class="qlc-icon">🔲</span>
          <span class="qlc-name">错题本</span>
          <span class="qlc-arrow">→</span>
        </router-link>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import {
  RESOURCE_SECTIONS,
  SYLLABUS_ITEMS,
  LIBRARY_ITEMS,
  KNOWLEDGE_ITEMS,
} from '@/constants/resources'

const activeTab = ref('syllabus')

function formatCount(n) {
  if (n >= 10000) return (n / 10000).toFixed(1) + '万'
  if (n >= 1000) return (n / 1000).toFixed(1) + 'k'
  return n
}
</script>

<style lang="scss" scoped>
.resources-page {
  min-height: 100vh;
  background: $color-bg-page;
}

.resources-hero {
  padding: 100px 0 32px;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;
  h1 { font-size: $font-size-4xl; font-weight: $font-weight-bold; margin-bottom: 8px; }
  p { opacity: 0.85; font-size: $font-size-md; }
}

// 栏目导航
.resource-tabs-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 32px 20px;
}

.resource-tabs {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.resource-tab {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 20px 24px;
  background: #fff;
  border: 2px solid #eee;
  border-radius: $radius-2xl;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover, &.active {
    border-color: var(--tab-color);
    box-shadow: $shadow-md;
    transform: translateY(-2px);
  }
}

.tab-icon { font-size: 36px; }
.tab-text { display: flex; flex-direction: column; }
.tab-title { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; }
.tab-desc { font-size: $font-size-xs; color: $color-text-muted; margin-top: 4px; }

// 内容区
.content-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 20px 60px;
}

.section-header {
  text-align: center;
  margin-bottom: 32px;
  h2 { font-size: $font-size-3xl; font-weight: $font-weight-bold; color: $color-text-primary; }
  p { font-size: $font-size-sm; color: $color-text-muted; margin-top: 6px; }
}

.resource-card-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.resource-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  background: #fff;
  border-radius: $radius-2xl;
  padding: 24px;
  box-shadow: $shadow-sm;
  transition: all $transition-fast;

  &:hover { box-shadow: $shadow-md; transform: translateY(-2px); }
}

.card-icon-badge {
  width: 50px; height: 50px;
  border-radius: $radius-xl;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 22px;
  flex-shrink: 0;
}

.card-body { flex: 1; min-width: 0;
  h3 { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 6px; }
}

.card-desc { font-size: $font-size-sm; color: $color-text-muted; line-height: 1.5; margin-bottom: 10px; }

.card-meta { display: flex; gap: 12px; flex-wrap: wrap; }
.meta-item { font-size: $font-size-xs; color: $color-text-light; }

.card-tags { display: flex; gap: 6px; margin-bottom: 8px; }
.card-tag {
  padding: 2px 8px;
  background: #fff3e0;
  color: $color-warning;
  font-size: $font-size-xs;
  border-radius: $radius-sm;
}

.card-download-btn {
  padding: 8px 18px;
  background: $color-primary;
  color: #fff;
  border: none;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  cursor: pointer;
  white-space: nowrap;
  flex-shrink: 0;
  align-self: center;
  transition: background $transition-fast;
  &:hover { background: $color-primary-dark; }
}

// 核心知识点卡片
.knowledge-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

.knowledge-card {
  background: #fff;
  border-radius: $radius-2xl;
  padding: 24px;
  box-shadow: $shadow-sm;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  transition: all $transition-fast;

  &:hover { box-shadow: $shadow-md; transform: translateY(-3px); }
}

.k-card-badge {
  width: 56px; height: 56px;
  border-radius: $radius-xl;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 26px;
  margin-bottom: 14px;
}

.k-card-body {
  h3 { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; margin-bottom: 6px; }
  p { font-size: $font-size-xs; color: $color-text-muted; line-height: 1.5; margin-bottom: 16px; }
}

.k-card-stats { display: flex; gap: 20px; justify-content: center; }
.k-stat { text-align: center; }
.k-stat-num { display: block; font-size: $font-size-lg; font-weight: $font-weight-bold; color: $color-primary; }
.k-stat-label { font-size: $font-size-xs; color: $color-text-light; margin-top: 2px; }

.diff-基础 { color: #4caf50; }
.diff-适中 { color: #ff9800; }

.k-card-btn {
  margin-top: 18px;
  width: 100%;
  padding: 10px 0;
  background: $color-primary-light;
  color: $color-primary;
  border: none;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  font-weight: $font-weight-medium;
  cursor: pointer;
  transition: all $transition-fast;
  &:hover { background: $color-primary; color: #fff; }
}

// 智能题库嵌入
.quiz-embed-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 0 20px 60px;
}

.quiz-link-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.quiz-link-card {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 16px 20px;
  background: #fff;
  border-radius: $radius-xl;
  text-decoration: none;
  box-shadow: $shadow-sm;
  transition: all $transition-fast;

  &:hover { box-shadow: $shadow-md; transform: translateY(-2px); }
}

.qlc-icon { font-size: 24px; }
.qlc-name { font-size: $font-size-sm; font-weight: $font-weight-medium; color: $color-text-primary; flex: 1; }
.qlc-arrow { font-size: $font-size-sm; color: $color-text-light; }

@include respond-to('tablet') {
  .resource-card-grid, .knowledge-grid { grid-template-columns: 1fr; }
  .resource-tabs { grid-template-columns: 1fr; }
  .quiz-link-cards { grid-template-columns: repeat(2, 1fr); }
}

@include respond-to('mobile') {
  .resource-card { flex-direction: column; align-items: center; text-align: center; }
  .card-download-btn { align-self: center; }
}
</style>