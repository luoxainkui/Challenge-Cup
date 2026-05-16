<template>
  <div class="page-container">
    <div class="form-box">
      <template v-if="mode === 'login'">
        <div class="form-header">
          <div class="form-logo">桂</div>
          <h2 class="form-title">登录桂升通</h2>
        </div>
        <div class="input-group">
          <input v-model="loginForm.phone" type="text" placeholder="手机号" />
        </div>
        <div class="input-group">
          <input v-model="loginForm.password" type="password" placeholder="密码" />
        </div>
        <p class="form-error" v-if="loginError">{{ loginError }}</p>
        <button class="form-btn" @click="handleLogin" :disabled="loginLoading">
          {{ loginLoading ? '登录中...' : '登 录' }}
        </button>
        <div class="form-links">
          <router-link to="/register">立即注册</router-link>
          <span>|</span>
          <a href="#" @click.prevent="mode = 'forgot'">忘记密码</a>
        </div>
      </template>

      <ForgotPassword
        v-else
        @back="mode = 'login'"
        @done="mode = 'login'"
      />
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'
import ForgotPassword from '@/components/auth/ForgotPassword.vue'

const router = useRouter()
const authStore = useAuthStore()

const mode = ref('login')
const loginError = ref('')
const loginLoading = ref(false)

const loginForm = reactive({
  phone: '',
  password: '',
})

async function handleLogin() {
  loginError.value = ''
  if (!loginForm.phone.trim()) {
    loginError.value = '请输入手机号'
    return
  }
  if (!loginForm.password.trim()) {
    loginError.value = '请输入密码'
    return
  }
  loginLoading.value = true
  try {
    const res = await authApi.login({ phone: loginForm.phone, password: loginForm.password })
    authStore.setAuth({ token: res.token, user: res.user })
    router.push('/')
  } catch (e) {
    loginError.value = e.message || '登录失败，请重试'
  } finally {
    loginLoading.value = false
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