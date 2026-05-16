<template>
  <div class="chat-panel">
    <div ref="chatBody" class="chat-body">
      <div
        v-for="(msg, i) in messages"
        :key="i"
        :class="['chat-bubble', msg.role === 'user' ? 'chat-user' : 'chat-ai']"
      >
        <div class="chat-avatar">
          {{ msg.role === 'user' ? '&#128100;' : '&#129302;' }}
        </div>
        <div class="chat-content">
          <span class="chat-role">{{ msg.role === 'user' ? '我' : 'AI 助手' }}</span>
          <div class="chat-text" v-html="msg.text"></div>
          <!-- 回填联系方式表单 -->
          <div v-if="msg.showContact && !contactSubmitted" class="contact-form">
            <input
              :value="contactForm.name"
              class="cform-input"
              placeholder="您的姓名"
              @input="$emit('update:contactForm', { ...contactForm, name: $event.target.value })"
            />
            <input
              :value="contactForm.phone"
              class="cform-input"
              placeholder="手机号"
              @input="$emit('update:contactForm', { ...contactForm, phone: $event.target.value })"
            />
            <button class="cform-submit" @click="$emit('submitContact')">提交</button>
          </div>
        </div>
      </div>

      <!-- 打字中 -->
      <div v-if="typing" class="chat-bubble chat-ai">
        <div class="chat-avatar">&#129302;</div>
        <div class="chat-content">
          <span class="typing-dots"><span></span><span></span><span></span></span>
        </div>
      </div>
    </div>

    <!-- 输入框 -->
    <div class="chat-input-area">
      <textarea
        :value="inputText"
        class="chat-textarea"
        placeholder="输入你的问题..."
        rows="2"
        @input="$emit('update:inputText', $event.target.value)"
        @keydown.enter.exact.prevent="$emit('send')"
      ></textarea>
      <button class="chat-send" @click="$emit('send')">发送</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  messages: { type: Array, required: true },
  typing: { type: Boolean, default: false },
  contactForm: { type: Object, required: true },
  contactSubmitted: { type: Boolean, default: false },
  inputText: { type: String, default: '' },
})

defineEmits(['send', 'submitContact', 'update:inputText', 'update:contactForm'])

defineExpose({ chatBody: null })
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.chat-panel {
  flex: 1;
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.chat-body {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 16px;
  background: #f9fafb;
  border-radius: $radius-2xl;
  margin-bottom: 16px;
  min-height: 500px;
}

.chat-bubble {
  display: flex;
  gap: 10px;
  max-width: 85%;
  &.chat-ai { align-self: flex-start; }
  &.chat-user { align-self: flex-end; flex-direction: row-reverse; }
}

.chat-avatar {
  width: 36px; height: 36px;
  border-radius: $radius-round;
  display: flex; align-items: center; justify-content: center;
  font-size: 20px; flex-shrink: 0;
  .chat-ai & { background: $color-primary-light; }
  .chat-user & { background: #e0e7ff; }
}

.chat-content {
  .chat-ai & {
    background: #fff;
    border-radius: 0 $radius-2xl $radius-2xl $radius-2xl;
    box-shadow: 0 1px 4px rgba(0,0,0,.05);
  }
  .chat-user & {
    background: $color-primary;
    color: #fff;
    border-radius: $radius-2xl 0 $radius-2xl $radius-2xl;
  }
  padding: 12px 16px;
}

.chat-role {
  font-size: $font-size-xs;
  opacity: 0.6;
  display: block;
  margin-bottom: 4px;
}

.chat-text {
  font-size: $font-size-base;
  line-height: 1.7;
  :deep(strong) { color: inherit; font-weight: $font-weight-bold; }
  :deep(em) { opacity: .7; }
}

// 内嵌联系表单
.contact-form {
  margin-top: 12px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  .cform-input {
    flex: 1; min-width: 100px;
    padding: 8px 10px;
    border: 1px solid #ddd;
    border-radius: $radius-md;
    font-size: $font-size-sm;
    outline: none;
    &:focus { border-color: $color-primary; }
  }
  .cform-submit {
    padding: 8px 16px;
    background: $color-primary;
    color: #fff; border: none;
    border-radius: $radius-md;
    cursor: pointer;
    &:hover { background: $color-primary-dark; }
  }
}

// 打字动画
.typing-dots {
  display: flex; gap: 4px; padding: 4px 0;
  span {
    width: 8px; height: 8px;
    background: #ccc;
    border-radius: $radius-round;
    animation: dotBounce 1.4s infinite ease-in-out both;
    &:nth-child(1) { animation-delay: -.32s; }
    &:nth-child(2) { animation-delay: -.16s; }
    &:nth-child(3) { animation-delay: 0s; }
  }
}
@keyframes dotBounce {
  0%, 80%, 100% { transform: scale(0); }
  40% { transform: scale(1); }
}

// 输入区域
.chat-input-area {
  display: flex; gap: 12px;
  background: #fff;
  border: 1px solid #eee;
  border-radius: $radius-2xl;
  padding: 12px 16px;
}

.chat-textarea {
  flex: 1;
  border: none;
  outline: none;
  resize: none;
  font-size: $font-size-base;
  font-family: inherit;
  line-height: 1.5;
  &::placeholder { color: #bbb; }
}

.chat-send {
  align-self: flex-end;
  padding: 10px 24px;
  background: $color-primary;
  color: #fff;
  border: none;
  border-radius: $radius-lg;
  font-size: $font-size-base;
  font-weight: $font-weight-bold;
  cursor: pointer;
  transition: background $transition-fast;
  &:hover { background: $color-primary-dark; }
}

// 响应式
@media (max-width: 768px) {
  .chat-bubble { max-width: 95%; }
  .chat-body { min-height: 400px; }
}
</style>