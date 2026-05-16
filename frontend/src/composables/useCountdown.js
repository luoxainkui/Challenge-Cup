import { ref } from 'vue'

/**
 * 验证码倒计时
 * @param {number} seconds - 倒计时秒数，默认 60
 * @returns {{ countdown, start, stop }}
 */
export function useCountdown(seconds = 60) {
  const countdown = ref(0)
  let timer = null

  function start() {
    stop()
    countdown.value = seconds
    timer = setInterval(() => {
      countdown.value--
      if (countdown.value <= 0) stop()
    }, 1000)
  }

  function stop() {
    clearInterval(timer)
    countdown.value = 0
  }

  return { countdown, start, stop }
}