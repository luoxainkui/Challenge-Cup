<template>
  <div class="page-container">
    <div class="service-hero">
      <span class="service-hero-icon">&#128172;</span>
      <h1 class="service-hero-title">在线咨询</h1>
      <p class="service-hero-desc">AI 智能助手 24 小时在线，专升本政策、报考时间、课程区别、价格咨询，随时随地秒答。支持留联系方式、预约试听课。</p>
    </div>

    <div class="back-row">
      <button class="back-btn" @click="$router.back()">&#8592; 返回</button>
    </div>

    <section class="consult-layout">
      <QuickPanel
        :trial-form="trialForm"
        :trial-submitted="trialSubmitted"
        @ask="sendMessage"
        @submit-trial="submitTrial"
        @update:trial-form="Object.assign(trialForm, $event)"
      />
      <ChatPanel
        ref="chatPanelRef"
        :messages="messages"
        :typing="typing"
        :contact-form="contactForm"
        :contact-submitted="contactSubmitted"
        :input-text="inputText"
        @send="sendMessage()"
        @submit-contact="submitContact"
        @update:input-text="inputText = $event"
        @update:contact-form="Object.assign(contactForm, $event)"
      />
    </section>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import QuickPanel from '@/components/consultation/QuickPanel.vue'
import ChatPanel from '@/components/consultation/ChatPanel.vue'
import { useConsultation } from '@/composables/useConsultation'

const chatPanelRef = ref(null)
const chatBody = ref(null)

// ChatPanel 挂载后获取内部 chatBody 元素
watch(chatPanelRef, (panel) => {
  if (panel?.chatBody) chatBody.value = panel.chatBody
})

const {
  inputText,
  typing,
  contactSubmitted,
  trialSubmitted,
  messages,
  trialForm,
  contactForm,
  sendMessage,
  submitContact,
  submitTrial,
} = useConsultation(chatBody)
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.service-hero {
  text-align: center;
  padding: 40px 20px 20px;
  &-icon { font-size: 48px; display: block; margin-bottom: 12px; }
  &-title { font-size: $font-size-5xl; font-weight: $font-weight-bold; margin-bottom: 10px; }
  &-desc { font-size: $font-size-md; color: $color-text-secondary; max-width: 700px; margin: 0 auto; line-height: 1.6; }
}

.back-row { margin-bottom: 20px; }
.back-btn {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 18px; border: 1px solid #ddd;
  background: #fff; border-radius: $radius-lg;
  font-size: $font-size-base; cursor: pointer;
  transition: all $transition-fast;
  &:hover { border-color: $color-primary; color: $color-primary; }
}

.consult-layout {
  display: flex; gap: 24px;
  align-items: flex-start;
  @media (max-width: 768px) { flex-direction: column; }
}
</style>