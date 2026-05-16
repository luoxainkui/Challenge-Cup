import type { StarReview } from './common'

/** 伴学服务特性 */
export interface MentorFeature {
  icon: string
  title: string
  desc: string
}

/** 伴学流程步骤 */
export interface MentorFlowStep {
  num: string
  title: string
  desc: string
}

/** 导师信息 */
export interface Mentor {
  id: number
  name: string
  title: string
  color: string
  tags: string[]
  desc: string
  students: number
  rate: number
}

/** 伴学服务聚合 */
export interface MentorData {
  features: MentorFeature[]
  flowSteps: MentorFlowStep[]
  mentors: Mentor[]
  reviews: StarReview[]
}