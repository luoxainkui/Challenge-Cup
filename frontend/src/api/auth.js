import { http } from './base'

/**
 * 认证相关 API — 对应后端 /api/auth/*
 */
export const authApi = {
  /** 登录 → POST /api/auth/login { email, password } */
  login: (data) => http.post('/auth/login', data),

  /** 注册 → POST /api/auth/register { username, email, password } */
  register: (data) => http.post('/auth/register', data),

  /** 发送验证码 → POST /api/auth/send-code { email } */
  sendCode: (email) => http.post('/auth/send-code', { email }),

  /** 重置密码 → POST /api/auth/reset-password { email, code, password } */
  resetPassword: (email, code, password) => http.post('/auth/reset-password', { email, code, password }),

  /**
   * 手机验证码登录 → POST /api/auth/phone-login { phone, code }
   * TODO: 后端需实现该接口，当前前端 PhoneLoginForm 有演示模式兜底
   */
  phoneLogin: (data) => http.post('/auth/phone-login', data),

  /**
   * 发送短信验证码 → POST /api/auth/send-sms { phone }
   * TODO: 后端需实现该接口，当前前端复用 sendCode 作为演示
   */
  sendSms: (phone) => http.post('/auth/send-sms', { phone }),
}
