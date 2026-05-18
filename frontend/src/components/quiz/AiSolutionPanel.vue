<template>
  <div class="ai-solution-box">
    <div class="ai-solution-header" @click="expanded = !expanded">
      <div class="ai-solution-title">
        <span class="ai-solution-icon">🤖</span>
        <span>AI 解题解析</span>
        <span class="ai-solution-badge">AI 辅助</span>
      </div>
      <span class="ai-solution-arrow" :class="{ expanded }">▾</span>
    </div>
    <transition name="ai-solution-fade">
      <div v-if="expanded" class="ai-solution-content">
        <div class="ai-solution-step">
          <div class="ai-step-label">📋 审题分析</div>
          <div class="ai-step-body ai-placeholder-text">正在分析题目类型、考查知识点及题干关键信息...</div>
        </div>
        <div class="ai-solution-step">
          <div class="ai-step-label">🔍 解题步骤</div>
          <div class="ai-step-body">
            <div class="ai-placeholder-line w-80"></div>
            <div class="ai-placeholder-line w-60"></div>
            <div class="ai-placeholder-line w-70"></div>
          </div>
        </div>
        <div class="ai-solution-step">
          <div class="ai-step-label">⚠️ 易错提醒</div>
          <div class="ai-step-body">
            <div class="ai-placeholder-line w-50"></div>
            <div class="ai-placeholder-line w-40"></div>
          </div>
        </div>
        <div class="ai-solution-step">
          <div class="ai-step-label">📚 知识点拓展</div>
          <div class="ai-step-body">
            <div class="ai-tag-row">
              <span class="ai-tag-placeholder">相关考点一</span>
              <span class="ai-tag-placeholder">相关考点二</span>
              <span class="ai-tag-placeholder">关联公式</span>
            </div>
          </div>
        </div>
        <div class="ai-solution-footer">
          <span class="ai-footer-note">💡 以上内容由 AI 自动生成，仅供参考</span>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const expanded = ref(true)
</script>

<style lang="scss" scoped>
.ai-solution-box {
  margin: 0 0 20px;
  border: 1px solid #e0e7ff;
  border-radius: $radius-lg;
  overflow: hidden;
  background: linear-gradient(135deg, #fafbff 0%, #f3f6ff 100%);
}
.ai-solution-header {
  display: flex; align-items: center; justify-content: space-between;
  padding: 14px 18px; cursor: pointer; user-select: none; transition: background .2s;
  &:hover { background: rgba(102, 126, 234, .06); }
}
.ai-solution-title { display: flex; align-items: center; gap: 8px; font-size: 13px; font-weight: $font-weight-semibold; color: #3740a0; }
.ai-solution-icon { font-size: 18px; }
.ai-solution-badge {
  font-size: 10px; padding: 2px 8px; border-radius: 50px;
  background: linear-gradient(135deg, #818cf8, #6366f1); color: #fff; font-weight: $font-weight-medium;
}
.ai-solution-arrow { font-size: 14px; color: #818cf8; transition: transform .25s;
  &.expanded { transform: rotate(180deg); }
}
.ai-solution-content { padding: 4px 18px 18px; }
.ai-solution-step { margin-top: 14px; padding: 12px 14px; background: #fff; border-radius: $radius-md; border: 1px solid #eef1f8; }
.ai-step-label { font-size: 12px; font-weight: $font-weight-semibold; color: #4a4a6a; margin-bottom: 8px; }
.ai-step-body { font-size: 12px; color: #7a7a9a; line-height: 1.7; }
.ai-placeholder-text { padding: 8px 0; font-style: italic; color: #9e9ec0; }
.ai-placeholder-line {
  height: 8px;
  background: linear-gradient(90deg, #eef1f8 25%, #f0f4ff 50%, #eef1f8 75%);
  background-size: 200% 100%;
  border-radius: $radius-full;
  animation: ai-shimmer 2s ease-in-out infinite;
  & + & { margin-top: 8px; }
  &.w-80 { width: 80%; } &.w-70 { width: 70%; } &.w-60 { width: 60%; }
  &.w-50 { width: 50%; } &.w-40 { width: 40%; }
}
@keyframes ai-shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
.ai-tag-row { display: flex; gap: 8px; flex-wrap: wrap; }
.ai-tag-placeholder {
  padding: 4px 12px; font-size: 11px; border-radius: 50px;
  background: #eef0ff; color: #6366f1; border: 1px dashed #a5b4fc;
}
.ai-solution-footer { margin-top: 14px; padding-top: 12px; border-top: 1px dashed #dde2f0; text-align: center; }
.ai-footer-note { font-size: 11px; color: #a0a0c0; }

.ai-solution-fade-enter-active, .ai-solution-fade-leave-active { transition: all .3s ease; }
.ai-solution-fade-enter-from, .ai-solution-fade-leave-to { opacity: 0; max-height: 0; padding-top: 0; padding-bottom: 0; }

@media (max-width: 520px) {
  .ai-solution-header { padding: 12px 14px; }
  .ai-solution-content { padding: 4px 12px 14px; }
  .ai-solution-title { font-size: 12px; }
  .ai-solution-icon { font-size: 16px; }
}
</style>