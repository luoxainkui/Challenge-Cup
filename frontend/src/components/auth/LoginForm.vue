<template>
  <div>
    <!-- ====== 品牌头部 ====== -->
    <div class="text-center mb-7">
      <!-- 装饰 Logo -->
      <div class="relative inline-flex items-center justify-center">
        <div class="absolute inset-0 w-16 h-16 rounded-2xl bg-gradient-to-br from-blue-400/20 via-indigo-400/15 to-purple-400/20 blur-md animate-pulse"></div>
        <div class="relative w-14 h-14 rounded-xl bg-gradient-to-br from-blue-500 via-indigo-500 to-purple-600 flex items-center justify-center shadow-[0_8px_25px_rgba(79,70,229,0.3)]">
          <span class="text-white text-2xl font-bold tracking-wider">桂</span>
        </div>
      </div>
      <h2 class="text-[22px] font-bold text-slate-800 mt-5 mb-1.5 tracking-tight">登录桂升通</h2>
      <p class="text-sm text-slate-400">登录后即可访问完整功能</p>
    </div>

    <!-- ====== 表单 ====== -->
    <div class="mb-4">
      <div class="relative">
        <!-- 邮箱图标 -->
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
          class="input-field pl-11"
          :class="{ 'input-error': errors.email }"
          @input="clearFieldError('email')"
        />
      </div>
      <p v-if="errors.email" class="field-error">{{ errors.email }}</p>
    </div>

    <div class="mb-3">
      <div class="relative">
        <!-- 锁图标 -->
        <div class="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-300 pointer-events-none">
          <svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
          </svg>
        </div>
        <input
          v-model="form.password"
          :type="showPassword ? 'text' : 'password'"
          placeholder="请输入密码"
          autocomplete="current-password"
          class="input-field pl-11 pr-11"
          :class="{ 'input-error': errors.password }"
          @input="clearFieldError('password')"
          @keyup.enter="handleLogin"
        />
        <button
          type="button"
          class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-300 hover:text-slate-500 transition-colors p-1.5 rounded-lg hover:bg-slate-100"
          @click="showPassword = !showPassword"
          :title="showPassword ? '隐藏密码' : '显示密码'"
        >
          <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
        </button>
      </div>
      <p v-if="errors.password" class="field-error">{{ errors.password }}</p>
    </div>

    <!-- 忘记密码 -->
    <div class="text-right mb-3">
      <a
        href="#"
        class="text-xs text-indigo-500 no-underline hover:text-indigo-600 font-medium transition-colors"
        @click.prevent="$emit('forgot')"
      >忘记密码？</a>
    </div>

    <!-- 通用错误提示 -->
    <p v-if="loginError" class="text-[#ef4444] text-[13px] text-center mb-3 bg-red-50 rounded-lg py-2 px-3">{{ loginError }}</p>

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

    <!-- ====== 第三方快捷登录 ====== -->
    <div class="flex items-center gap-4 my-6">
      <div class="flex-1 h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent"></div>
      <span class="text-xs text-slate-350 whitespace-nowrap tracking-wide">快捷登录</span>
      <div class="flex-1 h-px bg-gradient-to-r from-transparent via-slate-200 to-transparent"></div>
    </div>

    <div class="flex justify-center gap-6">
      <!-- 微信登录 -->
      <button
        class="social-btn social-btn--wechat group"
        title="微信登录"
        @click="handleSocialLogin('wechat')"
      >
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 01.213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 00.167-.054l1.903-1.114a.864.864 0 01.717-.098 10.16 10.16 0 002.837.403c.276 0 .543-.027.811-.05-.857-2.578.157-4.972 1.932-6.446 1.703-1.415 3.882-1.98 5.853-1.838-.576-3.583-4.196-6.348-8.596-6.348zM5.992 5.193c.455-.47 1.131-.47 1.586 0 .455.47.455 1.215 0 1.685-.455.47-1.131.47-1.586 0-.455-.47-.455-1.215 0-1.685zm4.1 0c.455-.47 1.131-.47 1.586 0 .455.47.455 1.215 0 1.685-.455.47-1.131.47-1.586 0-.455-.47-.455-1.215 0-1.685z"/>
          <path d="M19.381 13.561c-3.184 0-5.774 2.588-5.774 5.774 0 3.186 2.59 5.774 5.774 5.774.645 0 1.272-.106 1.86-.303a.566.566 0 01.471.064l1.248.73a.214.214 0 00.11.035.193.193 0 00.19-.193c0-.042-.018-.098-.032-.145l-.256-.97a.386.386 0 01.14-.436c1.202-.883 1.982-2.279 1.982-3.854 0-3.186-2.59-5.774-5.774-5.774h.051zm-2.5 2.621c.36-.372.832-.372 1.192 0 .36.372.36.957 0 1.329-.36.372-.832.372-1.192 0-.36-.372-.36-.957 0-1.329zm3.964 0c.36-.372.832-.372 1.192 0 .36.372.36.957 0 1.329-.36.372-.832.372-1.192 0-.36-.372-.36-.957 0-1.329z"/>
        </svg>
      </button>
      <!-- QQ登录 -->
      <button
        class="social-btn social-btn--qq group"
        title="QQ登录"
        @click="handleSocialLogin('qq')"
      >
        <svg class="w-5 h-5" viewBox="0 0 24 24" fill="currentColor">
          <path d="M21.395 13.581c-1.047-.632-2.442-1.416-2.442-3.352 0-1.582.76-2.417 1.213-3.064.26-.372.36-.687.413-.913.065-.285.087-.57.087-.856C20.666 2.08 18.818 0 12.2 0 5.58 0 3.333 2.08 3.333 5.396c0 .286.022.571.087.856.053.226.153.541.413.913.453.647 1.213 1.482 1.213 3.064 0 1.936-1.395 2.72-2.442 3.352C1.558 14.21 0 15.4 0 17.009v3.993c0 .547.453.998 1 .998h21c.547 0 1-.451 1-.998v-3.993c0-1.609-1.558-2.799-2.605-3.428z"/>
        </svg>
      </button>
    </div>

    <!-- ====== 底部链接：去注册 + 手机号登录 ====== -->
    <div class="flex flex-col items-center gap-2 mt-5">
      <p class="text-sm text-slate-500 m-0">
        没有账号？
        <router-link to="/register" class="text-indigo-500 no-underline font-semibold hover:text-indigo-600 transition-colors" @click="handleRegisterClick">去注册</router-link>
      </p>
      <a
        href="#"
        class="text-sm text-indigo-500 no-underline hover:text-indigo-600 font-medium transition-colors"
        @click.prevent="$emit('switch-tab', 'phone')"
      >手机号快捷登录 →</a>
    </div>
  </div>
</template>

<script setup>
/**
 * LoginForm — 邮箱密码登录表单
 * 功能：邮箱+密码登录、密码显隐切换、实时校验、加载状态、第三方登录入口
 */
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'

const emit = defineEmits(['switch-tab', 'forgot', 'success'])
const router = useRouter()
const authStore = useAuthStore()

const form = reactive({ email: '', password: '' })
const errors = reactive({ email: '', password: '' })
const showPassword = ref(false)
const loginError = ref('')
const loginLoading = ref(false)

function clearFieldError(field) {
  errors[field] = ''
  loginError.value = ''
}

function validate() {
  let valid = true
  // 邮箱校验
  if (!form.email.trim()) {
    errors.email = '请输入邮箱'
    valid = false
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) {
    errors.email = '请输入正确的邮箱格式'
    valid = false
  } else {
    errors.email = ''
  }
  // 密码校验
  if (!form.password.trim()) {
    errors.password = '请输入密码'
    valid = false
  } else if (form.password.trim().length < 6) {
    errors.password = '密码长度不能少于6位'
    valid = false
  } else {
    errors.password = ''
  }
  return valid
}

async function handleLogin() {
  loginError.value = ''
  if (!validate()) return

  loginLoading.value = true
  try {
    const res = await authApi.login({
      email: form.email.trim(),
      password: form.password,
    })
    authStore.setAuth({ access_token: res.data.access_token, user: res.data.user })
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
  // 关闭弹窗后跳转注册页
  authStore.clearLoginRequired()
}

function handleSocialLogin(platform) {
  // TODO: 对接后端 OAuth 回调 — 微信/QQ 第三方登录
  loginError.value = `${platform === 'wechat' ? '微信' : 'QQ'}登录功能即将上线，敬请期待`
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
  border-color: #6366f1;
  background: #fff;
  box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.08), 0 1px 2px rgba(0,0,0,0.04);
}
.input-field.input-error {
  border-color: #ef4444;
  background: #fefafa;
}
.input-field.input-error:focus {
  box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.08);
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
  background: linear-gradient(135deg, #4f46e5 0%, #4338ca 50%, #6d28d9 100%);
  box-shadow: 0 8px 30px rgba(99, 102, 241, 0.4), 0 2px 6px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}
.form-btn:active:not(:disabled) {
  transform: translateY(0);
  box-shadow: 0 2px 10px rgba(99, 102, 241, 0.25);
}
.form-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
}

/* ====== 社交登录按钮 ====== */
.social-btn {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  border: 1.5px solid #e8ecf1;
  background: #fafbfc;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  color: #94a3b8;
}
.social-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
}
.social-btn--wechat:hover {
  color: #07c160;
  border-color: #07c160;
  background: #f0fdf4;
  box-shadow: 0 8px 24px rgba(7, 193, 96, 0.15);
}
.social-btn--qq:hover {
  color: #0ea5e9;
  border-color: #0ea5e9;
  background: #f0f9ff;
  box-shadow: 0 8px 24px rgba(14, 165, 233, 0.15);
}
</style>