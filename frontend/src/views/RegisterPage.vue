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
      <div class="input-group">
        <input
          v-model="form.phone"
          type="text"
          placeholder="手机号（选填）"
          autocomplete="tel"
        />
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
const loading = ref(false)

const form = reactive({
  username: '',
  email: '',
  phone: '',
  password: '',
  confirmPassword: '',
})

function validate() {
  if (!form.username.trim()) return '请输入用户名'
  if (form.username.trim().length < 2) return '用户名至少2个字符'
  if (!form.email.trim()) return '请输入邮箱'
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email.trim())) return '请输入正确的邮箱格式'
  if (form.phone.trim() && !/^1\d{10}$/.test(form.phone.trim())) return '请输入正确的手机号'
  if (!form.password || form.password.length < 6) return '密码不能少于6位'
  if (form.password !== form.confirmPassword) return '两次输入的密码不一致'
  return null
}

async function handleRegister() {
  error.value = ''
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
      password: form.password,
    }
    if (form.phone.trim()) {
      payload.phone = form.phone.trim()
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
.form-error {
  color: #e74c3c;
  font-size: 13px;
  margin-bottom: 10px;
  text-align: center;
}
</style>