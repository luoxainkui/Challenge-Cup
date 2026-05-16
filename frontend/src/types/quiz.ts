/** 题目类型枚举 */
export type QuestionType = 'single' | 'multi' | 'truefalse' | 'fill'

/** 题目类型配置 */
export interface QuestionTypeConfig {
  label: string
  icon: string
}

/** 考点定义 */
export interface ExamPoint {
  id: string
  name: string
  subject: string
}

/** 题目定义 */
export interface Question {
  id: number
  pointId: string
  type: QuestionType
  difficulty: number
  stem: string
  options: string[]
  answer: number[]
  analysis: string
}

/** 错题记录 */
export interface MistakeRecord {
  questionId: number
  wrongCount: number
  correctCount: number
  lastWrongAt: string
}

/** 练习题模式 */
export interface QuizMode {
  id: string
  icon: string
  name: string
  desc: string
  count: string
}

/** 科目统计 */
export interface QuizSubject {
  name: string
  icon: string
  color: string
  count: number
  progress: number
}

/** 试卷 */
export interface QuizPaper {
  id: string
  name: string
  subject: string
  duration: number
  total: number
}

/** 章节 */
export interface Chapter {
  name: string
  color: string
  icon: string
  topics: ChapterTopic[]
}

/** 章节主题 */
export interface ChapterTopic {
  id: string
  name: string
  count: number
}

/** 答题结果 */
export interface QuizResult {
  total: number
  correct: number
  wrong: number
  score: number
  timeUsed: number
  answers: Record<number, number[]>
}

/** 错题分布 */
export interface MistakeDistribution {
  subject: string
  count: number
  percentage: number
}