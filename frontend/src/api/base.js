const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

/**
 * 基础请求封装
 */
async function request(url, options = {}) {
  const config = {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  }

  try {
    const response = await fetch(`${API_BASE_URL}${url}`, config)
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`)
    }
    return await response.json()
  } catch (error) {
    console.error(`[API Error] ${url}:`, error)
    throw error
  }
}

export const http = {
  get: (url, params) => {
    const query = params ? '?' + new URLSearchParams(params).toString() : ''
    return request(`${url}${query}`)
  },
  post: (url, data) => request(url, { method: 'POST', body: JSON.stringify(data) }),
  put: (url, data) => request(url, { method: 'PUT', body: JSON.stringify(data) }),
  delete: (url) => request(url, { method: 'DELETE' }),
}