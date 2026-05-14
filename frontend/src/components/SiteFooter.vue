<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-brand">
        <h3>桂升通</h3>
        <p>广西专升本一站式服务平台</p>
      </div>
      <div class="footer-links">
        <div class="link-group">
          <h4>产品服务</h4>
          <router-link to="/services/courses">精讲课程</router-link>
          <router-link to="/services/quiz">智能题库</router-link>
          <router-link to="/services/mentor">伴学服务</router-link>
        </div>
        <div class="link-group">
          <h4>关于我们</h4>
          <router-link to="/about">公司介绍</router-link>
          <a href="#">服务协议</a>
          <a href="#">隐私政策</a>
        </div>
        <div class="link-group">
          <h4>联系我们</h4>
          <a href="#">客服热线：400-888-0000</a>
          <a href="#">工作日 9:00-18:00</a>
          <a href="#">邮箱：contact@guishengtong.cn</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2025 桂升通 版权所有 | 桂ICP备xxxxxxxx号</span>
    </div>
  </footer>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.footer {
  background: #1a1f2e;
  color: #ccc;
  padding-top: 48px;
}

.footer-container {
  width: $max-width;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  gap: 60px;
  flex-wrap: wrap;
}

.footer-brand {
  h3 {
    font-size: $font-size-2xl;
    color: #fff;
    margin-bottom: 8px;
  }
  p {
    font-size: $font-size-base;
  }
}

.footer-links {
  display: flex;
  gap: 60px;
  flex-wrap: wrap;
}

.link-group {
  h4 {
    color: #fff;
    margin-bottom: 16px;
    font-size: $font-size-md;
  }

  a {
    display: block;
    color: #999;
    text-decoration: none;
    font-size: $font-size-base;
    margin-bottom: 12px;
    transition: color $transition-fast;

    &:hover {
      color: #fff;
    }
  }
}

.footer-bottom {
  margin-top: 40px;
  padding: 20px 0;
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  font-size: $font-size-xs;
  color: #666;
}

@include respond-to('desktop') {
  .footer-container {
    width: 100%;
    padding: 0 20px;
  }
}

@include respond-to('tablet') {
  .footer-container {
    flex-direction: column;
    gap: 30px;
  }
  .footer-links {
    gap: 20px;
  }
}
</style>