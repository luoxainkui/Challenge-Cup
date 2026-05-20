<template>
  <Transition name="modal-fade">
    <div
      v-if="visible"
      class="fixed inset-0 z-[9999] flex items-center justify-center"
      @click.self="handleOverlayClick"
    >
      <!-- 多层蒙层背景 -->
      <div class="absolute inset-0 bg-gradient-to-br from-slate-900/60 via-slate-800/50 to-blue-900/60 backdrop-blur-[8px]"></div>
      <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-blue-400/10 via-transparent to-purple-400/10"></div>

      <!-- ====== 弹窗卡片 ====== -->
      <div class="modal-card relative w-full max-w-[440px] mx-5 max-h-[90vh] overflow-y-auto rounded-2xl bg-white/95 backdrop-blur-xl shadow-[0_25px_80px_rgba(0,0,0,0.2),0_0_0_1px_rgba(255,255,255,0.3)_inset] px-8 py-10">

        <!-- 顶部装饰渐变条 -->
        <div class="absolute top-0 left-0 right-0 h-1 rounded-t-2xl bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500"></div>

        <!-- 装饰圆环 -->
        <div class="absolute -top-16 -right-16 w-40 h-40 rounded-full bg-gradient-to-br from-blue-400/8 to-indigo-500/8 blur-2xl pointer-events-none"></div>
        <div class="absolute -bottom-10 -left-10 w-32 h-32 rounded-full bg-gradient-to-tr from-purple-400/6 to-blue-400/6 blur-2xl pointer-events-none"></div>

        <!-- 关闭按钮 -->
        <button
          class="absolute top-4 right-4 w-8 h-8 flex items-center justify-center rounded-full bg-slate-100/80 hover:bg-slate-200 text-slate-400 hover:text-slate-600 transition-all duration-200 hover:scale-110 border-none cursor-pointer z-10"
          @click="handleClose"
        >
          <svg xmlns="http://www.w3.org/2000/svg" class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>

        <!-- ====== 登录模式 ====== -->
        <template v-if="mode === 'login'">
          <LoginForm
            @switch-tab="switchTab"
            @forgot="mode = 'forgot'"
            @success="handleLoginSuccess"
          />
        </template>

        <!-- ====== 手机号快捷登录模式 ====== -->
        <template v-else-if="mode === 'phone'">
          <PhoneLoginForm
            @switch-tab="switchTab"
            @success="handleLoginSuccess"
          />
        </template>

        <!-- ====== 忘记密码模式（内嵌组件） ====== -->
        <template v-else-if="mode === 'forgot'">
          <ForgotPassword
            @back="mode = 'login'"
            @done="mode = 'login'"
          />
        </template>
      </div>
    </div>
  </Transition>
</template>

<script setup>
/**
 * LoginModal — 登录弹窗（主容器）
 * 负责：弹窗显隐、蒙层点击关闭、动画、模式切换调度
 */
import { ref, watch } from 'vue'
import { useAuthStore } from '@/stores/auth'
import ForgotPassword from '@/components/auth/ForgotPassword.vue'
import LoginForm from './LoginForm.vue'
import PhoneLoginForm from './PhoneLoginForm.vue'

const props = defineProps({
  visible: { type: Boolean, default: false },
})
const emit = defineEmits(['close', 'logged-in'])

const authStore = useAuthStore()
const mode = ref('login') // 'login' | 'phone' | 'forgot'

// 弹窗打开时重置到默认登录模式
watch(() => props.visible, (v) => {
  if (v) {
    mode.value = 'login'
  }
})

function switchTab(tab) {
  mode.value = tab
}

function handleLoginSuccess() {
  emit('logged-in')
}

function handleOverlayClick() {
  handleClose()
}

function handleClose() {
  authStore.clearLoginRequired()
  emit('close')
}
</script>

<style scoped>
/* ====== 弹窗淡入淡出动画 ====== */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

/* 卡片动画 — 平滑下落/上移 + 缩放 */
.modal-fade-enter-active .modal-card {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.modal-fade-leave-active .modal-card {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
.modal-fade-enter-from .modal-card {
  transform: translateY(32px) scale(0.96);
  opacity: 0;
}
.modal-fade-leave-to .modal-card {
  transform: translateY(-20px) scale(0.96);
  opacity: 0;
}

/* 卡片滚动条美化 */
.modal-card::-webkit-scrollbar {
  width: 4px;
}
.modal-card::-webkit-scrollbar-thumb {
  background: #d1d5db;
  border-radius: 4px;
}
</style>