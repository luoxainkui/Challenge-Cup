import { ref, reactive, nextTick } from 'vue'
import { KNOWLEDGE_BASE, WELCOME_MESSAGE } from '@/constants/consultation'

/**
 * AI 咨询聊天引擎
 * @param {Ref} chatBody - 聊天区域 DOM 引用
 */
export function useConsultation(chatBody) {
  const inputText = ref('')
  const typing = ref(false)
  const contactSubmitted = ref(false)
  const trialSubmitted = ref(false)

  const messages = ref([{ ...WELCOME_MESSAGE }])

  const trialForm = reactive({ name: '', phone: '', course: '' })
  const contactForm = reactive({ name: '', phone: '' })

  // ---- 关键词匹配答案 ----
  function findAnswer(question) {
    const q = question.toLowerCase()
    if (q.includes('政策') || q.includes('条件') || q.includes('要求') || q.includes('资格')) return KNOWLEDGE_BASE['政策']
    if (q.includes('时间') || q.includes('什么时候') || q.includes('几月') || q.includes('报考')) return KNOWLEDGE_BASE['报考时间']
    if (q.includes('课程') && (q.includes('区别') || q.includes('不同') || q.includes('哪个好'))) return KNOWLEDGE_BASE['区别']
    if (q.includes('课程') || q.includes('班') || q.includes('学什么')) return KNOWLEDGE_BASE['课程']
    if (q.includes('价格') || q.includes('费用') || q.includes('多少钱') || q.includes('优惠') || q.includes('分期')) return KNOWLEDGE_BASE['价格']
    if (q.includes('备考') || q.includes('复习') || q.includes('怎么学') || q.includes('计划') || q.includes('建议')) return KNOWLEDGE_BASE['备考']
    if (q.includes('电话') || q.includes('联系') || q.includes('地址') || q.includes('邮箱')) return KNOWLEDGE_BASE['电话']
    if (q.includes('试听') || q.includes('体验') || q.includes('预约')) return KNOWLEDGE_BASE['试听']
    if (q.includes('联系') || q.includes('咨询') || q.includes('顾问') || q.includes('微信')) return KNOWLEDGE_BASE['联系']
    return KNOWLEDGE_BASE['默认']
  }

  function scrollToBottom() {
    nextTick(() => {
      if (chatBody.value) chatBody.value.scrollTop = chatBody.value.scrollHeight
    })
  }

  function sendMessage(text) {
    const content = (text || inputText.value).trim()
    if (!content) return

    messages.value.push({ role: 'user', text: content.replace(/\n/g, '<br>'), showContact: false })
    if (!text) inputText.value = ''
    typing.value = true

    setTimeout(() => {
      typing.value = false
      const answer = findAnswer(content)
      const showContact = /联系|电话|微信|咨询|顾问|预约/.test(content)
      messages.value.push({ role: 'ai', text: answer, showContact })
      scrollToBottom()
    }, 800 + Math.random() * 600)
  }

  function submitContact() {
    if (!contactForm.name.trim() || !contactForm.phone.trim()) return
    contactSubmitted.value = true
    messages.value.push({
      role: 'ai',
      text: `感谢 <strong>${contactForm.name}</strong>！您的联系方式已记录，我们的课程顾问将尽快联系您（${contactForm.phone}），请保持手机畅通。`,
      showContact: false,
    })
    scrollToBottom()
  }

  function submitTrial() {
    if (!trialForm.name.trim() || !trialForm.phone.trim() || !trialForm.course) return
    trialSubmitted.value = true
    messages.value.push({
      role: 'ai',
      text: `&#127881; <strong>${trialForm.name}</strong>，您已成功预约 <strong>${trialForm.course}</strong> 试听课！我们的课程顾问将在 24 小时内与您联系（${trialForm.phone}）确认试听时间，敬请期待~`,
      showContact: false,
    })
    scrollToBottom()
  }

  return {
    inputText,
    typing,
    contactSubmitted,
    trialSubmitted,
    messages,
    trialForm,
    contactForm,
    sendMessage,
    submitContact,
    submitTrial,
    scrollToBottom,
  }
}