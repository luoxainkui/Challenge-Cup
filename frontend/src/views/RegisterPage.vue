<template>
  <div class="page-container">
    <div class="form-box">
      <div class="form-header">
        <div class="form-logo">桂</div>
        <h2 class="form-title">注册桂升通</h2>
      </div>
      <div class="input-group">
        <input type="text" placeholder="手机号" />
      </div>
      <div class="code-input">
        <input type="text" placeholder="验证码" />
        <button class="code-btn">获取验证码</button>
      </div>
      <div class="input-group">
        <input type="password" placeholder="设置密码" />
      </div>
      <div class="input-group">
        <input type="password" placeholder="确认密码" />
      </div>
      <button class="form-btn">注 册</button>
      <div class="form-links">
        <span>已有账号？</span>
        <router-link to="/login">立即登录</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>