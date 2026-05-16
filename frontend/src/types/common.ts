/** 通用 API 响应包装 */
export interface ApiResponse<T> {
  code: number
  message: string
  data: T
}

/** 分页数据 */
export interface PaginatedData<T> {
  list: T[]
  total: number
  page: number
  pageSize: number
}

/** 统计数据项 */
export interface StatItem {
  num: string
  label: string
}

/** 星级评价 */
export interface StarReview {
  id: number
  name: string
  color: string
  stars: number
  date: string
  text: string
  tags: string[]
}