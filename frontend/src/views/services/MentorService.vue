<template>
  <div class="page-container">
    <!-- 页面头部 -->
    <div class="service-hero">
      <span class="service-hero-icon">&#128101;</span>
      <h1 class="service-hero-title">伴学服务</h1>
      <p class="service-hero-desc">专属班主任全程督学，制定详细学习规划，定期跟进学习进度，确保每一步都走得扎实。</p>
    </div>

    <!-- 服务亮点 -->
    <div class="mentor-features">
      <div class="mentor-feature-item">
        <div class="mf-icon">&#128100;</div>
        <h4>1对1专属导师</h4>
        <p>每位学员配备专属班主任导师，全程跟踪学习状态</p>
      </div>
      <div class="mentor-feature-item">
        <div class="mf-icon">&#128197;</div>
        <h4>定制学习计划</h4>
        <p>根据入学测评结果，生成个性化阶段学习计划</p>
      </div>
      <div class="mentor-feature-item">
        <div class="mf-icon">&#128276;</div>
        <h4>智能提醒督学</h4>
        <p>上课提醒、作业提醒、考试提醒，不错过每个关键节点</p>
      </div>
      <div class="mentor-feature-item">
        <div class="mf-icon">&#128172;</div>
        <h4>定期回访沟通</h4>
        <p>每周学习报告 + 月度电话回访，及时调整学习策略</p>
      </div>
    </div>

    <!-- 学习流程 -->
    <section class="quiz-section">
      <h2 class="section-title">伴学流程</h2>
      <div class="flow-steps">
        <div class="flow-step">
          <div class="step-num">01</div>
          <div class="step-content">
            <h3>入学测评</h3>
            <p>全面评估当前知识水平与薄弱环节</p>
          </div>
        </div>
        <div class="flow-arrow">&rarr;</div>
        <div class="flow-step">
          <div class="step-num">02</div>
          <div class="step-content">
            <h3>定制计划</h3>
            <p>生成个性化学习规划与阶段目标</p>
          </div>
        </div>
        <div class="flow-arrow">&rarr;</div>
        <div class="flow-step">
          <div class="step-num">03</div>
          <div class="step-content">
            <h3>每日督学</h3>
            <p>课前提醒、课后作业、每日打卡</p>
          </div>
        </div>
        <div class="flow-arrow">&rarr;</div>
        <div class="flow-step">
          <div class="step-num">04</div>
          <div class="step-content">
            <h3>阶段测评</h3>
            <p>定期模拟测试，检验学习成果</p>
          </div>
        </div>
        <div class="flow-arrow">&rarr;</div>
        <div class="flow-step">
          <div class="step-num">05</div>
          <div class="step-content">
            <h3>考前冲刺</h3>
            <p>考前集中突破，心理辅导与应试指导</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 导师团队 -->
    <section class="quiz-section">
      <h2 class="section-title">明星导师</h2>
      <div class="mentor-list">
        <div v-for="m in mentors" :key="m.id" class="mentor-card">
          <div class="mentor-avatar" :style="{ background: m.color }">{{ m.name[0] }}</div>
          <div class="mentor-info">
            <h3 class="mentor-name">{{ m.name }}</h3>
            <span class="mentor-title">{{ m.title }}</span>
            <div class="mentor-tags">
              <span v-for="t in m.tags" :key="t" class="mentor-tag">{{ t }}</span>
            </div>
            <p class="mentor-desc">{{ m.desc }}</p>
            <div class="mentor-stats">
              <span>已带学员 {{ m.students }}+</span>
              <span>好评率 {{ m.rate }}%</span>
            </div>
          </div>
          <button class="mentor-btn">预约咨询</button>
        </div>
      </div>
    </section>

    <!-- 学员评价 -->
    <section class="quiz-section">
      <h2 class="section-title">学员心声</h2>
      <div class="review-list">
        <div v-for="r in reviews" :key="r.id" class="review-card">
          <div class="review-header">
            <div class="review-avatar" :style="{ background: r.color }">{{ r.name[0] }}</div>
            <div>
              <div class="review-name">{{ r.name }}</div>
              <div class="review-stars">
                <span v-for="i in 5" :key="i" :class="{ active: i <= r.stars }">&#11088;</span>
              </div>
            </div>
            <span class="review-date">{{ r.date }}</span>
          </div>
          <p class="review-text">{{ r.text }}</p>
          <div class="review-tag-row">
            <span v-for="t in r.tags" :key="t" class="review-tag">{{ t }}</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ========== AI 功能预留区 ========== -->
    <!--
      后续 AI 功能接入接口：
      - 智能督学：AI自动根据学习进度推送提醒与鼓励
      - 学情报告：AI生成每周/每月学习分析报告
      - 个性化建议：基于学习数据给出针对性改进建议
      - 智能排课：根据学员时间偏好自动排课
      - 答疑匹配：AI智能分配学员问题给最适合的导师
      API 端点预留：
        POST /api/ai/mentor/supervise
        GET  /api/ai/mentor/report
        POST /api/ai/mentor/advice
        POST /api/ai/mentor/schedule
        POST /api/ai/mentor/qa-match
    -->
    <div class="ai-placeholder">
      <div class="ai-placeholder-header">
        <span class="ai-icon">&#129302;</span>
        <h3>AI 督学助手</h3>
        <span class="ai-badge">即将上线</span>
      </div>
      <p class="ai-placeholder-desc">AI 督学助手将全天候关注您的学习动态，智能分析学习行为，主动推送提醒与鼓励，让督学服务更贴心、更智能。</p>
      <div class="ai-feature-row">
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128276;</span>
          <span>智能提醒</span>
        </div>
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128202;</span>
          <span>数据分析</span>
        </div>
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128488;</span>
          <span>情感关怀</span>
        </div>
        <div class="ai-feature-item">
          <span class="ai-feature-icon">&#128161;</span>
          <span>策略建议</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const mentors = ref([
  {
    id: 1, name: '林晓燕', title: '资深班主任导师', color: '#2a6eff',
    tags: ['英语', '管理类'], desc: '10年教育辅导经验，擅长专升本全科规划，帮助500+学员成功上岸',
    students: 520, rate: 99
  },
  {
    id: 2, name: '黄志强', title: '金牌伴学导师', color: '#ff6b35',
    tags: ['数学', '计算机'], desc: '8年专升本教辅经验，专注理科类学员伴学督学，提分效果显著',
    students: 380, rate: 98
  },
  {
    id: 3, name: '周美琳', title: '高级学习规划师', color: '#4caf50',
    tags: ['语文', '经济学'], desc: '教育学硕士，擅长个性化学习方案制定，关注学员心理健康与备考状态',
    students: 290, rate: 97
  },
])

const reviews = ref([
  {
    id: 1, name: '陈同学', color: '#2a6eff', stars: 5, date: '2025-03-15',
    text: '从最开始不知道怎么复习，到后来跟着林老师制定的计划一步步走，成绩提升非常明显。特别感谢林老师每次在我想要放弃的时候给我鼓励！',
    tags: ['计划合理', '鼓励到位']
  },
  {
    id: 2, name: '刘同学', color: '#ff6b35', stars: 5, date: '2025-02-28',
    text: '数学一直是我的短板，黄老师帮我分析薄弱点后，制定了专项训练计划，两个月数学提高了40多分，真的太感谢了！',
    tags: ['提分显著', '耐心细致']
  },
  {
    id: 3, name: '韦同学', color: '#9c27b0', stars: 4, date: '2025-03-08',
    text: '周老师不仅帮我规划了学习，还经常关心我的心理状态，考试前给了我很多信心。服务很贴心！',
    tags: ['服务贴心', '心理支持']
  },
])
</script>