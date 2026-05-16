/** 课程分类 */
export interface CourseCategory {
  label: string
  value: string
}

/** 课程卡片数据 */
export interface Course {
  id: number
  subject: string
  category: string
  name: string
  desc: string
  teacher: string
  students: number
  rating: number
  price: number
  hot: boolean
  color: string
  duration: string
  lessons: number
}

/** 课程详情（含章节） */
export interface CourseDetail extends Course {
  chapters?: CourseChapter[]
  syllabus?: string[]
}

/** 课程章节 */
export interface CourseChapter {
  id: number | string
  title: string
  duration?: string
  videoUrl?: string
  free?: boolean
}

/** 课程筛选条件 */
export interface CourseFilter {
  category: string
  keyword: string
  page: number
  pageSize: number
}

/** 章节目录 */
export interface TopicMap {
  [subject: string]: string[]
}