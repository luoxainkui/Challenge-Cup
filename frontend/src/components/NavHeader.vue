<template>
  <header class="header">
    <div class="header-container">
      <div class="logo" @click="$router.push('/')">
        <div class="logo-icon">桂</div>
        <span class="logo-text">桂升通</span>
      </div>
      <nav class="nav-list">
        <router-link to="/" class="nav-link" active-class="active">首页</router-link>
        <div class="nav-dropdown" @mouseenter="showMenu = true" @mouseleave="showMenu = false">
          <span class="nav-link" :class="{ active: isServiceActive }">核心服务</span>
          <transition name="dropdown-fade">
            <div v-show="showMenu" class="dropdown-menu">
              <router-link to="/services/courses">精讲课程</router-link>
              <router-link to="/services/quiz">智能题库</router-link>
              <router-link to="/services/mentor">伴学服务</router-link>
            </div>
          </transition>
        </div>
        <router-link to="/courses" class="nav-link" active-class="active">课程中心</router-link>
        <router-link to="/about" class="nav-link" active-class="active">关于我们</router-link>
        <router-link to="/login" class="nav-link nav-auth" active-class="active">登录</router-link>
      </nav>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const showMenu = ref(false)

const isServiceActive = computed(() => route.path.startsWith('/services'))
</script>

<style lang="scss" scoped>
.header {
  width: 100%;
  height: $header-height;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  position: fixed;
  top: 0;
  left: 0;
  z-index: 999;
}

.header-container {
  width: $max-width;
  height: 100%;
  margin: 0 auto;
  @include flex-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  cursor: pointer;
}

.logo-icon {
  width: 50px;
  height: 50px;
  background: $color-primary;
  color: #fff;
  border-radius: $radius-lg;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: $font-size-3xl;
  font-weight: $font-weight-bold;
}

.logo-text {
  font-size: $font-size-3xl;
  font-weight: $font-weight-bold;
  color: $color-primary;
}

.nav-list {
  display: flex;
  gap: 40px;
  align-items: center;
}

.nav-link {
  text-decoration: none;
  color: $color-text-secondary;
  font-size: $font-size-md;
  font-weight: $font-weight-medium;
  transition: color $transition-base;
  padding: 8px 0;
  display: inline-block;
  cursor: pointer;
  border-bottom: 2px solid transparent;

  &:hover,
  &.active {
    color: $color-primary;
    border-bottom-color: $color-primary;
  }
}

.nav-dropdown {
  position: relative;
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #fff;
  border-radius: $radius-xl;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
  padding: 8px 0;
  min-width: 140px;
  z-index: 1000;
  margin-top: 4px;

  a {
    display: block;
    padding: 10px 20px;
    font-size: $font-size-base;
    color: #555;
    text-decoration: none;
    transition: all $transition-fast;
    white-space: nowrap;

    &:hover {
      background: $color-primary-light;
      color: $color-primary;
    }
  }
}

.dropdown-fade-enter-active,
.dropdown-fade-leave-active {
  transition: opacity $transition-fast, transform $transition-fast;
}
.dropdown-fade-enter-from,
.dropdown-fade-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(-4px);
}

@include respond-to('desktop') {
  .header-container {
    width: 100%;
    padding: 0 20px;
  }
}

@include respond-to('tablet') {
  .nav-list {
    display: none;
  }
}
</style>