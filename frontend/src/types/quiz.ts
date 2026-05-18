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

// ========== 答题引擎 ==========

/** 答题即时统计（useQuiz stats） */
export interface QuizStats {
  correct: number
  wrong: number
  unanswered: number
  total: number
  score: number
}

/** 答题卡题目项 */
export interface QuestionCardItem {
  index: number
  type: QuestionType
  typeLabel: string
  submitted: boolean
  correct: boolean | null
}

/** 用户作答记录 */
export interface AnswerRecord {
  [questionIndex: number]: number[]
}

// ========== 错题本 ==========

/** 错题详情（含题目与考点） */
export interface MistakeDetail {
  questionId: number
  wrongCount: number
  correctCount: number
  lastWrongAt: string
  question: Question
  point: ExamPoint
}

/** 错题本设置 */
export interface MistakeSettings {
  autoRemove: boolean
  autoRemoveThreshold: number
}

/** 考点分布项 */
export interface PointDistributionItem {
  point: ExamPoint
  count: number
}

/** 科目分布项（错题本柱状图） */
export interface SubjectDistributionItem {
  subject: string
  count: number
  color: string
}

/** 题型分布项（错题本柱状图） */
export interface TypeDistributionItem {
  type: QuestionType
  label: string
  count: number
}

// ========== AI 智能组卷 ==========

/** AI 组卷配置 */
export interface AIGenConfig {
  /** 已选科目 */
  selectedSubjects: string[]
  /** 题目总数 */
  count: number
  /** 简单题占比（0-100） */
  easy: number
  /** 中等题占比（0-100） */
  medium: number
  /** 困难题占比（0-100） */
  hard: number
}

/** AI 分析维度 */
export type AIAnalysisType = 'weak' | 'focus' | 'normal'

/** AI 分析项 */
export interface AIAnalysisItem {
  type: AIAnalysisType
  label: string
  detail: string
}

/** AI 解题步骤 */
export type AISolutionStep = '审题分析' | '解题步骤' | '易错提醒' | '知识点拓展'

/** AI 解题解析 */
export interface AISolution {
  /** 审题分析 */
  analysis: string
  /** 解题步骤 */
  steps: string[]
  /** 易错提醒 */
  warnings: string[]
  /** 知识点标签 */
  tags: string[]
}