<template>
  <div class="page-container">
    <div class="form-box">
      <div class="form-header">
        <div class="form-logo">桂</div>
        <h2 class="form-title">登录桂升通</h2>
      </div>
      <div class="input-group">
        <input type="text" placeholder="手机号 / 邮箱" />
      </div>
      <div class="input-group">
        <input type="password" placeholder="密码" />
      </div>
      <button class="form-btn">登 录</button>
      <div class="form-links">
        <router-link to="/register">立即注册</router-link>
        <span>|</span>
        <a href="#">忘记密码</a>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>