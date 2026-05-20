<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-emerald-50/50 via-teal-50/30 to-cyan-50/40 px-4 py-8 relative overflow-hidden">
    <!-- 浮动背景装饰 -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-32 -right-32 w-[28rem] h-[28rem] bg-gradient-to-br from-emerald-400/15 via-teal-400/10 to-cyan-400/15 rounded-full blur-3xl animate-float-slow"></div>
      <div class="absolute -bottom-32 -left-32 w-[28rem] h-[28rem] bg-gradient-to-tr from-teal-400/15 via-emerald-400/10 to-cyan-400/15 rounded-full blur-3xl animate-float-slow" style="animation-delay: 3s"></div>
      <div class="absolute top-1/4 left-[15%] w-3 h-3 bg-emerald-400/30 rounded-full blur-sm animate-ping-slow"></div>
      <div class="absolute bottom-1/3 right-[20%] w-2 h-2 bg-teal-400/30 rounded-full blur-sm animate-ping-slow" style="animation-delay: 2s"></div>
      <div class="absolute top-[60%] left-[70%] w-2.5 h-2.5 bg-cyan-400/30 rounded-full blur-sm animate-ping-slow" style="animation-delay: 4s"></div>
    </div>

    <div class="relative w-full max-w-md z-10">
      <!-- 卡片 -->
      <div class="relative bg-white/85 backdrop-blur-2xl rounded-3xl shadow-[0_25px_80px_rgba(0,0,0,0.12),0_0_0_1px_rgba(255,255,255,0.4)_inset] border border-white/60 p-8 sm:p-10 overflow-hidden">
        <!-- 顶部渐变装饰条 -->
        <div class="absolute top-0 left-0 right-0 h-1.5 rounded-t-3xl bg-gradient-to-r from-emerald-400 via-teal-500 to-cyan-500"></div>
        <!-- 装饰光晕 -->
        <div class="absolute -top-12 -right-12 w-32 h-32 rounded-full bg-gradient-to-br from-emerald-400/6 to-cyan-400/6 blur-2xl pointer-events-none"></div>

        <!-- 品牌头部 -->
        <div class="text-center mb-7">
          <div class="relative inline-flex items-center justify-center">
            <div class="absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-emerald-400/20 via-teal-400/15 to-cyan-400/20 blur-md animate-pulse"></div>
            <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-emerald-500 via-teal-500 to-cyan-600 flex items-center justify-center shadow-[0_8px_25px_rgba(20,184,166,0.3)]">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.8">
                <path stroke-linecap="round" stroke-linejoin="round" d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
              </svg>
            </div>
          </div>
          <h2 class="text-[22px] font-bold text-slate-800 mt-5 mb-1.5 tracking-tight">注册桂升通</h2>
          <p class="text-sm text-slate-400">创建您的学习账户</p>
        </div>

        <!-- 表单：用户名 -->
        <div class="mb-4">
          <div class="relative">
            <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
              </svg>
            </div>
            <input
              v-model="form.username"
              type="text"
              placeholder="请输入用户名"
              autocomplete="username"
              class="input-field-page"
              :class="{ 'input-error-page': error && !form.username }"
            />
          </div>
        </div>

        <!-- 邮箱 -->
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
              placeholder="请输入邮箱地址"
              autocomplete="email"
              class="input-field-page"
              :class="{ 'input-error-page': error && !form.email }"
            />
          </div>
        </div>

        <!-- 验证码 + 发送按钮 -->
        <div class="mb-4">
          <div class="flex gap-2.5">
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
                maxlength="6"
                autocomplete="off"
                class="input-field-page"
                :class="{ 'input-error-page': error && !form.code }"
              />
            </div>
            <button
              type="button"
              class="code-btn-page flex-shrink-0"
              :disabled="codeLoading || codeCountdown > 0"
              @click="handleSendCode"
            >
              {{ codeCountdown > 0 ? `${codeCountdown}秒` : codeLoading ? '发送中...' : '获取验证码' }}
            </button>
          </div>
        </div>

        <!-- 密码 -->
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
              placeholder="设置密码（不少于6位）"
              autocomplete="new-password"
              class="input-field-page"
              :class="{ 'input-error-page': error && !form.password }"
            />
          </div>
        </div>

        <!-- 确认密码 -->
        <div class="mb-3">
          <div class="relative">
            <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
              <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
              </svg>
            </div>
            <input
              v-model="form.confirmPassword"
              type="password"
              placeholder="确认密码"
              autocomplete="new-password"
              class="input-field-page"
              :class="{ 'input-error-page': error && !form.confirmPassword }"
            />
          </div>
        </div>

        <!-- 提示信息 -->
        <p v-if="error" class="text-[#ef4444] text-[13px] text-center mb-3 bg-red-50 rounded-lg py-2 px-3">{{ error }}</p>
        <p v-if="success" class="text-[#10b981] text-[13px] text-center mb-3 bg-emerald-50 rounded-lg py-2 px-3">{{ success }}</p>
        <p class="flex items-start gap-1.5 text-xs text-slate-400 text-center mb-4 leading-relaxed bg-blue-50/50 rounded-lg py-2 px-3">
          <span class="flex-shrink-0 mt-0.5">💡</span>
          <span>验证码将发送到您的注册邮箱，请注意查收（如未收到请查看终端控制台）</span>
        </p>

        <!-- 注册按钮 -->
        <button
          class="submit-btn-page submit-btn-page--teal group"
          :disabled="loading"
          @click="handleRegister"
        >
          <span v-if="loading" class="inline-flex items-center gap-2">
            <svg class="animate-spin w-4 h-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"></path>
            </svg>
            注册中...
          </span>
          <span v-else>注 册</span>
        </button>

        <!-- 底部链接 -->
        <div class="text-center mt-6">
          <p class="text-sm text-slate-500 m-0">
            已有账号？
            <router-link to="/login" class="text-teal-500 no-underline font-semibold hover:text-teal-600 transition-colors">立即登录</router-link>
          </p>
        </div>
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
import { useCountdown } from '@/composables/useCountdown'
import { authApi } from '@/api/auth'

const router = useRouter()
const authStore = useAuthStore()

const error = ref('')
const success = ref('')
const loading = ref(false)
const codeLoading = ref(false)
const { countdown: codeCountdown, start: startCodeCountdown } = useCountdown(60)

const form = reactive({
  username: '',
  email: '',
  code: '',
  password: '',
  confirmPassword: '',
})

function validate() {
  if (!form.username.trim()) return '请输入用户名'
  if (form.username.trim().length > 10) return '用户名不能超过10个字符'
  if (/^\d+$/.test(form.username.trim())) return '用户名不能为纯数字'
  if (!form.email.trim()) return '请输入邮箱'
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) return '请输入正确的邮箱格式'
  if (!form.code.trim()) return '请输入邮箱验证码'
  if (!/^\d{6}$/.test(form.code.trim())) return '验证码为6位数字'
  if (!form.password || form.password.length < 6) return '密码不能少于6位'
  if (form.password !== form.confirmPassword) return '两次输入的密码不一致'
  return null
}

async function handleSendCode() {
  if (!form.email.trim()) {
    error.value = '请先输入邮箱'
    return
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) {
    error.value = '请输入正确的邮箱格式'
    return
  }
  error.value = ''
  codeLoading.value = true
  try {
    await authApi.sendCode(form.email.trim())
    success.value = '验证码已发送，请查看终端控制台'
    error.value = ''
    startCodeCountdown()
  } catch (e) {
    error.value = e.message || '验证码发送失败'
  } finally {
    codeLoading.value = false
  }
}

async function handleRegister() {
  error.value = ''
  success.value = ''
  const msg = validate()
  if (msg) {
    error.value = msg
    return
  }

  loading.value = true
  try {
    const payload = {
      username: form.username.trim(),
      email: form.email.trim(),
      code: form.code.trim(),
      password: form.password,
    }

    const res = await authApi.register(payload)
    authStore.setAuth({ access_token: res.data.access_token, user: res.data.user })
    router.push('/')
  } catch (e) {
    error.value = e.message || '注册失败，请重试'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
/* 浮动动画 */
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

/* 输入框 */
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
  border-color: #14b8a6;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(20, 184, 166, 0.08), 0 1px 2px rgba(0,0,0,0.04);
}
.input-field-page.input-error-page {
  border-color: #ef4444;
  background: #fefafa;
}
.input-field-page.input-error-page:focus {
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
}

/* 验证码按钮 */
.code-btn-page {
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
.code-btn-page:hover:not(:disabled) {
  background: #14b8a6;
  color: #fff;
  box-shadow: 0 4px 15px rgba(20, 184, 166, 0.3);
  transform: translateY(-1px);
}
.code-btn-page:disabled {
  opacity: 0.45;
  cursor: not-allowed;
  border-color: #cdd5df;
  color: #a1a1aa;
}

/* 提交按钮 */
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

/* 注册按钮使用 teal 色系 */
.submit-btn-page--teal {
  background: linear-gradient(135deg, #14b8a6 0%, #0d9488 50%, #0891b2 100%);
  box-shadow: 0 4px 20px rgba(20, 184, 166, 0.3), 0 1px 3px rgba(0,0,0,0.08);
}
.submit-btn-page--teal:hover:not(:disabled) {
  background: linear-gradient(135deg, #0d9488 0%, #0f766e 50%, #0e7490 100%);
  box-shadow: 0 8px 30px rgba(20, 184, 166, 0.4), 0 2px 6px rgba(0,0,0,0.1);
}
.submit-btn-page--teal:active:not(:disabled) {
  box-shadow: 0 2px 10px rgba(20, 184, 166, 0.25);
}
</style>
