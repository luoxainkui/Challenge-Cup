// ========== 题库统计 ==========
export const QUIZ_STATISTICS = [
  { num: '12,800+', label: '题目总数' },
  { num: '8', label: '科目覆盖' },
  { num: '98.6%', label: '答案解析率' },
  { num: '50万+', label: '累计刷题人次' },
]

// ========== 练习模式 ==========
export const QUIZ_MODES = [
  { id: 'chapter', icon: '📖', name: '章节练习', desc: '按知识点章节逐项突破，夯实基础', count: '1,200+ 章节' },
  { id: 'mock', icon: '📝', name: '模拟考试', desc: '全真模拟考试环境，计时作答体验真实考场', count: '48 套模拟卷' },
  { id: 'real', icon: '📄', name: '历年真题', desc: '收录近5年广西专升本真题，掌握命题规律', count: '15 套真题' },
  { id: 'mistake', icon: '🔲', name: '错题本', desc: '自动收录错题，针对性强化薄弱知识点', count: '智能归类分析' },
]

// ========== 科目 ==========
export const QUIZ_SUBJECTS = [
  { name: '大学英语', icon: 'EN', color: '#2a6eff', count: 2850, progress: 35 },
  { name: '高等数学', icon: '数', color: '#ff6b35', count: 2100, progress: 22 },
  { name: '大学语文', icon: '语', color: '#9c27b0', count: 1980, progress: 48 },
  { name: '政治理论', icon: '政', color: '#e74c3c', count: 1650, progress: 60 },
  { name: '管理学', icon: '管', color: '#4caf50', count: 1420, progress: 15 },
  { name: '会计学', icon: '会', color: '#008888', count: 980, progress: 8 },
  { name: '计算机', icon: '计', color: '#ff9800', count: 1120, progress: 30 },
  { name: '经济学', icon: '经', color: '#607d8b', count: 700, progress: 5 },
]

// ========== 题目类型定义 ==========
export const QUESTION_TYPES = {
  single:   { label: '单选题', icon: '①' },
  multi:    { label: '多选题', icon: '☑' },
  truefalse:{ label: '判断题', icon: '✓' },
  fill:     { label: '填空题', icon: '✎' },
}

// ========== 模拟考试试卷 ==========
export const MOCK_PAPERS = [
  { id: 'mock-1', name: '模拟试卷一', subject: '综合', duration: 120, total: 50 },
  { id: 'mock-2', name: '模拟试卷二', subject: '综合', duration: 120, total: 50 },
  { id: 'mock-3', name: '模拟试卷三', subject: '综合', duration: 120, total: 50 },
]

// ========== 历年真题试卷 ==========
export const REAL_PAPERS = [
  { id: 'real-2024', name: '2024年真题', subject: '综合', duration: 120, total: 50 },
  { id: 'real-2023', name: '2023年真题', subject: '综合', duration: 120, total: 50 },
  { id: 'real-2022', name: '2022年真题', subject: '综合', duration: 120, total: 50 },
]

// ========== 章节列表 ==========
export const CHAPTERS = QUIZ_SUBJECTS.map(s => ({
  name: s.name,
  color: s.color,
  icon: s.icon,
  topics: [
    { id: s.name.replace(/[^\w]/g, '') + '-t1', name: '基础概念与原理', count: Math.floor(s.count * 0.3) },
    { id: s.name.replace(/[^\w]/g, '') + '-t2', name: '核心应用与计算', count: Math.floor(s.count * 0.4) },
    { id: s.name.replace(/[^\w]/g, '') + '-t3', name: '综合拔高与拓展', count: Math.floor(s.count * 0.3) },
  ]
}))

// ========== 错题本：考点定义 ==========
export const EXAM_POINTS = [
  { id: 'vocab', name: '词汇与语法', subject: '大学英语' },
  { id: 'reading', name: '阅读理解', subject: '大学英语' },
  { id: 'writing', name: '写作与翻译', subject: '大学英语' },
  { id: 'function', name: '函数与极限', subject: '高等数学' },
  { id: 'derivative', name: '导数与微分', subject: '高等数学' },
  { id: 'integral', name: '积分及应用', subject: '高等数学' },
  { id: 'classical', name: '文言文阅读', subject: '大学语文' },
  { id: 'poetry', name: '诗词鉴赏', subject: '大学语文' },
  { id: 'philosophy', name: '马克思主义哲学', subject: '政治理论' },
  { id: 'socialism', name: '中国特色社会主义', subject: '政治理论' },
  { id: 'management', name: '管理概述与决策', subject: '管理学' },
  { id: 'organization', name: '组织设计与文化', subject: '管理学' },
  { id: 'accounting', name: '会计基础与凭证', subject: '会计学' },
  { id: 'finance', name: '财务报表编制', subject: '会计学' },
  { id: 'office', name: 'Office办公应用', subject: '计算机' },
  { id: 'network', name: '网络与安全基础', subject: '计算机' },
  { id: 'demand', name: '需求与供给理论', subject: '经济学' },
  { id: 'macro', name: '宏观经济学基础', subject: '经济学' },
]

// ========== 完整题库（多题型） ==========
export const ALL_QUESTIONS = [
  // ---- 单选 ----
  { id: 1, pointId: 'vocab', type: 'single', difficulty: 1, stem: 'The manager asked his secretary to _____ the document before the meeting.', options: ['A. prepare', 'B. preparing', 'C. prepared', 'D. prepares'], answer: [0], analysis: 'ask sb. to do sth. 是固定搭配，不定式作宾补。' },
  { id: 2, pointId: 'reading', type: 'single', difficulty: 2, stem: 'What is the main idea of the passage?\n\nEarly childhood education plays a crucial role in cognitive development. Studies show that children who receive quality preschool education perform better in later academic years...', options: ['A. Government policies on education', 'B. The importance of early childhood education', 'C. School funding allocation', 'D. Teacher training programs'], answer: [1], analysis: '文章首句为主题句，全文围绕早期儿童教育的重要性展开。' },
  { id: 3, pointId: 'writing', type: 'single', difficulty: 1, stem: '以下哪个是正式书信的正确开头？', options: ['A. Hey there,', 'B. Dear Sir/Madam,', 'C. Hi!', 'D. What\'s up?'], answer: [1], analysis: '正式书信应用 Dear Sir/Madam 作为开头，其他选项均为非正式用语。' },
  { id: 4, pointId: 'function', type: 'single', difficulty: 2, stem: '极限 \\(\\lim_{x \\to 0} \\frac{\\sin x}{x}\\) 的值为：', options: ['A. 0', 'B. 1', 'C. \\(\\infty\\)', 'D. 不存在'], answer: [1], analysis: '重要极限公式：\\(\\lim_{x \\to 0} \\frac{\\sin x}{x} = 1\\)。' },
  { id: 5, pointId: 'derivative', type: 'single', difficulty: 2, stem: '函数 \\(f(x) = x^3 - 3x\\) 的导数为：', options: ['A. \\(x^2 - 3\\)', 'B. \\(3x^2 - 3\\)', 'C. \\(3x^2 + 3\\)', 'D. \\(x^3 - 3\\)'], answer: [1], analysis: '\\(f\'(x) = 3x^2 - 3\\)，使用幂函数求导公式。' },
  { id: 6, pointId: 'integral', type: 'single', difficulty: 1, stem: '\\(\\int_0^1 2x\\,dx\\) 的值为：', options: ['A. 0.5', 'B. 1', 'C. 2', 'D. 0'], answer: [1], analysis: '\\(\\int_0^1 2x\\,dx = x^2|_0^1 = 1\\)。' },
  { id: 7, pointId: 'classical', type: 'single', difficulty: 1, stem: '“学而时习之，不亦说乎”出自：', options: ['A. 《孟子》', 'B. 《论语》', 'C. 《大学》', 'D. 《中庸》'], answer: [1], analysis: '此句出自《论语·学而》，是孔子关于学习方法的经典论述。' },
  { id: 8, pointId: 'poetry', type: 'single', difficulty: 1, stem: '"床前明月光"的作者是：', options: ['A. 杜甫', 'B. 白居易', 'C. 李白', 'D. 王维'], answer: [2], analysis: '此诗句出自李白《静夜思》，是千古传诵的思乡名篇。' },
  { id: 9, pointId: 'philosophy', type: 'single', difficulty: 1, stem: '马克思主义哲学认为世界的本质是：', options: ['A. 意识', 'B. 物质', 'C. 绝对精神', 'D. 感觉'], answer: [1], analysis: '马克思主义哲学坚持唯物主义一元论，认为世界的本质是物质。' },
  { id: 10, pointId: 'socialism', type: 'single', difficulty: 2, stem: '中国特色社会主义进入新时代，我国社会主要矛盾已经转化为：', options: ['A. 人民日益增长的物质文化需要同落后的社会生产之间的矛盾', 'B. 人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾', 'C. 经济发展与环境保护之间的矛盾', 'D. 城乡发展不平衡的矛盾'], answer: [1], analysis: '党的十九大报告明确指出社会主要矛盾已经转化。' },
  { id: 11, pointId: 'management', type: 'single', difficulty: 1, stem: '管理的首要职能是：', options: ['A. 组织', 'B. 领导', 'C. 计划', 'D. 控制'], answer: [2], analysis: '计划是管理的首要职能，为其他管理活动提供方向和标准。' },
  { id: 12, pointId: 'organization', type: 'single', difficulty: 2, stem: '事业部制组织结构的最大优点是：', options: ['A. 节约管理成本', 'B. 利于培养全面管理人才', 'C. 指挥高度统一', 'D. 部门沟通便捷'], answer: [1], analysis: '事业部制使各事业部负责人独立经营核算，有利于培养全面管理人才。' },
  { id: 13, pointId: 'accounting', type: 'single', difficulty: 1, stem: '借贷记账法的理论基础是：', options: ['A. 收付实现制', 'B. 权责发生制', 'C. 资产=负债+所有者权益', 'D. 收入-费用=利润'], answer: [2], analysis: '借贷记账法基于会计恒等式：资产＝负债＋所有者权益。' },
  { id: 14, pointId: 'finance', type: 'single', difficulty: 1, stem: '资产负债表中，流动资产不包括：', options: ['A. 应收账款', 'B. 存货', 'C. 固定资产', 'D. 货币资金'], answer: [2], analysis: '固定资产属于非流动资产，在资产负债表中单独列示。' },
  { id: 15, pointId: 'office', type: 'single', difficulty: 1, stem: '在Excel中，函数 SUM(A1:A5) 的作用是：', options: ['A. 求平均值', 'B. 求和', 'C. 求最大值', 'D. 计数'], answer: [1], analysis: 'SUM 是求和函数，计算指定区域的数值总和。' },
  { id: 16, pointId: 'network', type: 'single', difficulty: 1, stem: 'HTTP协议的默认端口号是：', options: ['A. 21', 'B. 80', 'C. 443', 'D. 25'], answer: [1], analysis: 'HTTP 默认使用 80 端口，HTTPS 使用 443 端口。' },
  { id: 17, pointId: 'demand', type: 'single', difficulty: 1, stem: '在其他条件不变时，商品价格上升会导致：', options: ['A. 需求增加', 'B. 需求减少', 'C. 供给减少', 'D. 需求不变'], answer: [1], analysis: '根据需求定律，在其他条件不变时，价格与需求量呈反向关系。' },
  { id: 18, pointId: 'macro', type: 'single', difficulty: 1, stem: 'GDP 的全称是：', options: ['A. 国民生产总值（GNP）', 'B. 国内生产总值', 'C. 国民收入（NI）', 'D. 个人可支配收入（DPI）'], answer: [1], analysis: 'GDP 即 Gross Domestic Product，衡量一国在特定时期内生产的全部最终产品与服务的市场价值。' },

  // ---- 多选 ----
  { id: 101, pointId: 'vocab', type: 'multi', difficulty: 2, stem: '以下哪些短语表示"参加"？', options: ['A. take part in', 'B. participate in', 'C. look forward to', 'D. join in'], answer: [0, 1, 3], analysis: 'take part in、participate in、join in 均表示"参加"。look forward to 表示"期待"。' },
  { id: 102, pointId: 'management', type: 'multi', difficulty: 2, stem: '管理的四大基本职能包括：', options: ['A. 计划', 'B. 组织', 'C. 创新', 'D. 领导', 'E. 控制'], answer: [0, 1, 3, 4], analysis: '管理的四大基本职能为：计划、组织、领导、控制。创新是管理的拓展职能。' },
  { id: 103, pointId: 'function', type: 'multi', difficulty: 3, stem: '以下哪些函数的导数等于其自身？', options: ['A. \\(f(x) = e^x\\)', 'B. \\(f(x) = \\sin x\\)', 'C. \\(f(x) = Ce^x\\)（C为常数）', 'D. \\(f(x) = x^2\\)'], answer: [0, 2], analysis: '\\(e^x\\) 的导数仍为 \\(e^x\\)，\\(Ce^x\\) 同理。\\(\\sin x\\) 的导数为 \\(\\cos x\\)，\\(x^2\\) 的导数为 \\(2x\\)。' },
  { id: 104, pointId: 'socialism', type: 'multi', difficulty: 2, stem: '"四个全面"战略布局包括：', options: ['A. 全面建设社会主义现代化国家', 'B. 全面深化改革', 'C. 全面依法治国', 'D. 全面对外开放', 'E. 全面从严治党'], answer: [0, 1, 2, 4], analysis: '"四个全面"指全面建设社会主义现代化国家、全面深化改革、全面依法治国、全面从严治党。' },
  { id: 105, pointId: 'network', type: 'multi', difficulty: 2, stem: '以下哪些属于网络传输层协议？', options: ['A. TCP', 'B. IP', 'C. UDP', 'D. HTTP'], answer: [0, 2], analysis: 'TCP 和 UDP 是传输层协议。IP 是网络层协议，HTTP 是应用层协议。' },

  // ---- 判断 ----
  { id: 201, pointId: 'demand', type: 'truefalse', difficulty: 1, stem: '在其他条件不变时，替代品价格上升会导致本商品需求下降。', options: [], answer: [1], analysis: '替代品价格上升会使得消费者转向购买本商品，因此本商品需求增加而非下降。故此判断为错误。' },
  { id: 202, pointId: 'accounting', type: 'truefalse', difficulty: 1, stem: '权责发生制是以现金的实际收付作为确认收入和费用的标准。', options: [], answer: [1], analysis: '权责发生制以权利义务的发生为确认基础，以现金收付为标准的叫收付实现制。故此判断为错误。' },
  { id: 203, pointId: 'philosophy', type: 'truefalse', difficulty: 1, stem: '意识是人脑对客观存在的主观映象。', options: [], answer: [0], analysis: '这是马克思主义哲学对意识的科学定义。故此判断为正确。' },
  { id: 204, pointId: 'classical', type: 'truefalse', difficulty: 1, stem: '"三人行，必有我师焉"出自《孟子》。', options: [], answer: [1], analysis: '此句出自《论语·述而》，是孔子的话语，非《孟子》。故此判断为错误。' },
  { id: 205, pointId: 'office', type: 'truefalse', difficulty: 1, stem: '在Word中，Ctrl+S 是保存文档的快捷键。', options: [], answer: [0], analysis: 'Ctrl+S 确实是 Word 保存文档的快捷键。故此判断为正确。' },

  // ---- 填空 ----
  { id: 301, pointId: 'reading', type: 'fill', difficulty: 2, stem: 'A healthy diet should include a variety of _____ and vegetables.', options: [], answer: [0], analysis: '根据语境和搭配，应填入 fruits。"fruits and vegetables" 是常见搭配。' },
  { id: 302, pointId: 'function', type: 'fill', difficulty: 2, stem: '函数 \\(f(x) = x^2\\) 在 \\(x = 2\\) 处的导数值为 _____。', options: [], answer: [0], analysis: '\\(f\'(x) = 2x\\)，代入 \\(x = 2\\) 得 \\(f\'(2) = 4\\)。' },
  { id: 303, pointId: 'poetry', type: 'fill', difficulty: 2, stem: '"春眠不觉晓，处处闻啼_____"（填入缺失的字）', options: [], answer: [0], analysis: '出自孟浩然《春晓》：春眠不觉晓，处处闻啼鸟。' },
  { id: 304, pointId: 'socialism', type: 'fill', difficulty: 2, stem: '实现中华民族伟大复兴，就是中华民族近代以来最伟大的_____。', options: [], answer: [0], analysis: '"中国梦"的完整表述。应填入"梦想"。' },
  { id: 305, pointId: 'macro', type: 'fill', difficulty: 2, stem: '通货膨胀是指一国货币的购买力持续_____的现象。', options: [], answer: [0], analysis: '通货膨胀意味着货币购买力下降。"下降" 或 "降低"。' },
]

// ========== 错题本：示例题目（独立引用，保持兼容） ==========
export const SAMPLE_QUESTIONS = ALL_QUESTIONS.filter(q => q.type === 'single')

// ========== 错题本：初始错题种子数据 ==========
export const INITIAL_MISTAKES = [
  { questionId: 1, wrongCount: 3, correctCount: 1, lastWrongAt: '2025-05-10' },
  { questionId: 4, wrongCount: 2, correctCount: 0, lastWrongAt: '2025-05-12' },
  { questionId: 7, wrongCount: 1, correctCount: 0, lastWrongAt: '2025-05-14' },
  { questionId: 9, wrongCount: 4, correctCount: 2, lastWrongAt: '2025-05-13' },
  { questionId: 11, wrongCount: 2, correctCount: 1, lastWrongAt: '2025-05-11' },
  { questionId: 15, wrongCount: 1, correctCount: 0, lastWrongAt: '2025-05-15' },
]