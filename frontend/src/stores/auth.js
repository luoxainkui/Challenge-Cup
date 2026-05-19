import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || '')
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))
  const loginRequired = ref(false)
  const redirectPath = ref('')

  const isLoggedIn = computed(() => !!token.value)
  const userName = computed(() => user.value?.username || user.value?.name || '')

  function setAuth(data) {
    // 后端返回 access_token，统一存为 token
    const accessToken = data.access_token || data.token
    token.value = accessToken
    user.value = data.user
    localStorage.setItem('token', accessToken)
    localStorage.setItem('user', JSON.stringify(data.user))
  }

  function logout() {
    token.value = ''
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  function setLoginRequired(path = '') {
    loginRequired.value = true
    redirectPath.value = path || redirectPath.value
  }

  function clearLoginRequired() {
    loginRequired.value = false
    redirectPath.value = ''
  }

  function popRedirectPath() {
    const p = redirectPath.value
    redirectPath.value = ''
    clearLoginRequired()
    return p
  }

  return { token, user, isLoggedIn, userName, loginRequired, redirectPath, setAuth, logout, setLoginRequired, clearLoginRequired, popRedirectPath }
})
