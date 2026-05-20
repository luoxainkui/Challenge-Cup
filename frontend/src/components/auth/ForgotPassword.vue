<template>
  <div>
    <!-- ====== 品牌头部 ====== -->
    <div class="text-center mb-7">
      <!-- 装饰 Logo -->
      <div class="relative inline-flex items-center justify-center">
        <div class="absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-amber-400/20 via-orange-400/15 to-rose-400/20 blur-md"></div>
        <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-amber-500 via-orange-500 to-rose-600 flex items-center justify-center shadow-[0_8px_25px_rgba(245,158,11,0.3)]">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 5.25a3 3 0 013 3m3 0a6 6 0 01-7.029 5.912c-.563-.097-1.159.026-1.563.43L10.5 17.25H8.25v2.25H6v2.25H2.25v-2.818c0-.597.237-1.17.659-1.591l6.499-6.499c.404-.404.527-1 .43-1.563A6 6 0 1121.75 8.25z" />
          </svg>
        </div>
      </div>
      <h2 class="text-[22px] font-bold text-slate-800 mt-5 mb-1.5 tracking-tight">重置密码</h2>
      <p class="text-sm text-slate-400">通过邮箱验证重置您的密码</p>
    </div>

    <!-- 步骤 1：输入邮箱 -->
    <div v-if="step === 1">
      <div class="mb-4">
        <div class="relative">
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
            </svg>
          </div>
          <input
            v-model="form.email"
            type="email"
            placeholder="请输入注册邮箱"
            class="input-field pl-11"
            @input="error = ''"
          />
        </div>
      </div>
      <p v-if="error" class="form-message form-message--error">{{ error }}</p>
      <p class="flex items-start gap-1.5 text-xs text-slate-400 mb-4 leading-relaxed bg-blue-50/50 rounded-lg py-2 px-3">
        <span class="flex-shrink-0 mt-0.5">💡</span>
        <span>验证码将发送到您的注册邮箱，请注意查收（如未收到请检查垃圾箱）</span>
      </p>
      <button class="form-btn" :disabled="sending" @click="handleSendCode">
        <span v-if="sending" class="inline-flex items-center gap-2">
          <svg class="animate-spin w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
          </svg>
          发送中...
        </span>
        <span v-else>获取验证码</span>
      </button>
      <div class="text-center mt-5">
        <a href="#" class="text-sm text-slate-400 no-underline hover:text-indigo-500 transition-colors font-medium" @click.prevent="emit('back')">← 返回登录</a>
      </div>
    </div>

    <!-- 步骤 2：验证码 + 新密码 -->
    <div v-else>
      <div class="mb-4">
        <div class="relative">
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
            </svg>
          </div>
          <input
            v-model="form.email"
            type="email"
            disabled
            class="input-field input-disabled pl-11"
          />
        </div>
      </div>

      <div class="mb-4 flex gap-2.5">
        <div class="relative flex-1">
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
            </svg>
          </div>
          <input
            v-model="form.code"
            type="text"
            placeholder="输入验证码"
            class="input-field pl-11"
            @input="error = ''"
          />
        </div>
        <button
          class="code-btn flex-shrink-0"
          :disabled="sending || countdown > 0"
          @click="handleSendCode"
        >
          {{ countdown > 0 ? `${countdown}s 后重发` : '重新发送' }}
        </button>
      </div>

      <div class="mb-4">
        <div class="relative">
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
            </svg>
          </div>
          <input
            v-model="form.password"
            type="password"
            placeholder="设置新密码（不少于6位）"
            class="input-field pl-11"
            @input="error = ''"
          />
        </div>
      </div>

      <div class="mb-2">
        <div class="relative">
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
            </svg>
          </div>
          <input
            v-model="form.confirmPassword"
            type="password"
            placeholder="确认新密码"
            class="input-field pl-11"
            @keyup.enter="handleReset"
          />
        </div>
      </div>

      <p v-if="error" class="form-message form-message--error">{{ error }}</p>
      <p v-if="success" class="form-message form-message--success">{{ success }}</p>

      <button class="form-btn" :disabled="resetting" @click="handleReset">
        <span v-if="resetting" class="inline-flex items-center gap-2">
          <svg class="animate-spin w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
          </svg>
          重置中...
        </span>
        <span v-else>重置密码</span>
      </button>

      <div class="text-center mt-5">
        <a href="#" class="text-sm text-slate-400 no-underline hover:text-indigo-500 transition-colors font-medium" @click.prevent="emit('back')">← 返回登录</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { authApi } from '@/api/auth'
import { useCountdown } from '@/composables/useCountdown'

const emit = defineEmits(['back', 'done'])

const step = ref(1)
const error = ref('')
const success = ref('')
const sending = ref(false)
const resetting = ref(false)
const { countdown, start: startCountdown, stop: stopCountdown } = useCountdown()

const form = reactive({
  email: '',
  code: '',
  password: '',
  confirmPassword: '',
})

function resetState() {
  step.value = 1
  error.value = ''
  success.value = ''
  stopCountdown()
  form.email = ''
  form.code = ''
  form.password = ''
  form.confirmPassword = ''
}

async function handleSendCode() {
  error.value = ''
  if (!form.email.trim()) {
    error.value = '请输入邮箱'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) {
    error.value = '请输入正确的邮箱格式'
    return
  }
  sending.value = true
  try {
    await authApi.sendCode(form.email.trim())
    if (step.value === 1) step.value = 2
    startCountdown()
    success.value = '验证码已发送，请查看终端控制台'
  } catch (e) {
    error.value = e.message || '验证码发送失败，请重试'
  } finally {
    sending.value = false
  }
}

async function handleReset() {
  error.value = ''
  success.value = ''
  if (!form.code.trim()) {
    error.value = '请输入验证码'
    return
  }
  if (!form.password.trim() || form.password.length < 6) {
    error.value = '新密码不能少于6位'
    return
  }
  if (form.password !== form.confirmPassword) {
    error.value = '两次输入的密码不一致'
    return
  }
  resetting.value = true
  try {
    await authApi.resetPassword(form.email.trim(), form.code.trim(), form.password)
    success.value = '密码重置成功！即将跳转到登录页...'
    setTimeout(() => {
      emit('done')
      resetState()
    }, 2000)
  } catch (e) {
    error.value = e.message || '密码重置失败，请重试'
  } finally {
    resetting.value = false
  }
}

defineExpose({ resetState })
</script>

<style scoped>
/* ====== 输入框 ====== */
.input-field {
  width: 100%;
  padding: 13px 15px;
  border: 1.5px solid #e8ecf1;
  border-radius: 12px;
  font-size: 15px;
  background: #f8fafb;
  outline: none;
  transition: all 0.3s ease;
  box-sizing: border-box;
  color: #334155;
}
.input-field::placeholder {
  color: #bcc4d0;
  font-size: 14px;
}
.input-field:hover {
  border-color: #cdd5df;
  background: #fafbfc;
}
.input-field:focus {
  border-color: #f59e0b;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(245, 158, 11, 0.08), 0 1px 2px rgba(0,0,0,0.04);
}
.input-field.input-disabled {
  background: #f1f5f9;
  color: #94a3b8;
  cursor: not-allowed;
}
.input-field.input-disabled:hover {
  border-color: #e8ecf1;
}

/* ====== 验证码按钮 ====== */
.code-btn {
  flex-shrink: 0;
  padding: 0 16px;
  border: 1.5px solid #f59e0b;
  border-radius: 12px;
  background: #fff;
  color: #f59e0b;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.code-btn:hover:not(:disabled) {
  background: #f59e0b;
  color: #fff;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
  transform: translateY(-1px);
}
.code-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  border-color: #cdd5df;
  color: #a1a1aa;
}

/* ====== 提示消息 ====== */
.form-message {
  font-size: 13px;
  margin-bottom: 12px;
  text-align: center;
  border-radius: 10px;
  padding: 9px 12px;
}
.form-message--error {
  color: #ef4444;
  background: #fef2f2;
}
.form-message--success {
  color: #10b981;
  background: #ecfdf5;
}

/* ====== 提交按钮 ====== */
.form-btn {
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg, #f59e0b 0%, #d97706 50%, #ea580c 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 20px rgba(245, 158, 11, 0.3), 0 1px 3px rgba(0,0,0,0.08);
  letter-spacing: 0.5px;
  position: relative;
  overflow: hidden;
}
.form-btn::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 50%);
  opacity: 0;
  transition: opacity 0.35s ease;
}
.form-btn:hover:not(:disabled)::before {
  opacity: 1;
}
.form-btn:hover:not(:disabled) {
  background: linear-gradient(135deg, #d97706 0%, #b45309 50%, #c2410c 100%);
  box-shadow: 0 8px 30px rgba(245, 158, 11, 0.4), 0 2px 6px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.form-btn:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(245, 158, 11, 0.25);
}
.form-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}
</style>