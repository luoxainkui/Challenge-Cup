<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-slate-50 via-blue-50/30 to-indigo-50/40 px-4 py-8 relative overflow-hidden">
    <!-- ====== 浮动背景装饰 ====== -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <!-- 大光环 -->
      <div class="absolute -top-32 -right-32 w-[28rem] h-[28rem] bg-gradient-to-br from-indigo-400/15 via-purple-400/10 to-blue-400/15 rounded-full blur-3xl animate-float-slow"></div>
      <div class="absolute -bottom-32 -left-32 w-[28rem] h-[28rem] bg-gradient-to-tr from-blue-400/15 via-cyan-400/10 to-indigo-400/15 rounded-full blur-3xl animate-float-slow" style="animation-delay: 3s"></div>
      <!-- 小光点 -->
      <div class="absolute top-1/4 left-[15%] w-3 h-3 bg-indigo-400/30 rounded-full blur-sm animate-ping-slow"></div>
      <div class="absolute bottom-1/3 right-[20%] w-2 h-2 bg-purple-400/30 rounded-full blur-sm animate-ping-slow" style="animation-delay: 2s"></div>
      <div class="absolute top-[60%] left-[70%] w-2.5 h-2.5 bg-blue-400/30 rounded-full blur-sm animate-ping-slow" style="animation-delay: 4s"></div>
    </div>

    <div class="relative w-full max-w-md z-10">
      <!-- ====== 卡片 ====== -->
      <div class="relative bg-white/85 backdrop-blur-2xl rounded-3xl shadow-[0_25px_80px_rgba(0,0,0,0.12),0_0_0_1px_rgba(255,255,255,0.4)_inset] border border-white/60 p-8 sm:p-10 overflow-hidden">
        <!-- 顶部渐变装饰条 -->
        <div class="absolute top-0 left-0 right-0 h-1.5 rounded-t-3xl bg-gradient-to-r from-blue-400 via-indigo-500 to-purple-500"></div>
        <!-- 装饰光晕 -->
        <div class="absolute -top-12 -right-12 w-32 h-32 rounded-full bg-gradient-to-br from-indigo-400/6 to-purple-400/6 blur-2xl pointer-events-none"></div>

        <template v-if="mode === 'login' || mode === 'phone'">
          <!-- ====== 品牌头部 ====== -->
          <div class="text-center mb-7">
            <div class="relative inline-flex items-center justify-center">
              <div class="absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-400/20 via-indigo-400/15 to-purple-400/20 blur-md animate-pulse"></div>
              <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-blue-500 via-indigo-500 to-purple-600 flex items-center justify-center shadow-[0_8px_25px_rgba(79,70,229,0.3)]">
                <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" />
                </svg>
              </div>
            </div>
            <h2 class="text-[22px] font-bold text-slate-800 mt-5 mb-1.5 tracking-tight">
              {{ mode === 'phone' ? '手机号快捷登录' : '登录桂升通' }}
            </h2>
            <p class="text-sm text-slate-400">
              {{ mode === 'phone' ? '使用手机验证码快速登录' : '登录后即可访问完整功能' }}
            </p>
          </div>

          <!-- ====== 登录方式切换 Tab ====== -->
          <div class="flex bg-slate-100 rounded-xl p-1 mb-5">
            <button
              class="flex-1 py-2.5 text-sm font-medium rounded-[10px] transition-all duration-300"
              :class="mode === 'login' ? 'bg-white text-indigo-600 shadow-[0_2px_8px_rgba(0,0,0,0.06)]' : 'text-slate-500 hover:text-slate-700'"
              @click="mode = 'login'"
            >邮箱登录</button>
            <button
              class="flex-1 py-2.5 text-sm font-medium rounded-[10px] transition-all duration-300"
              :class="mode === 'phone' ? 'bg-white text-indigo-600 shadow-[0_2px_8px_rgba(0,0,0,0.06)]' : 'text-slate-500 hover:text-slate-700'"
              @click="mode = 'phone'"
            >手机登录</button>
          </div>

          <!-- ====== 邮箱登录表单 ====== -->
          <template v-if="mode === 'login'">
            <div class="mb-4">
              <div class="relative">
                <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none transition-colors duration-300 peer-focus:text-indigo-400">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75" />
                  </svg>
                </div>
                <input
                  v-model="loginForm.email"
                  type="email"
                  placeholder="请输入邮箱地址"
                  autocomplete="email"
                  class="input-field-page"
                  :class="{ 'input-error-page': loginError && !loginForm.email }"
                />
              </div>
            </div>

            <div class="mb-3">
              <div class="relative">
                <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                  </svg>
                </div>
                <input
                  v-model="loginForm.password"
                  type="password"
                  placeholder="请输入密码"
                  autocomplete="current-password"
                  class="input-field-page"
                  @keyup.enter="handleLogin"
                />
              </div>
            </div>

            <div class="text-right mb-3">
              <a href="#" class="text-xs text-indigo-500 no-underline hover:text-indigo-600 font-medium transition-colors" @click.prevent="mode = 'forgot'">忘记密码？</a>
            </div>
          </template>

          <!-- ====== 手机登录表单 ====== -->
          <template v-else>
            <div class="mb-4">
              <div class="relative">
                <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
                  <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3" />
                  </svg>
                </div>
                <input
                  v-model="phoneForm.phone"
                  type="tel"
                  placeholder="请输入手机号"
                  autocomplete="tel"
                  maxlength="11"
                  class="input-field-page pl-11"
                  @input="onPhoneInput"
                />
              </div>
            </div>

            <div class="mb-3">
              <div class="flex gap-2.5">
                <div class="relative flex-1">
                  <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
                    <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
                    </svg>
                  </div>
                  <input
                    v-model="phoneForm.code"
                    type="text"
                    placeholder="输入验证码"
                    maxlength="6"
                    autocomplete="off"
                    class="input-field-page pl-11"
                    @input="clearPhoneError"
                  />
                </div>
                <button
                  type="button"
                  class="code-btn-page flex-shrink-0"
                  :disabled="phoneCodeLoading || phoneCountdown > 0"
                  @click="handleSendPhoneCode"
                >
                  {{ phoneCountdown > 0 ? `${phoneCountdown}秒` : phoneCodeLoading ? '发送中...' : '获取验证码' }}
                </button>
              </div>
            </div>
            <p class="flex items-start gap-1.5 text-xs text-slate-400 text-center mb-3 leading-relaxed bg-blue-50/50 rounded-lg py-2 px-3">
              <span class="flex-shrink-0 mt-0.5">💡</span>
              <span>演示环境验证码：<strong class="text-indigo-500">123456</strong></span>
            </p>
          </template>

          <!-- 通用错误提示 -->
          <p v-if="loginError" class="text-[#ef4444] text-[13px] text-center mb-3 bg-red-50 rounded-lg py-2 px-3">{{ loginError }}</p>

          <!-- 登录按钮 -->
          <button
            class="submit-btn-page group"
            :disabled="loginLoading"
            @click="mode === 'login' ? handleLogin() : handlePhoneLogin()"
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

          <!-- 底部链接 -->
          <div class="flex flex-col items-center gap-2 mt-5">
            <p class="text-sm text-slate-500 m-0">
              没有账号？
              <router-link to="/register" class="text-indigo-500 no-underline font-semibold hover:text-indigo-600 transition-colors">去注册</router-link>
            </p>
          </div>
        </template>

        <!-- ====== 忘记密码 ====== -->
        <ForgotPassword v-else @back="mode = 'login'" @done="mode = 'login'" />
      </div>

      <!-- 底部版权 -->
      <p class="text-center text-xs text-slate-400 mt-6">© 2025 桂升通 · 用心服务每一位用户</p>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'
import { useCountdown } from '@/composables/useCountdown'
import ForgotPassword from '@/components/auth/ForgotPassword.vue'

const router = useRouter()
const authStore = useAuthStore()

const mode = ref('login')
const loginError = ref('')
const loginLoading = ref(false)

// 邮箱登录表单
const loginForm = reactive({
  email: '',
  password: '',
})

// 手机登录表单
const phoneForm = reactive({ phone: '', code: '' })
const phoneCodeLoading = ref(false)
const { countdown: phoneCountdown, start: startPhoneCountdown } = useCountdown(60)

function onPhoneInput() {
  phoneForm.phone = phoneForm.phone.replace(/\D/g, '')
  loginError.value = ''
}

function clearPhoneError() {
  loginError.value = ''
}

function validatePhone() {
  if (!phoneForm.phone.trim()) {
    loginError.value = '请输入手机号'
    return false
  }
  if (!/^1[3-9]\d{9}$/.test(phoneForm.phone.trim())) {
    loginError.value = '请输入正确的手机号'
    return false
  }
  return true
}

async function handleSendPhoneCode() {
  loginError.value = ''
  if (!validatePhone()) return

  phoneCodeLoading.value = true
  try {
    await authApi.sendCode(`${phoneForm.phone}@sms.local`)
    startPhoneCountdown()
  } catch (e) {
    loginError.value = e.message || '验证码发送失败，请重试'
  } finally {
    phoneCodeLoading.value = false
  }
}

async function handlePhoneLogin() {
  loginError.value = ''
  if (!validatePhone()) return
  if (!phoneForm.code.trim()) {
    loginError.value = '请输入验证码'
    return
  }
  if (phoneForm.code.trim() !== '123456') {
    loginError.value = '验证码错误（演示环境请输入 123456）'
    return
  }

  loginLoading.value = true
  try {
    const mockRes = {
      data: {
        access_token: 'demo-phone-token-' + Date.now(),
        user: {
          id: 0,
          username: '手机用户' + phoneForm.phone.slice(-4),
          email: phoneForm.phone + '@sms.local',
          phone: phoneForm.phone,
        },
      },
    }
    authStore.setAuth({ access_token: mockRes.data.access_token, user: mockRes.data.user })
    router.push('/')
  } catch (e) {
    loginError.value = e.message || '登录失败，请重试'
  } finally {
    loginLoading.value = false
  }
}

async function handleLogin() {
  loginError.value = ''
  if (!loginForm.email.trim()) {
    loginError.value = '请输入邮箱'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(loginForm.email.trim())) {
    loginError.value = '请输入正确的邮箱格式'
    return
  }
  if (!loginForm.password.trim()) {
    loginError.value = '请输入密码'
    return
  }
  loginLoading.value = true
  try {
    const res = await authApi.login({ email: loginForm.email.trim(), password: loginForm.password })
    authStore.setAuth({ access_token: res.data.access_token, user: res.data.user })
    router.push('/')
  } catch (e) {
    loginError.value = e.message || '登录失败，请重试'
  } finally {
    loginLoading.value = false
  }
}
</script>

<style scoped>
/* ====== 浮动动画 ====== */
@keyframes float-slow {
  0%, 100% { transform: translateY(0) scale(1); }
  50% { transform: translateY(-20px) scale(1.05); }
}
@keyframes ping-slow {
  0%, 100% { opacity: 0.3; transform: scale(1); }
  50% { opacity: 0.7; transform: scale(1.5); }
}
.animate-float-slow {
  animation: float-slow 8s ease-in-out infinite;
}
.animate-ping-slow {
  animation: ping-slow 4s ease-in-out infinite;
}

/* ====== 输入框 ====== */
.input-field-page {
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
.input-field-page::placeholder {
  color: #bcc4d0;
  font-size: 14px;
}
.input-field-page:hover {
  border-color: #cdd5df;
  background: #fafbfc;
}
.input-field-page:focus {
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.08), 0 1px 2px rgba(0,0,0,0.04);
}
.input-field-page.input-error-page {
  border-color: #ef4444;
  background: #fefafa;
}
.input-field-page.input-error-page:focus {
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
}

/* ====== 验证码按钮 ====== */
.code-btn-page {
  flex-shrink: 0;
  padding: 0 16px;
  border: 1.5px solid #6366f1;
  border-radius: 12px;
  background: #fff;
  color: #6366f1;
  font-size: 13px;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  letter-spacing: 0.3px;
}
.code-btn-page:hover:not(:disabled) {
  background: #6366f1;
  color: #fff;
  box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
  transform: translateY(-1px);
}
.code-btn-page:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  border-color: #cdd5df;
  color: #a1a1aa;
}

/* ====== 提交按钮 ====== */
.submit-btn-page {
  width: 100%;
  padding: 13px;
  background: linear-gradient(135deg, #6366f1 0%, #4f46e5 50%, #7c3aed 100%);
  color: #fff;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3), 0 1px 3px rgba(0,0,0,0.08);
  margin-top: 4px;
  letter-spacing: 0.5px;
  position: relative;
  overflow: hidden;
}
.submit-btn-page::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0.2) 0%, transparent 50%);
  opacity: 0;
  transition: opacity 0.35s ease;
}
.submit-btn-page:hover:not(:disabled)::before {
  opacity: 1;
}
.submit-btn-page:hover:not(:disabled) {
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 50%, #6d28d9 100%);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4), 0 2px 6px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.submit-btn-page:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(99, 102, 241, 0.25);
}
.submit-btn-page:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

</style>
