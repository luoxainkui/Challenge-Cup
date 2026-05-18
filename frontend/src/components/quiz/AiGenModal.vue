<template>
  <transition name="modal-fade">
    <div v-if="visible" class="ai-modal-overlay" @click.self="$emit('close')">
      <div class="ai-modal">
        <div class="ai-modal-header">
          <div class="ai-modal-title-row">
            <span class="ai-modal-icon">🤖</span>
            <h3>AI 智能组卷</h3>
            <span class="ai-modal-badge">即将上线</span>
          </div>
          <button class="ai-modal-close" @click="$emit('close')">✕</button>
        </div>

        <div class="ai-modal-body">
          <!-- 步骤 1：选择范围 -->
          <div class="ai-modal-step">
            <div class="ai-step-indicator">
              <span class="ai-step-num">1</span>
              <span class="ai-step-title">选择组卷范围</span>
            </div>
            <div class="ai-subject-chips">
              <button v-for="s in selected" :key="s" class="ai-chip active" @click="toggle(s)">{{ s }}</button>
              <button v-for="s in available" :key="s" class="ai-chip" @click="toggle(s)">{{ s }}</button>
            </div>
          </div>

          <!-- 步骤 2：题目配置 -->
          <div class="ai-modal-step">
            <div class="ai-step-indicator">
              <span class="ai-step-num">2</span>
              <span class="ai-step-title">题目配置</span>
            </div>
            <div class="ai-config-row">
              <div class="ai-config-item">
                <label>题目数量</label>
                <div class="ai-counter">
                  <button class="ai-counter-btn" @click="count = Math.max(5, count - 5)">−</button>
                  <span class="ai-counter-num">{{ count }}</span>
                  <button class="ai-counter-btn" @click="count = Math.min(50, count + 5)">+</button>
                </div>
              </div>
              <div class="ai-config-item">
                <label>难度分布</label>
                <div class="ai-difficulty-bar">
                  <span class="ai-diff-label" :style="{ width: easy + '%' }">简单 {{ easy }}%</span>
                  <span class="ai-diff-label" :style="{ width: medium + '%' }">中等 {{ medium }}%</span>
                  <span class="ai-diff-label" :style="{ width: hard + '%' }">困难 {{ hard }}%</span>
                </div>
              </div>
            </div>
          </div>

          <!-- 步骤 3：智能分析预览 -->
          <div class="ai-modal-step">
            <div class="ai-step-indicator">
              <span class="ai-step-num">3</span>
              <span class="ai-step-title">智能分析</span>
            </div>
            <div class="ai-analysis-preview">
              <div class="ai-preview-item">
                <span class="ai-preview-dot weak"></span>
                <span>薄弱知识点：<strong>高等数学 / 导数与微分</strong></span>
              </div>
              <div class="ai-preview-item">
                <span class="ai-preview-dot focus"></span>
                <span>建议侧重：<strong>大学英语 / 阅读理解</strong></span>
              </div>
              <div class="ai-preview-item">
                <span class="ai-preview-dot normal"></span>
                <span>已掌握：<strong>政治理论 / 马克思主义哲学</strong></span>
              </div>
            </div>
            <div class="ai-preview-footer">
              <span>📊 基于你的 <strong>128</strong> 次答题记录分析</span>
            </div>
          </div>
        </div>

        <div class="ai-modal-footer">
          <button class="ai-footer-btn secondary" @click="$emit('close')">取消</button>
          <button class="ai-footer-btn primary" disabled>
            <span class="ai-btn-loading"></span>
            功能开发中，敬请期待
          </button>
        </div>

        <div class="ai-modal-note">
          💡 AI 智能组卷功能即将上线，届时将根据你的历史学习数据自动生成个性化试卷
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  visible: { type: Boolean, default: false },
  subjects: { type: Array, required: true },
})

defineEmits(['close'])

const selected = ref([props.subjects[0], props.subjects[1]])
const available = ref(props.subjects.slice(2))
const count = ref(20)
const easy = ref(30)
const medium = ref(50)
const hard = ref(20)

function toggle(name) {
  const idx = selected.value.indexOf(name)
  if (idx >= 0) {
    selected.value.splice(idx, 1)
    available.value.push(name)
  } else {
    available.value.splice(available.value.indexOf(name), 1)
    selected.value.push(name)
  }
}
</script>

<style lang="scss" scoped>
.ai-modal-overlay {
  position: fixed; inset: 0; z-index: 1100;
  display: flex; align-items: center; justify-content: center;
  background: rgba(0,0,0,.45); backdrop-filter: blur(4px); padding: 20px;
}
.ai-modal {
  background: #fff; border-radius: $radius-2xl; width: 100%; max-width: 580px;
  max-height: 90vh; overflow-y: auto; box-shadow: 0 20px 60px rgba(0,0,0,.15);
}
.ai-modal-header { display: flex; align-items: center; justify-content: space-between; padding: 22px 28px 0; }
.ai-modal-title-row { display: flex; align-items: center; gap: 10px; }
.ai-modal-icon { font-size: 24px; }
.ai-modal-title-row h3 { font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary; }
.ai-modal-badge {
  font-size: 10px; padding: 3px 10px;
  background: linear-gradient(135deg, #818cf8, #6366f1); color: #fff;
  border-radius: 50px; font-weight: $font-weight-medium;
}
.ai-modal-close {
  width: 32px; height: 32px; display: flex; align-items: center; justify-content: center;
  border: 1px solid #e8e8e8; background: #fafafa; border-radius: $radius-full;
  font-size: 14px; color: #999; cursor: pointer; transition: all .15s;
  &:hover { background: #eee; color: #555; }
}
.ai-modal-body { padding: 20px 28px 8px; }
.ai-modal-step { margin-bottom: 20px; }
.ai-step-indicator { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
.ai-step-num {
  width: 22px; height: 22px; display: flex; align-items: center; justify-content: center;
  background: linear-gradient(135deg, #818cf8, #6366f1); color: #fff;
  font-size: 11px; font-weight: $font-weight-bold; border-radius: $radius-full; flex-shrink: 0;
}
.ai-step-title { font-size: 13px; font-weight: $font-weight-semibold; color: $color-text-primary; }

.ai-subject-chips { display: flex; flex-wrap: wrap; gap: 8px; padding-left: 30px; }
.ai-chip {
  padding: 6px 16px; font-size: 12px; border: 1.5px solid #e0e0e0; background: #f9f9f9;
  border-radius: 50px; color: $color-text-secondary; cursor: pointer; transition: all .15s;
  &:hover { border-color: #818cf8; color: #818cf8; }
  &.active { border-color: #818cf8; background: #eef0ff; color: #5a4fcf; font-weight: $font-weight-medium; }
}

.ai-config-row { display: flex; gap: 24px; padding-left: 30px; flex-wrap: wrap; }
.ai-config-item { flex: 1; min-width: 160px; }
.ai-config-item label { font-size: 12px; color: $color-text-tertiary; margin-bottom: 6px; display: block; }
.ai-counter { display: flex; align-items: center; border: 1px solid #e0e0e0; border-radius: $radius-md; overflow: hidden; width: fit-content; }
.ai-counter-btn {
  width: 36px; height: 34px; display: flex; align-items: center; justify-content: center;
  border: none; background: #f5f6f8; font-size: 16px; color: $color-text-secondary; cursor: pointer;
  &:hover { background: #e8e8e8; }
}
.ai-counter-num { width: 50px; text-align: center; font-size: $font-size-sm; font-weight: $font-weight-semibold; color: $color-text-primary; }
.ai-difficulty-bar { display: flex; border-radius: $radius-full; overflow: hidden; height: 28px; background: #f0f0f5; }
.ai-diff-label {
  display: flex; align-items: center; justify-content: center; font-size: 10px; color: #fff;
  font-weight: $font-weight-medium; transition: width .3s;
  &:first-child { background: #4caf50; }
  &:nth-child(2) { background: #ff9800; }
  &:last-child { background: #f44336; }
}

.ai-analysis-preview { padding-left: 30px; display: flex; flex-direction: column; gap: 10px; }
.ai-preview-item {
  display: flex; align-items: center; gap: 8px; font-size: 12px; color: #777;
  padding: 8px 14px; background: #f9fafc; border-radius: $radius-md;
  strong { color: $color-text-primary; }
}
.ai-preview-dot { width: 8px; height: 8px; border-radius: $radius-full; flex-shrink: 0;
  &.weak { background: #f44336; } &.focus { background: #ff9800; } &.normal { background: #4caf50; }
}
.ai-preview-footer { padding-left: 30px; font-size: 11px; color: #aaa; margin-top: 4px; strong { color: #888; } }

.ai-modal-footer { display: flex; gap: 12px; padding: 12px 28px 20px; }
.ai-footer-btn {
  flex: 1; padding: 12px; font-size: $font-size-xs; font-weight: $font-weight-medium;
  border-radius: $radius-md; cursor: pointer; border: none; transition: all .15s;
  display: flex; align-items: center; justify-content: center; gap: 8px;
  &.secondary { background: #f5f5f5; color: #777; &:hover { background: #e8e8e8; } }
  &.primary {
    background: linear-gradient(135deg, #818cf8, #6366f1); color: #fff;
    &:disabled { opacity: .6; cursor: not-allowed; }
  }
}
.ai-btn-loading {
  width: 14px; height: 14px; border: 2px solid rgba(255,255,255,.3);
  border-top-color: #fff; border-radius: $radius-full; animation: ai-spin .8s linear infinite;
}
@keyframes ai-spin { to { transform: rotate(360deg); } }

.ai-modal-note { padding: 0 28px 22px; font-size: 11px; color: #aaa; text-align: center; line-height: 1.6; }

.modal-fade-enter-active, .modal-fade-leave-active {
  transition: opacity .25s ease;
  .ai-modal { transition: transform .25s ease; }
}
.modal-fade-enter-from, .modal-fade-leave-to { opacity: 0;
  .ai-modal { transform: scale(.95) translateY(10px); }
}

@media (max-width: 520px) {
  .ai-modal { max-width: calc(100vw - 24px); margin: 0 8px; border-radius: $radius-xl; }
  .ai-modal-header { padding: 18px 18px 0; }
  .ai-modal-body { padding: 16px 18px 4px; }
  .ai-modal-footer { padding: 10px 18px 16px; flex-direction: column; }
  .ai-modal-note { padding: 0 18px 18px; }
  .ai-subject-chips { padding-left: 0; }
  .ai-config-row { padding-left: 0; flex-direction: column; gap: 16px; }
  .ai-analysis-preview { padding-left: 0; }
  .ai-preview-footer { padding-left: 0; }
}
</style>