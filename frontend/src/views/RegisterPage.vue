<template>
  <div class="page-container">
    <div class="form-box">
      <div class="form-header">
        <div class="form-logo">桂</div>
        <h2 class="form-title">注册桂升通</h2>
      </div>

      <div class="input-group">
        <input
          v-model="form.username"
          type="text"
          placeholder="用户名"
          autocomplete="username"
        />
      </div>
      <div class="input-group">
        <input
          v-model="form.email"
          type="email"
          placeholder="邮箱"
          autocomplete="email"
        />
      </div>
      <div class="input-group input-group-code">
        <input
          v-model="form.code"
          type="text"
          placeholder="邮箱验证码"
          maxlength="6"
          autocomplete="off"
        />
        <button
          type="button"
          class="code-btn"
          :disabled="codeLoading || codeCountdown > 0"
          @click="handleSendCode"
        >
          {{ codeCountdown > 0 ? `${codeCountdown}秒` : codeLoading ? '发送中...' : '获取验证码' }}
        </button>
      </div>
      <div class="input-group">
        <input
          v-model="form.password"
          type="password"
          placeholder="设置密码（不少于6位）"
          autocomplete="new-password"
        />
      </div>
      <div class="input-group">
        <input
          v-model="form.confirmPassword"
          type="password"
          placeholder="确认密码"
          autocomplete="new-password"
        />
      </div>

      <p class="form-error" v-if="error">{{ error }}</p>
      <p class="form-success" v-if="success">{{ success }}</p>
      <p class="form-hint">💡 验证码将发送到您的注册邮箱，请注意查收。如未收到请查看终端控制台输出。</p>

      <button class="form-btn" @click="handleRegister" :disabled="loading">
        {{ loading ? '注册中...' : '注 册' }}
      </button>
      <div class="form-links">
        <span>已有账号？</span>
        <router-link to="/login">立即登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'

const router = useRouter()
const authStore = useAuthStore()

const error = ref('')
const success = ref('')
const loading = ref(false)
const codeLoading = ref(false)
const codeCountdown = ref(0)

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
    codeCountdown.value = 60
    const timer = setInterval(() => {
      codeCountdown.value--
      if (codeCountdown.value <= 0) clearInterval(timer)
    }, 1000)
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
.input-group-code {
  display: flex;
  gap: 10px;
}
.input-group-code input {
  flex: 1;
}
.code-btn {
  flex-shrink: 0;
  padding: 0 14px;
  border: 1px solid #8b5e3c;
  border-radius: 8px;
  background: #fff;
  color: #8b5e3c;
  font-size: 13px;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s;
}
.code-btn:hover:not(:disabled) {
  background: #8b5e3c;
  color: #fff;
}
.code-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
.form-error {
  color: #e74c3c;
  font-size: 13px;
  margin-bottom: 10px;
  text-align: center;
}
.form-success {
  color: #27ae60;
  font-size: 13px;
  margin-bottom: 10px;
  text-align: center;
}
.form-hint {
  font-size: 12px;
  color: #888;
  margin-bottom: 14px;
  text-align: center;
  line-height: 1.6;
}
</style>
