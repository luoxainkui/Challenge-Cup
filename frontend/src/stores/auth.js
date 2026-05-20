import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || '')
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'))
  const loginRequired = ref(false)       // 路由守卫触发的登录要求
  const showLoginModal = ref(false)      // 用户手动点击登录按钮
  const redirectPath = ref('')

  const isLoggedIn = computed(() => !!token.value)
  const userName = computed(() => user.value?.username || user.value?.name || '')

  /** 弹窗是否应该显示 = 路由守卫触发 OR 用户手动点击 */
  const isModalVisible = computed(() => loginRequired.value || showLoginModal.value)

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

  /** 手动打开登录弹窗 */
  function openLoginModal() {
    showLoginModal.value = true
  }

  /** 关闭登录弹窗（同时清理两种触发状态） */
  function closeLoginModal() {
    showLoginModal.value = false
    loginRequired.value = false
    redirectPath.value = ''
  }

  return {
    token, user, isLoggedIn, userName,
    loginRequired, showLoginModal, isModalVisible, redirectPath,
    setAuth, logout,
    setLoginRequired, clearLoginRequired, popRedirectPath,
    openLoginModal, closeLoginModal,
  }
})
