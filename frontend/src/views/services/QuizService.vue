<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="service-hero">
      <span class="service-hero-icon">&#128202;</span>
      <h1 class="service-hero-title">智能题库</h1>
      <p class="service-hero-desc">海量真题及模拟题，智能组卷与错题分析，支持个性化定制训练，精确检测学习效果。</p>
    </div>

    <!-- 题库统计概览 -->
    <div class="quiz-stats">
      <div class="stat-card">
        <div class="stat-num">12,800+</div>
        <div class="stat-label">题目总数</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">8</div>
        <div class="stat-label">科目覆盖</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">98.6%</div>
        <div class="stat-label">答案解析率</div>
      </div>
      <div class="stat-card">
        <div class="stat-num">50万+</div>
        <div class="stat-label">累计刷题人次</div>
      </div>
    </div>

    <!-- 练习模式 -->
    <section class="quiz-section">
      <h2 class="section-title">练习模式</h2>
      <div class="mode-cards">
        <div class="mode-card">
          <div class="mode-icon">&#128214;</div>
          <h3>章节练习</h3>
          <p>按知识点章节逐项突破，夯实基础</p>
          <div class="mode-count">1,200+ 章节</div>
          <button class="mode-btn">进入练习</button>
        </div>
        <div class="mode-card">
          <div class="mode-icon">&#128221;</div>
          <h3>模拟考试</h3>
          <p>全真模拟考试环境，计时作答体验真实考场</p>
          <div class="mode-count">48 套模拟卷</div>
          <button class="mode-btn">进入考试</button>
        </div>
        <div class="mode-card">
          <div class="mode-icon">&#128196;</div>
          <h3>历年真题</h3>
          <p>收录近5年广西专升本真题，掌握命题规律</p>
          <div class="mode-count">15 套真题</div>
          <button class="mode-btn">开始刷题</button>
        </div>
        <div class="mode-card">
          <div class="mode-icon">&#128260;</div>
          <h3>错题本</h3>
          <p>自动收录错题，针对性强化薄弱知识点</p>
          <div class="mode-count">智能归类分析</div>
          <button class="mode-btn">查看错题</button>
        </div>
      </div>
    </section>

    <!-- 科目选择 -->
    <section class="quiz-section">
      <h2 class="section-title">科目题库</h2>
      <div class="subject-grid">
        <div v-for="s in subjects" :key="s.name" class="subject-card">
          <div class="subject-icon" :style="{ background: s.color }">{{ s.icon }}</div>
          <div class="subject-info">
            <h3 class="subject-name">{{ s.name }}</h3>
            <span class="subject-count">{{ s.count }} 道题</span>
          </div>
          <div class="subject-progress">
            <div class="progress-bar">
              <div class="progress-fill" :style="{ width: s.progress + '%' }"></div>
            </div>
            <span class="progress-text">{{ s.progress }}%</span>
          </div>
          <button class="subject-btn">开始练习</button>
        </div>
      </div>
    </section>

    <!-- ========== AI 功能预留区 ========== -->
    <!--
      后续 AI 功能接入接口：
      - 智能组卷：根据用户知识薄弱点自动生成定制试卷
      - 智能批改：主观题AI自动评分与反馈
      - 错题分析：AI诊断错误原因并推荐强化练习
      - 能力评估：基于答题数据生成学力雷达图
      - 个性化推题：根据答题正确率智能推送专项题目
      API 端点预留：
        POST /api/ai/quiz/gen-paper
        POST /api/ai/quiz/auto-grade
        GET  /api/ai/quiz/mistake-analysis
        GET  /api/ai/quiz/ability-report
        POST /api/ai/quiz/recommend
    -->
    <div class="ai-placeholder">
      <div class="ai-placeholder-header">
        <span class="ai-icon">&#129302;</span>
        <h3>AI 智能组卷</h3>
        <span class="ai-badge">即将上线</span>
      </div>
      <p class="ai-placeholder-desc">AI 将根据您的历史答题数据，智能分析薄弱知识点，自动生成个性化定制试卷，让每一次练习都精准高效。</p>
      <div class="ai-feature-row">
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#127919;</span>
          <span>精准定位薄弱点</span>
        </div>
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128260;</span>
          <span>智能难度匹配</span>
        </div>
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128200;</span>
          <span>学习趋势分析</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const subjects = ref([
  { name: '大学英语', icon: 'EN', color: '#2a6eff', count: 2850, progress: 35 },
  { name: '高等数学', icon: '数', color: '#ff6b35', count: 2100, progress: 22 },
  { name: '大学语文', icon: '语', color: '#9c27b0', count: 1980, progress: 48 },
  { name: '政治理论', icon: '政', color: '#e74c3c', count: 1650, progress: 60 },
  { name: '管理学', icon: '管', color: '#4caf50', count: 1420, progress: 15 },
  { name: '会计学', icon: '会', color: '#008888', count: 980, progress: 8 },
  { name: '计算机', icon: '计', color: '#ff9800', count: 1120, progress: 30 },
  { name: '经济学', icon: '经', color: '#607d8b', count: 700, progress: 5 },
])
</script>