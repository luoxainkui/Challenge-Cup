import { http } from './base'

/**
 * 课程相关 API
 */
export const courseApi = {
  /** 获取课程列表 */
  getList: (params) => http.get('/courses', params),

  /** 获取课程详情 */
  getDetail: (id) => http.get(`/courses/${id}`),

  /** 报名课程 */
  enroll: (courseId) => http.post(`/courses/${courseId}/enroll`),
}