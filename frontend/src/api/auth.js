import { http } from './base'

/**
 * 认证相关 API
 */
export const authApi = {
  /** 登录 */
  login: (data) => http.post('/auth/login', data),

  /** 注册 */
  register: (data) => http.post('/auth/register', data),

  /** 发送验证码 */
  sendCode: (phone) => http.post('/auth/send-code', { phone }),

  /** 验证验证码 */
  verifyCode: (phone, code) => http.post('/auth/verify-code', { phone, code }),

  /** 重置密码 */
  resetPassword: (phone, code, password) => http.post('/auth/reset-password', { phone, code, password }),
}
