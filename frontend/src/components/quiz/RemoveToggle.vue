<template>
  <div class="remove-toggle">
    <label class="toggle-row">
      <span class="toggle-label">自动移除错题</span>
      <span class="toggle-switch" :class="{ active: modelValue }" @click="$emit('update:modelValue', !modelValue)">
        <span class="toggle-knob"></span>
      </span>
    </label>
    <div class="toggle-sub" v-if="modelValue">
      <span>连续答对</span>
      <button class="num-btn" :class="{ active: threshold === 2 }" @click="$emit('update:threshold', 2)">2</button>
      <button class="num-btn" :class="{ active: threshold === 3 }" @click="$emit('update:threshold', 3)">3</button>
      <button class="num-btn" :class="{ active: threshold === 5 }" @click="$emit('update:threshold', 5)">5</button>
      <span>次后移除</span>
    </div>
  </div>
</template>

<script setup>
defineProps({
  modelValue: { type: Boolean, default: true },
  threshold: { type: Number, default: 3 },
})

defineEmits(['update:modelValue', 'update:threshold'])
</script>

<style lang="scss" scoped>
.remove-toggle {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  padding: 14px 20px;
  background: #fff;
  border-radius: $radius-lg;
  box-shadow: 0 1px 6px rgba(0,0,0,.04);
  margin-bottom: 20px;
}
.toggle-row {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}
.toggle-label {
  font-size: $font-size-sm;
  color: $color-text-primary;
  font-weight: $font-weight-medium;
}
.toggle-switch {
  width: 44px;
  height: 24px;
  background: #d0d5dd;
  border-radius: $radius-full;
  position: relative;
  transition: background $transition-fast;
  &.active { background: $color-primary; }
}
.toggle-knob {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 20px;
  height: 20px;
  background: #fff;
  border-radius: 50%;
  transition: left $transition-fast;
  .active & { left: 22px; }
}
.toggle-sub {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: $font-size-xs;
  color: $color-text-tertiary;
}
.num-btn {
  width: 28px;
  height: 28px;
  border: 1.5px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-md;
  font-size: $font-size-xs;
  font-weight: $font-weight-medium;
  color: $color-text-secondary;
  cursor: pointer;
  transition: all $transition-fast;
  &:hover { border-color: $color-primary; }
  &.active { background: $color-primary; color: #fff; border-color: $color-primary; }
}
</style>