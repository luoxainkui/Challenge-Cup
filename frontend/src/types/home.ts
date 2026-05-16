import type { StatItem } from './common'

/** 首页服务卡 */
export interface HomeService {
  icon: string
  title: string
  desc: string
  link: string
}

/** 优势卡 */
export interface Advantage {
  icon: string
  title: string
  desc: string
  color: string
}

/** 首页聚合 */
export interface HomeData {
  stats: StatItem[]
  services: HomeService[]
  advantages: Advantage[]
}