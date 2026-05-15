<template>
  <div class="qp-sub-page">
    <header class="qp-sub-header">
      <button class="qp-sub-back" @click="router.push({ name: 'service-quiz' })">← 返回题库</button>
      <h1 class="qp-sub-title">错题本</h1>
      <span class="qp-sub-count">{{ mistakeCount }} 道错题</span>
    </header>

    <div class="qp-sub-body">
      <MistakeStats :mistake-count="mistakeCount" :mistake-rate="mistakeRate" :mastery-rate="masteryRate" />
      <MistakeCharts
        :subject-data="subjectDistribution"
        :subject-max="subjectMax"
        :type-data="typeDistribution"
        :type-max="typeMax"
      />
      <RemoveToggle v-model="autoRemoveEnabled" :threshold="autoRemoveThreshold" @update:threshold="autoRemoveThreshold = $event" />
      <MistakeDistribution :distribution="pointDistribution" :max-count="maxPointCount" />
      <MistakeList :list="mistakeList" @correct="recordCorrect" @wrong="recordWrong" @remove="removeMistake" @clear="clearAll" />
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { useMistakeBook } from '@/composables/useMistakeBook'
import MistakeStats from '@/components/quiz/MistakeStats.vue'
import MistakeCharts from '@/components/quiz/MistakeCharts.vue'
import RemoveToggle from '@/components/quiz/RemoveToggle.vue'
import MistakeDistribution from '@/components/quiz/MistakeDistribution.vue'
import MistakeList from '@/components/quiz/MistakeList.vue'

const router = useRouter()

const {
  autoRemoveEnabled,
  autoRemoveThreshold,
  mistakeList,
  mistakeCount,
  mistakeRate,
  masteryRate,
  pointDistribution,
  maxPointCount,
  subjectDistribution,
  subjectMax,
  typeDistribution,
  typeMax,
  recordCorrect,
  recordWrong,
  removeMistake,
  clearAll,
} = useMistakeBook()
</script>

<style lang="scss" scoped>
.qp-sub-page {
  min-height: 100vh;
  background: #f5f6fa;
  padding: $header-height 20px 60px;
}
.qp-sub-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 0;
  max-width: $max-width;
  margin: 0 auto;
}
.qp-sub-back {
  padding: 8px 18px;
  font-size: $font-size-xs;
  border: 1px solid #e0e0e0;
  background: #fff;
  border-radius: $radius-md;
  color: $color-text-secondary;
  cursor: pointer;
  &:hover { color: $color-primary; border-color: $color-primary; }
}
.qp-sub-title {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
}
.qp-sub-count {
  font-size: $font-size-sm;
  color: $color-text-muted;
}
.qp-sub-body {
  max-width: $max-width;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>