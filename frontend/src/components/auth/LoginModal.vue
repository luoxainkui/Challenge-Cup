<template>
  <Transition name="modal-fade">
    <div v-if="visible" class="login-modal-overlay" @click.self="() => {}">
      <div class="login-modal-card">
        <button class="login-modal-close" @click="handleClose">&times;</button>

        <template v-if="mode === 'login'">
          <div class="form-header">
            <div class="form-logo">桂</div>
            <h2 class="form-title">登录桂升通</h2>
            <p class="form-sub">登录后即可访问完整功能</p>
          </div>
          <div class="input-group">
            <input v-model="loginForm.email" type="email" placeholder="邮箱" />
          </div>
          <div class="input-group">
            <input v-model="loginForm.password" type="password" placeholder="密码" @keyup.enter="handleLogin" />
          </div>
          <p class="form-error" v-if="loginError">{{ loginError }}</p>
          <button class="form-btn" @click="handleLogin" :disabled="loginLoading">
            {{ loginLoading ? '登录中...' : '登 录' }}
          </button>
          <div class="form-links">
            <router-link to="/register" @click="handleClose">立即注册</router-link>
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
  </Transition>
</template>

<script setup>
import { reactive, ref, watch } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { authApi } from '@/api/auth'
import ForgotPassword from '@/components/auth/ForgotPassword.vue'

const props = defineProps({
  visible: { type: Boolean, default: false },
})
const emit = defineEmits(['close', 'logged-in'])

const router = useRouter()
const authStore = useAuthStore()

const mode = ref('login')
const loginError = ref('')
const loginLoading = ref(false)

const loginForm = reactive({
  email: '',
  password: '',
})

// 每次弹窗打开时重置表单
watch(() => props.visible, (v) => {
  if (v) {
    mode.value = 'login'
    loginError.value = ''
    loginLoading.value = false
    loginForm.email = ''
    loginForm.password = ''
  }
})

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

    const redirect = authStore.popRedirectPath()
    emit('logged-in')
    if (redirect) {
      router.push(redirect)
    }
  } catch (e) {
    loginError.value = e.message || '登录失败，请重试'
  } finally {
    loginLoading.value = false
  }
}

function handleClose() {
  authStore.clearLoginRequired()
  emit('close')
}
</script>

<style scoped>
.login-modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
}

.login-modal-card {
  position: relative;
  width: 100%;
  max-width: 440px;
  margin: 0 20px;
  padding: 40px 32px;
  background: #fff;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.login-modal-close {
  position: absolute;
  top: 12px;
  right: 16px;
  background: none;
  border: none;
  font-size: 28px;
  line-height: 1;
  color: #999;
  cursor: pointer;
  padding: 4px 8px;
}

.login-modal-close:hover {
  color: #333;
}

.form-sub {
  font-size: 14px;
  color: #888;
  margin-top: 6px;
}

/* ---------- 渐变过渡（沿用 App.vue 的 fade 风格） ---------- */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}

.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-fade-enter-from .login-modal-card {
  transform: translateY(32px) scale(0.96);
  opacity: 0;
}

.modal-fade-leave-to .login-modal-card {
  transform: translateY(-20px) scale(0.96);
  opacity: 0;
}

.login-modal-card {
  transition: all 0.4s cubic-bezier(0.22, 1, 0.36, 1);
}
</style>