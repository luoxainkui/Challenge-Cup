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
}
