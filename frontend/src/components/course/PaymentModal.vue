<template>
  <Teleport to="body">
    <transition name="modal">
      <div class="modal-overlay" v-if="show" @click.self="$emit('close')">
        <div class="modal-card">
          <button class="modal-close" @click="$emit('close')">✕</button>

          <div class="modal-header">
            <h3>确认报名</h3>
            <p>您即将报名课程</p>
          </div>

          <div class="modal-course" v-if="course">
            <div class="modal-course-icon" :style="{ background: course.color }"></div>
            <div class="modal-course-info">
              <h4>{{ course.name }}</h4>
              <span>{{ course.teacher }}</span>
            </div>
          </div>

          <div class="modal-summary">
            <div class="summary-row">
              <span>课程价格</span>
              <span>¥{{ course?.price }}</span>
            </div>
            <div class="summary-row total">
              <span>应付金额</span>
              <span class="total-price">¥{{ course?.price }}</span>
            </div>
          </div>

          <!-- 支付方式 -->
          <div class="payment-methods">
            <h4>选择支付方式</h4>
            <div class="methods-grid">
              <button
                v-for="m in methods"
                :key="m.key"
                :class="{ active: selectedMethod === m.key }"
                @click="selectedMethod = m.key"
                class="method-btn"
              >
                <span class="method-icon">{{ m.icon }}</span>
                <span>{{ m.label }}</span>
              </button>
            </div>
          </div>

          <div class="modal-actions">
            <button class="btn-cancel" @click="$emit('close')">取消</button>
            <button class="btn-confirm" @click="handlePay" :disabled="paying">
              {{ paying ? '支付中...' : `确认支付 ¥${course?.price}` }}
            </button>
          </div>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  show: { type: Boolean, default: false },
  course: { type: Object, default: null },
})

const emit = defineEmits(['close', 'success'])

const selectedMethod = ref('wechat')
const paying = ref(false)

const methods = [
  { key: 'wechat', label: '微信支付', icon: '💬' },
  { key: 'alipay', label: '支付宝', icon: '🔵' },
  { key: 'card', label: '银行卡', icon: '💳' },
]

function handlePay() {
  paying.value = true
  // 模拟支付流程
  setTimeout(() => {
    paying.value = false
    emit('success', props.course)
  }, 1500)
}
</script>

<style lang="scss" scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.45);
  backdrop-filter: blur(4px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-card {
  background: #fff;
  border-radius: $radius-2xl;
  padding: 32px;
  width: 440px;
  max-height: 90vh;
  overflow-y: auto;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.modal-close {
  position: absolute;
  top: 16px;
  right: 16px;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  border: none;
  background: #f2f4f7;
  cursor: pointer;
  font-size: 16px;
  color: $color-text-tertiary;
  display: flex;
  align-items: center;
  justify-content: center;

  &:hover {
    background: #e2e5eb;
    color: $color-text-primary;
  }
}

.modal-header {
  text-align: center;
  margin-bottom: 24px;

  h3 {
    font-size: $font-size-xl;
    font-weight: $font-weight-bold;
    margin-bottom: 4px;
  }

  p {
    font-size: $font-size-sm;
    color: $color-text-tertiary;
  }
}

.modal-course {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px;
  background: #f8faff;
  border-radius: $radius-lg;
  margin-bottom: 20px;
}

.modal-course-icon {
  width: 48px;
  height: 48px;
  border-radius: $radius-md;
  flex-shrink: 0;
}

.modal-course-info {
  h4 {
    font-size: $font-size-base;
    font-weight: $font-weight-semibold;
    margin-bottom: 2px;
  }

  span {
    font-size: $font-size-xs;
    color: $color-text-tertiary;
  }
}

.modal-summary {
  margin-bottom: 24px;

  .summary-row {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    font-size: $font-size-base;
    color: $color-text-tertiary;

    &.total {
      border-top: 1px dashed #e5e8ed;
      margin-top: 8px;
      padding-top: 14px;
      font-weight: $font-weight-bold;
      color: $color-text-primary;

      .total-price {
        font-size: $font-size-xl;
        color: $color-accent;
      }
    }
  }
}

.payment-methods {
  margin-bottom: 24px;

  h4 {
    font-size: $font-size-sm;
    font-weight: $font-weight-semibold;
    margin-bottom: 12px;
    color: $color-text-primary;
  }
}

.methods-grid {
  display: flex;
  gap: 10px;
}

.method-btn {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  padding: 14px 8px;
  border: 2px solid #edf0f5;
  border-radius: $radius-lg;
  background: #fff;
  cursor: pointer;
  font-size: $font-size-xs;
  color: $color-text-tertiary;
  transition: all $transition-fast;

  .method-icon {
    font-size: 24px;
  }

  &:hover {
    border-color: #c0c8d6;
  }

  &.active {
    border-color: $color-primary;
    background: #f0f6ff;
    color: $color-primary;
    font-weight: $font-weight-medium;
  }
}

.modal-actions {
  display: flex;
  gap: 12px;
}

.btn-cancel {
  flex: 1;
  padding: 13px;
  border: 1px solid #e5e8ed;
  background: #fff;
  border-radius: $radius-full;
  font-size: $font-size-base;
  color: $color-text-tertiary;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover {
    background: #f5f6f8;
  }
}

.btn-confirm {
  flex: 2;
  padding: 13px;
  border: none;
  background: $color-primary;
  color: #fff;
  border-radius: $radius-full;
  font-size: $font-size-base;
  font-weight: $font-weight-semibold;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover:not(:disabled) {
    background: #4758e0;
    transform: translateY(-1px);
  }

  &:disabled {
    opacity: 0.6;
    cursor: not-allowed;
  }
}

/* Modal transition */
.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.25s ease;

  .modal-card {
    transition: transform 0.25s ease;
  }
}

.modal-enter-from,
.modal-leave-to {
  opacity: 0;

  .modal-card {
    transform: scale(0.92);
  }
}
</style>