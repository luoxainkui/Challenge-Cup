<template>
  <div>
    <!-- ====== 品牌头部 ====== -->
    <div class="text-center mb-7">
      <!-- 装饰 Logo -->
      <div class="relative inline-flex items-center justify-center">
        <div class="absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-400/20 via-teal-400/15 to-cyan-400/20 blur-md animate-pulse"></div>
        <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-emerald-500 via-teal-500 to-cyan-600 flex items-center justify-center shadow-[0_8px_25px_rgba(20,184,166,0.3)]">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
          </svg>
        </div>
      </div>
      <h2 class="text-[22px] font-bold text-slate-800 mt-5 mb-1.5 tracking-tight">手机号快捷登录</h2>
      <p class="text-sm text-slate-400">使用手机验证码快速登录</p>
    </div>

    <!-- ====== 表单 ====== -->
    <div class="mb-4">
      <div class="relative">
        <!-- 手机图标 -->
        <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
          </svg>
        </div>
        <input
          v-model="form.phone"
          type="tel"
          placeholder="请输入手机号"
          autocomplete="tel"
          maxlength="11"
          class="input-field pl-11"
          :class="{ 'input-error': errors.phone }"
          @input="onPhoneInput"
        />
      </div>
      <p v-if="errors.phone" class="field-error">{{ errors.phone }}</p>
    </div>

    <div class="mb-3">
      <div class="flex gap-2.5">
        <div class="relative flex-1">
          <!-- 验证码图标 -->
          <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
            </svg>
          </div>
          <input
            v-model="form.code"
            type="text"
            placeholder="输入验证码"
            maxlength="6"
            autocomplete="off"
            class="input-field pl-11"
            :class="{ 'input-error': errors.code }"
            @input="clearFieldError('code')"
          />
        </div>
        <button
          type="button"
          class="code-btn flex-shrink-0"
          :disabled="codeLoading || countdown > 0"
          @click="handleSendCode"
        >
          {{ countdown > 0 ? `${countdown}秒` : codeLoading ? '发送中...' : '获取验证码' }}
        </button>
      </div>
      <p v-if="errors.code" class="field-error">{{ errors.code }}</p>
    </div>

    <!-- 通用错误/成功提示 -->
    <p v-if="loginError" class="text-[#ef4444] text-[13px] text-center mb-3 bg-red-50 rounded-lg py-2 px-3">{{ loginError }}</p>
    <p v-if="successMsg" class="text-[#10b981] text-[13px] text-center mb-3 bg-emerald-50 rounded-lg py-2 px-3">{{ successMsg }}</p>
    <p class="flex items-start gap-1.5 text-xs text-slate-400 text-center mb-3 leading-relaxed bg-blue-50/50 rounded-lg py-2 px-3">
      <span class="flex-shrink-0 mt-0.5">💡</span>
      <span>验证码将发送至您的手机，请注意查收。演示环境验证码：<strong class="text-indigo-500">123456</strong></span>
    </p>

    <!-- 登录按钮 -->
    <button
      class="form-btn group"
      :disabled="loginLoading"
      @click="handleLogin"
    >
      <span v-if="loginLoading" class="inline-flex items-center gap-2">
        <svg class="animate-spin w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
        </svg>
        登录中...
      </span>
      <span v-else>登 录</span>
    </button>

    <!-- ====== 底部链接 ====== -->
    <div class="flex flex-col items-center gap-2 mt-5">
      <p class="text-sm text-slate-500 m-0">
        没有账号？
        <router-link to="/register" class="text-teal-500 no-underline font-semibold hover:text-teal-600 transition-colors" @click="handleRegisterClick">去注册</router-link>
      </p>
      <a
        href="#"
        class="text-sm text-teal-500 no-underline hover:text-teal-600 font-medium transition-colors"
        @click.prevent="$emit('switch-tab', 'login')"
      >← 邮箱密码登录</a>
    </div>
  </div>
</template>

<script setup>
/**
 * PhoneLoginForm — 手机号验证码快捷登录
 * 功能：手机号格式校验、验证码倒计时、实时错误提示、加载状态
 *
 * 对接后端说明：
 *   - 生产环境需后端提供 /auth/phone-login 和 /auth/send-sms 两个接口
 *   - 当前 sendCode 使用 authApi.sendCode（发送邮箱验证码），仅作演示
 *   - 演示环境可直接使用验证码 123456
 */
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'
import { useCountdown } from '@/composables/useCountdown'

const emit = defineEmits(['switch-tab', 'success'])
const router = useRouter()
const authStore = useAuthStore()

const form = reactive({ phone: '', code: '' })
const errors = reactive({ phone: '', code: '' })
const loginError = ref('')
const successMsg = ref('')
const loginLoading = ref(false)
const codeLoading = ref(false)
const { countdown, start: startCountdown } = useCountdown(60)

function clearFieldError(field) {
  errors[field] = ''
  loginError.value = ''
}

function onPhoneInput() {
  // 只允许数字
  form.phone = form.phone.replace(/\D/g, '')
  clearFieldError('phone')
}

function validate() {
  let valid = true
  // 手机号校验：中国大陆手机号正则
  if (!form.phone.trim()) {
    errors.phone = '请输入手机号'
    valid = false
  } else if (!/^1[3-9]\d{9}$/.test(form.phone.trim())) {
    errors.phone = '请输入正确的手机号'
    valid = false
  } else {
    errors.phone = ''
  }
  // 验证码校验
  if (!form.code.trim()) {
    errors.code = '请输入验证码'
    valid = false
  } else if (!/^\d{4,6}$/.test(form.code.trim())) {
    errors.code = '验证码为4-6位数字'
    valid = false
  } else {
    errors.code = ''
  }
  return valid
}

async function handleSendCode() {
  loginError.value = ''
  successMsg.value = ''
  // 先校验手机号
  if (!form.phone.trim()) {
    errors.phone = '请输入手机号'
    return
  }
  if (!/^1[3-9]\d{9}$/.test(form.phone.trim())) {
    errors.phone = '请输入正确的手机号'
    return
  }
  errors.phone = ''

  codeLoading.value = true
  try {
    // TODO: 生产环境需改为调用 /auth/send-sms { phone }
    // 当前演示：复用邮箱验证码接口（使用模拟邮箱格式传递手机号+@sms.local）
    await authApi.sendCode(`${form.phone}@sms.local`)
    startCountdown()
    successMsg.value = '验证码已发送（演示环境验证码：123456）'
  } catch (e) {
    loginError.value = e.message || '验证码发送失败，请重试'
  } finally {
    codeLoading.value = false
  }
}

async function handleLogin() {
  loginError.value = ''
  successMsg.value = ''
  if (!validate()) return

  loginLoading.value = true
  try {
    // TODO: 生产环境需改为调用 /auth/phone-login { phone, code }
    // 当前演示：验证码 123456 直接通过
    if (form.code.trim() !== '123456') {
      throw new Error('验证码错误（演示环境请输入 123456）')
    }

    // 演示通过后，模拟后端返回 token
    const mockRes = {
      data: {
        access_token: 'demo-phone-token-' + Date.now(),
        user: {
          id: 0,
          username: '手机用户' + form.phone.slice(-4),
          email: form.phone + '@sms.local',
          phone: form.phone,
        },
      },
    }
    authStore.setAuth({ access_token: mockRes.data.access_token, user: mockRes.data.user })
    const redirect = authStore.popRedirectPath()
    emit('success')
    if (redirect) {
      router.push(redirect)
    }
  } catch (e) {
    loginError.value = e.message || '登录失败，请重试'
  } finally {
    loginLoading.value = false
  }
}

function handleRegisterClick() {
  authStore.clearLoginRequired()
}

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
  border-color: #14b8a6;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(20, 184, 166, 0.08), 0 1px 2px rgba(0,0,0,0.04);
}
.input-field.input-error {
  border-color: #ef4444;
  background: #fefafa;
}
.input-field.input-error:focus {
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
}

/* ====== 验证码按钮 ====== */
.code-btn {
  flex-shrink: 0;
  padding: 0 16px;
  border: 1.5px solid #14b8a6;
  border-radius: 12px;
  background: #fff;
  color: #14b8a6;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  letter-spacing: 0.3px;
}
.code-btn:hover:not(:disabled) {
  background: #14b8a6;
  color: #fff;
  box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3);
  transform: translateY(-1px);
}
.code-btn:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  border-color: #cdd5df;
  color: #a1a1aa;
}

/* ====== 字段错误提示 ====== */
.field-error {
  color: #ef4444;
  font-size: 12px;
  margin: 5px 0 0 4px;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 4px;
}

/* ====== 提交按钮 ====== */
.form-btn {
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg, #14b8a6 0%, #0d9488 50%, #0891b2 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 20px rgba(20, 184, 166, 0.3), 0 1px 3px rgba(0,0,0,0.08);
  margin-top: 4px;
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
  background: linear-gradient(135deg, #0d9488 0%, #0f766e 50%, #0e7490 100%);
  box-shadow: 0 8px 30px rgba(20, 184, 166, 0.4), 0 2px 6px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.form-btn:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(20, 184, 166, 0.25);
}
.form-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

</style>