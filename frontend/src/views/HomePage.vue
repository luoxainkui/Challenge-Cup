<template>
  <div class="home-page">
    <HeroSection :stats="HOME_STATS" @scroll-to="scrollToSection" />
    <ServiceSection :courses="FEATURED_COURSES" />
    <AdvantageSection :advantages="ADVANTAGES" />
    <CtaSection />
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { HOME_STATS, ADVANTAGES } from '@/constants/home'
import { COURSES } from '@/constants/courses'
import HeroSection from '@/components/home/HeroSection.vue'
import ServiceSection from '@/components/home/ServiceSection.vue'
import AdvantageSection from '@/components/home/AdvantageSection.vue'
import CtaSection from '@/components/home/CtaSection.vue'

const FEATURED_COURSES = computed(() => COURSES.slice(0, 6))

function scrollToSection(id) {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}
</script>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.home-page {
  padding-top: $header-height;
}
</style>