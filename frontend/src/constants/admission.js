// ========== 志愿智能填报落地页 ==========

/** 页面统计数据 */
export const ADMISSION_STATS = [
  { num: '38', label: '广西专升本院校' },
  { num: '120+', label: '招生专业方向' },
  { num: '3年', label: '历年分数线数据' },
  { num: '92%', label: '适配预测准确率' },
]

/** 报考流程步骤 */
export const ADMISSION_STEPS = [
  { step: 1, icon: '📋', title: '了解院校', desc: '浏览38所广西专升本招生院校信息，对比办学特色' },
  { step: 2, icon: '📊', title: '参考分数', desc: '查询近3年各院校各专业最低录取分数线与位次' },
  { step: 3, icon: '🎯', title: '智能适配', desc: '输入你的预估分数与意向专业，获取适配院校推荐' },
  { step: 4, icon: '✅', title: '填报志愿', desc: '参考推荐结果，在规定时间内完成网上志愿填报' },
]

/** 院校报考指南 */
export const SCHOOL_GUIDE = [
  {
    id: 1,
    name: '广西师范大学',
    icon: '师',
    color: '#2a6eff',
    category: '师范类',
    location: '桂林市',
    features: ['教育学', '汉语言文学', '英语', '数学与应用数学'],
    isTop: true,
    admissionScore: 385,
    planCount: 320,
    desc: '广西重点师范院校，师范类专业实力突出，教育学、汉语言文学为国家级特色专业',
  },
  {
    id: 2,
    name: '广西医科大学',
    icon: '医',
    color: '#e74c3c',
    category: '医药类',
    location: '南宁市',
    features: ['临床医学', '护理学', '药学', '预防医学'],
    isTop: true,
    admissionScore: 410,
    planCount: 260,
    desc: '广西医学教育最高学府，临床医学和护理学专业优势显著',
  },
  {
    id: 3,
    name: '桂林电子科技大学',
    icon: '电',
    color: '#ff6b35',
    category: '理工类',
    location: '桂林市',
    features: ['计算机科学与技术', '电子信息工程', '通信工程', '软件工程'],
    isTop: true,
    admissionScore: 375,
    planCount: 420,
    desc: '以电子信息为特色的工科强校，计算机相关专业就业率高',
  },
  {
    id: 4,
    name: '广西财经学院',
    icon: '财',
    color: '#4caf50',
    category: '财经类',
    location: '南宁市',
    features: ['会计学', '财务管理', '金融学', '国际经济与贸易'],
    isTop: true,
    admissionScore: 360,
    planCount: 350,
    desc: '广西唯一财经类本科院校，会计学和金融学为优势专业',
  },
  {
    id: 5,
    name: '南宁师范大学',
    icon: '南',
    color: '#9c27b0',
    category: '师范类',
    location: '南宁市',
    features: ['小学教育', '学前教育', '体育教育', '音乐学'],
    isTop: false,
    admissionScore: 345,
    planCount: 280,
    desc: '自治区直属师范院校，教育学学科体系完善',
  },
  {
    id: 6,
    name: '广西科技大学',
    icon: '科',
    color: '#008888',
    category: '理工类',
    location: '柳州市',
    features: ['机械工程', '土木工程', '车辆工程', '自动化'],
    isTop: false,
    admissionScore: 335,
    planCount: 310,
    desc: '以工科为主的综合性大学，机械工程为自治区优势特色专业',
  },
  {
    id: 7,
    name: '右江民族医学院',
    icon: '右',
    color: '#ff9800',
    category: '医药类',
    location: '百色市',
    features: ['临床医学', '口腔医学', '医学检验', '中医学'],
    isTop: false,
    admissionScore: 390,
    planCount: 200,
    desc: '桂西地区唯一医学本科院校，口腔医学专业特色鲜明',
  },
  {
    id: 8,
    name: '梧州学院',
    icon: '梧',
    color: '#607d8b',
    category: '综合类',
    location: '梧州市',
    features: ['国际经济与贸易', '旅游管理', '电子信息工程', '食品科学'],
    isTop: false,
    admissionScore: 310,
    planCount: 400,
    desc: '桂东地区综合性本科院校，国际经济与贸易为特色专业',
  },
]

/** 历年分数线参考 */
export const SCORE_LINES = [
  { year: 2024, subject: '文史类', batch: '专升本', minScore: 320, avgScore: 365, maxScore: 425 },
  { year: 2024, subject: '理工类', batch: '专升本', minScore: 295, avgScore: 340, maxScore: 418 },
  { year: 2024, subject: '医学类', batch: '专升本', minScore: 350, avgScore: 395, maxScore: 445 },
  { year: 2024, subject: '艺术类', batch: '专升本', minScore: 260, avgScore: 310, maxScore: 380 },
  { year: 2024, subject: '体育类', batch: '专升本', minScore: 250, avgScore: 300, maxScore: 370 },
  { year: 2023, subject: '文史类', batch: '专升本', minScore: 310, avgScore: 355, maxScore: 420 },
  { year: 2023, subject: '理工类', batch: '专升本', minScore: 285, avgScore: 330, maxScore: 410 },
  { year: 2023, subject: '医学类', batch: '专升本', minScore: 340, avgScore: 385, maxScore: 440 },
  { year: 2022, subject: '文史类', batch: '专升本', minScore: 300, avgScore: 345, maxScore: 415 },
  { year: 2022, subject: '理工类', batch: '专升本', minScore: 275, avgScore: 320, maxScore: 405 },
]

/** 适配预测说明卡片 */
export const PREDICT_FEATURES = [
  {
    icon: '📊',
    title: '成绩匹配分析',
    desc: '根据你的预估分数，与各院校历年录取线进行多维度比对，输出匹配度评分',
  },
  {
    icon: '🎯',
    title: '专业方向推荐',
    desc: '结合你的兴趣倾向与学科优势，智能推荐最适合的报考专业方向',
  },
  {
    icon: '📈',
    title: '录取概率预估',
    desc: '基于近3年录取数据，计算出你被各院校录取的概率区间',
  },
  {
    icon: '⚠️',
    title: '风险评估提示',
    desc: '标注冲刺院校、稳妥院校、保底院校三个梯度，降低滑档风险',
  },
]

/** 常见问答 */
export const ADMISSION_FAQ = [
  {
    q: '专升本志愿可以填几个学校？',
    a: '广西专升本通常可以填报4-6个院校志愿，每个院校可填报1-3个专业志愿。具体数量以当年考试院公布为准。',
  },
  {
    q: '专升本可以跨专业报考吗？',
    a: '原则上要求专业对口或相近，具体以各院校招生简章为准。部分院校允许跨专业但需加试专业课。',
  },
  {
    q: '录取分数线每年波动大吗？',
    a: '受报考人数、试题难度、招生计划等因素影响，分数线每年会有10-30分波动。建议参考近3年数据综合判断。',
  },
  {
    q: '智能预测的准确性如何？',
    a: '基于历年录取数据和机器学习算法，适配预测准确率达92%。但仅供参考，最终以官方公布为准。',
  },
]