/** AI 知识库条目 */
export interface KnowledgeBase {
  [keyword: string]: string
}

/** 快捷问题 */
export interface QuickQuestion {
  id: number
  icon: string
  text: string
  keyword: string
}

/** 聊天消息 */
export interface ChatMessage {
  role: 'user' | 'ai'
  text: string
  showContact?: boolean
}

/** 消息角色类型 */
export type MessageRole = 'user' | 'ai'

/** 欢迎消息 */
export type WelcomeMessage = ChatMessage

/** 试听课选项 */
export interface TrialCourse {
  value: string
  label: string
}

/** 咨询预约表单 */
export interface ConsultationForm {
  name: string
  phone: string
  course: string
}