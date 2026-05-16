<template>
  <div class="quick-panel">
    <h3 class="panel-title">常见问题</h3>
    <div class="quick-list">
      <button
        v-for="q in quickQuestions"
        :key="q.id"
        class="quick-item"
        @click="$emit('ask', q.text)"
      >
        <span class="quick-icon" v-html="q.icon"></span>
        <span class="quick-text">{{ q.text }}</span>
      </button>
    </div>

    <!-- 预约试听 -->
    <div class="trial-card">
      <h4 class="trial-title">&#127891; 预约试听课</h4>
      <p class="trial-desc">免费体验一节精讲课程，感受学习氛围</p>
      <div class="trial-form">
        <input
          :value="trialForm.name"
          class="trial-input"
          placeholder="您的姓名"
          @input="$emit('update:trialForm', { ...trialForm, name: $event.target.value })"
        />
        <input
          :value="trialForm.phone"
          class="trial-input"
          placeholder="手机号"
          @input="$emit('update:trialForm', { ...trialForm, phone: $event.target.value })"
        />
        <select
          :value="trialForm.course"
          class="trial-input"
          @change="$emit('update:trialForm', { ...trialForm, course: $event.target.value })"
        >
          <option v-for="c in trialCourses" :key="c.value" :value="c.value">{{ c.label }}</option>
        </select>
        <button class="trial-submit" @click="$emit('submitTrial')">
          {{ trialSubmitted ? '&#10003; 已提交' : '免费预约试听' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { QUICK_QUESTIONS, TRIAL_COURSES } from '@/constants/consultation'

defineProps({
  trialForm: { type: Object, required: true },
  trialSubmitted: { type: Boolean, default: false },
})

defineEmits(['ask', 'submitTrial', 'update:trialForm'])

const quickQuestions = QUICK_QUESTIONS
const trialCourses = TRIAL_COURSES
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.quick-panel {
  width: 280px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.panel-title {
  font-size: $font-size-lg;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  margin-bottom: 4px;
}

.quick-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quick-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  background: #fff;
  border: 1px solid #eee;
  border-radius: $radius-lg;
  cursor: pointer;
  transition: all $transition-fast;
  font-size: $font-size-base;
  text-align: left;
  &:hover { border-color: $color-primary; background: $color-primary-light; transform: translateX(4px); }
}

.quick-icon { font-size: 18px; width: 24px; text-align: center; }
.quick-text { color: $color-text-secondary; font-weight: $font-weight-medium; }

.trial-card {
  background: $color-primary;
  color: #fff;
  border-radius: $radius-2xl;
  padding: 20px;
}

.trial-title {
  font-size: $font-size-lg;
  font-weight: $font-weight-bold;
  margin-bottom: 4px;
}

.trial-desc {
  font-size: $font-size-sm;
  opacity: 0.85;
  margin-bottom: 14px;
}

.trial-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.trial-input {
  padding: 10px 12px;
  border: none;
  border-radius: $radius-md;
  font-size: $font-size-base;
  color: $color-text-primary;
  outline: none;
  &::placeholder { color: #aaa; }
}

.trial-submit {
  padding: 12px;
  background: #fff;
  color: $color-primary;
  border: none;
  border-radius: $radius-md;
  font-size: $font-size-md;
  font-weight: $font-weight-bold;
  cursor: pointer;
  transition: all $transition-fast;
  &:hover { background: #f0f5ff; }
}
</style>