<template>
  <NavHeader />
  <div class="page-wrapper">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
  <SiteFooter />

  <LoginModal
    :visible="authStore.loginRequired"
    @close="authStore.clearLoginRequired()"
    @logged-in="authStore.clearLoginRequired()"
  />
</template>

<script setup>
import NavHeader from '@/components/NavHeader.vue'
import SiteFooter from '@/components/SiteFooter.vue'
import LoginModal from '@/components/auth/LoginModal.vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<style lang="scss" scoped>
.page-wrapper {
  position: relative;
  overflow: hidden;
  min-height: calc(100vh - 140px);
}

.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(32px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

.fade-enter-to,
.fade-leave-from {
  opacity: 1;
  transform: translateY(0);
}

</style>
