<template>
  <div class="ai-placeholder">
    <div class="ai-placeholder-header">
      <span class="ai-icon">🤖</span>
      <h3>AI 智能推荐</h3>
      <span class="ai-badge">即将上线</span>
    </div>
    <p class="ai-placeholder-desc">
      基于您的学习进度与薄弱环节，AI 将为您智能推荐最适合的课程组合，实现个性化高效备考。
    </p>
    <div class="ai-slot-row">
      <div class="ai-slot-card" v-for="i in 3" :key="i">
        <div class="ai-slot-thumb"></div>
        <div class="ai-slot-line w-60"></div>
        <div class="ai-slot-line w-40"></div>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.ai-placeholder {
  max-width: $max-width;
  margin: 0 auto 60px;
  padding: 32px;
  background: linear-gradient(135deg, #667eea1a, #764ba21a);
  border-radius: $radius-xl;
  border: 1px dashed #667eea;
}

.ai-placeholder-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;

  h3 {
    font-size: $font-size-lg;
    font-weight: $font-weight-semibold;
    color: $color-text-primary;
  }
}

.ai-icon {
  font-size: 28px;
}

.ai-badge {
  padding: 2px 12px;
  background: $color-primary;
  color: #fff;
  font-size: 11px;
  border-radius: $radius-full;
}

.ai-placeholder-desc {
  font-size: $font-size-sm;
  color: $color-text-tertiary;
  margin-bottom: 20px;
}

.ai-slot-row {
  display: flex;
  gap: 20px;
}

.ai-slot-card {
  flex: 1;
  padding: 16px;
  background: #fff;
  border-radius: $radius-lg;

  .ai-slot-thumb {
    height: 60px;
    background: #f0f2f5;
    border-radius: $radius-md;
    margin-bottom: 12px;
  }
  .ai-slot-line {
    height: 12px;
    background: #f0f2f5;
    border-radius: 6px;
    margin-bottom: 8px;

    &.w-60 { width: 60%; }
    &.w-40 { width: 40%; }
  }
}
</style>