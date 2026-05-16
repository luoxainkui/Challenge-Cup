<template>
  <section class="cta">
    <h2>准备好开启你的本科之路了吗？</h2>
    <p>加入桂升通，让专业团队助你圆梦本科</p>
    <a href="/courses" class="btn-primary" @click.prevent="$router.push('/courses')">立即开始</a>
  </section>
</template>

<style lang="scss" scoped>
@use '@/assets/styles/base/variables' as *;

.cta {
  padding: 80px 0;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  h2 {
    font-size: $font-size-3xl;
    margin-bottom: 12px;
  }
  p {
    font-size: $font-size-md;
    opacity: 0.85;
    margin-bottom: 28px;
  }
}

.btn-primary {
  display: inline-block;
  padding: 14px 36px;
  background: #fff;
  color: $color-primary;
  border-radius: $radius-full;
  font-weight: $font-weight-semibold;
  font-size: $font-size-md;
  text-decoration: none;
  transition: all $transition-base;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
  }
}
</style>