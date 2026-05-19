<template>
  <div>
    <div class="form-header">
      <div class="form-logo">桂</div>
      <h2 class="form-title">重置密码</h2>
      <p class="form-subtitle">通过邮箱验证重置您的密码</p>
    </div>

    <!-- 步骤 1：输入邮箱 -->
    <div v-if="step === 1">
      <div class="input-group">
        <input v-model="form.email" type="email" placeholder="请输入注册邮箱" />
      </div>
      <p class="form-error" v-if="error">{{ error }}</p>
      <p class="form-hint">💡 验证码将发送到您的注册邮箱，请注意查收（如未收到请检查垃圾箱）</p>
      <button class="form-btn" @click="handleSendCode" :disabled="sending">
        {{ sending ? '发送中...' : '获取验证码' }}
      </button>
      <div class="form-links">
        <a href="#" @click.prevent="emit('back')">← 返回登录</a>
      </div>
    </div>

    <!-- 步骤 2：验证码 + 新密码 -->
    <div v-else>
      <div class="input-group">
        <input v-model="form.email" type="email" disabled class="input-disabled" />
      </div>
      <div class="code-input">
        <input v-model="form.code" type="text" placeholder="输入验证码" />
        <button class="code-btn" @click="handleSendCode" :disabled="sending || countdown > 0">
          {{ countdown > 0 ? `${countdown}s 后重发` : '重新发送' }}
        </button>
      </div>
      <div class="input-group">
        <input v-model="form.password" type="password" placeholder="设置新密码（不少于6位）" />
      </div>
      <div class="input-group">
        <input v-model="form.confirmPassword" type="password" placeholder="确认新密码" />
      </div>
      <p class="form-error" v-if="error">{{ error }}</p>
      <p class="form-success" v-if="success">{{ success }}</p>
      <button class="form-btn" @click="handleReset" :disabled="resetting">
        {{ resetting ? '重置中...' : '重置密码' }}
      </button>
      <div class="form-links">
        <a href="#" @click.prevent="emit('back')">← 返回登录</a>
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
.form-subtitle {
  font-size: 14px;
  color: #888;
  margin-top: 6px;
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

.input-disabled {
  background-color: #f5f5f5;
  color: #999;
}
</style>