import { http } from './base'

/**
 * 认证相关 API — 对应后端 /api/auth/*
 */
export const authApi = {
  /** 登录 → POST /api/auth/login { username, password } */
  login: (data) => http.post('/auth/login', data),

  /** 注册 → POST /api/auth/register { username, email, password, phone? } */
  register: (data) => http.post('/auth/register', data),
}