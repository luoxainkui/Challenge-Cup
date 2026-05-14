<template>
  <div class="page-container">
    <!-- 课程中心头部 -->
    <div class="course-header">
      <h2 class="course-title">课程中心</h2>
      <div class="filter-bar">
        <select class="filter-select">
          <option>全部类别</option>
          <option>公共课</option>
          <option>专业课</option>
        </select>
        <div class="search-box">
          <input type="text" class="search-input" placeholder="搜索课程..." />
          <button class="search-btn">&#128269;</button>
        </div>
      </div>
    </div>

    <!-- 课程列表 -->
    <div class="course-list">
      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23e8f3ff' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%232a6eff' font-size='20'%3E大学英语%3C/text%3E%3C/svg%3E" alt="大学英语"/>
        <div class="course-info">
          <span class="course-category">公共课</span>
          <h3 class="course-name">专升本大学英语精讲班</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>张雪峰教授</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥299</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>

      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23fff3e8' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%23ff6b35' font-size='20'%3E高等数学%3C/text%3E%3C/svg%3E" alt="高等数学"/>
        <div class="course-info">
          <span class="course-category">公共课</span>
          <h3 class="course-name">专升本高等数学强化班</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>李明博士</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥359</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>

      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23f0ffe8' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%234caf50' font-size='20'%3E管理学%3C/text%3E%3C/svg%3E" alt="管理学"/>
        <div class="course-info">
          <span class="course-category">专业课</span>
          <h3 class="course-name">管理学原理精讲精练</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>王红副教授</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥259</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>

      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23f3e8ff' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%239c27b0' font-size='20'%3E大学语文%3C/text%3E%3C/svg%3E" alt="大学语文"/>
        <div class="course-info">
          <span class="course-category">公共课</span>
          <h3 class="course-name">专升本大学语文基础班</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>刘芳教授</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥199</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>

      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23e8ffee' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%23008888' font-size='20'%3E会计学%3C/text%3E%3C/svg%3E" alt="会计学"/>
        <div class="course-info">
          <span class="course-category">专业课</span>
          <h3 class="course-name">会计学基础与实务</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>陈强讲师</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥279</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>

      <div class="course-card">
        <img class="course-img" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='180'%3E%3Crect fill='%23fff0e8' width='400' height='180'/%3E%3Ctext x='200' y='90' text-anchor='middle' fill='%23ff9800' font-size='20'%3E计算机%3C/text%3E%3C/svg%3E" alt="计算机"/>
        <div class="course-info">
          <span class="course-category">专业课</span>
          <h3 class="course-name">计算机应用基础速成班</h3>
          <div class="course-teacher">
            <img class="teacher-avatar" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='30' height='30'%3E%3Ccircle fill='%232a6eff' cx='15' cy='15' r='15'/%3E%3C/svg%3E" alt="teacher"/>
            <span>赵敏博士</span>
          </div>
          <div class="course-footer">
            <span class="course-price">¥239</span>
            <button class="course-enroll">立即报名</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 分页 -->
    <div class="pagination">
      <button class="page-btn disabled">上一页</button>
      <button class="page-btn active">1</button>
      <button class="page-btn">2</button>
      <button class="page-btn">3</button>
      <button class="page-btn">下一页</button>
    </div>
  </div>
</template>

<script setup>
</script>