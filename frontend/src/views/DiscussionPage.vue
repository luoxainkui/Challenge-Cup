<template>
  <div class="discussion-page">
    <!-- Hero -->
    <section class="discussion-hero">
      <h1>刷题 & 资源讨论专区</h1>
      <p>和万千备考同学一起交流，分享经验与资源</p>
    </section>

    <!-- 板块导航 -->
    <section class="board-nav-section">
      <div class="board-grid">
        <button
          v-for="cat in BOARD_CATEGORIES"
          :key="cat.id"
          class="board-card"
          :class="{ active: currentBoard === cat.id }"
          :style="{ '--board-color': cat.color }"
          @click="selectBoard(cat.id)"
        >
          <span class="board-card-icon">{{ cat.icon }}</span>
          <span class="board-card-name">{{ cat.name }}</span>
          <span class="board-card-desc">{{ cat.desc }}</span>
        </button>
      </div>
    </section>

    <!-- 发帖按钮 -->
    <div class="discussion-toolbar" v-if="currentBoard !== 'all'">
      <div class="toolbar-info">
        <span class="toolbar-board-label">{{ currentBoardLabel }}</span>
        <span class="toolbar-post-count">{{ filteredPosts.length }} 个帖子</span>
      </div>
      <button class="post-btn" @click="showEditor = true">✏️ 发布新帖</button>
    </div>

    <!-- 帖子列表 -->
    <section class="post-list-section">
      <div class="post-list">
        <article
          v-for="post in filteredPosts"
          :key="post.id"
          class="post-item"
          :class="{ pinned: post.pinned }"
          @click="openPost(post)"
        >
          <div class="post-header">
            <span class="post-pin" v-if="post.pinned">📌 置顶</span>
            <h3 class="post-title">{{ post.title }}</h3>
          </div>
          <div class="post-meta">
            <span class="post-author-avatar" :style="{ background: post.author.color }">{{ post.author.avatar }}</span>
            <span class="post-author-name">{{ post.author.name }}</span>
            <span class="post-date">{{ post.createdAt }}</span>
            <span class="post-tags" v-if="post.tags?.length">
              <span v-for="tag in post.tags" :key="tag" class="post-tag">{{ tag }}</span>
            </span>
          </div>
          <div class="post-stats">
            <span class="post-stat">💬 {{ post.replyCount }}</span>
            <span class="post-stat">👀 {{ post.viewCount }}</span>
          </div>
        </article>
      </div>
      <div class="empty-state" v-if="filteredPosts.length === 0">
        <p>该板块暂无帖子，快来发表第一篇吧</p>
      </div>
    </section>

    <!-- 帖子详情弹层 -->
    <div class="post-overlay" v-if="activePost" @click.self="activePost = null">
      <div class="post-detail-panel">
        <button class="close-btn" @click="activePost = null">✕</button>
        <div class="post-detail-header">
          <span class="post-pin" v-if="activePost.pinned">📌 置顶</span>
          <h2>{{ activePost.title }}</h2>
          <div class="post-detail-meta">
            <span class="post-author-avatar" :style="{ background: activePost.author.color }">{{ activePost.author.avatar }}</span>
            <span>{{ activePost.author.name }}</span>
            <span>·</span>
            <span>{{ activePost.createdAt }}</span>
            <span>·</span>
            <span>💬 {{ activePost.replyCount }} 回复</span>
            <span>👀 {{ activePost.viewCount }} 浏览</span>
          </div>
          <div class="post-detail-tags" v-if="activePost.tags?.length">
            <span v-for="tag in activePost.tags" :key="tag" class="post-tag">{{ tag }}</span>
          </div>
        </div>
        <div class="post-detail-content">
          <p v-for="(line, i) in activePost.content.split('\n')" :key="i">{{ line }}</p>
        </div>

        <!-- 楼层回复 -->
        <div class="post-replies">
          <h3 class="reply-section-title">全部回复（{{ postReplies.length }}）</h3>
          <div v-if="postReplies.length === 0" class="reply-empty">
            <p>暂无回复，抢个沙发吧</p>
          </div>
          <div v-for="reply in postReplies" :key="reply.id" class="reply-item">
            <div class="reply-header">
              <span class="reply-avatar" :style="{ background: reply.author.color }">{{ reply.author.avatar }}</span>
              <span class="reply-author">{{ reply.author.name }}</span>
              <span class="reply-floor">#{{ reply.floor }}楼</span>
              <span class="reply-date">{{ reply.createdAt }}</span>
            </div>
            <div class="reply-content">
              <p v-for="(line, i) in reply.content.split('\n')" :key="i">{{ line }}</p>
            </div>
            <div class="reply-footer">
              <button class="reply-like-btn">👍 {{ reply.likes }}</button>
              <button class="reply-quote-btn">💬 回复</button>
            </div>
          </div>
        </div>

        <!-- 快速回复 -->
        <div class="quick-reply">
          <textarea
            v-model="replyText"
            class="quick-reply-input"
            placeholder="写下你的回复..."
            rows="3"
          ></textarea>
          <button class="quick-reply-submit" :disabled="!replyText.trim()">发表回复</button>
        </div>
      </div>
    </div>

    <!-- 发帖编辑器 -->
    <div class="post-overlay" v-if="showEditor" @click.self="showEditor = false">
      <div class="post-detail-panel editor-panel">
        <button class="close-btn" @click="showEditor = false">✕</button>
        <h2 class="editor-title">发布新帖</h2>
        <div class="editor-field">
          <label>选择板块</label>
          <select v-model="newPost.board" class="editor-select">
            <option v-for="cat in BOARD_CATEGORIES" :key="cat.id" :value="cat.id">{{ cat.icon }} {{ cat.name }}</option>
          </select>
        </div>
        <div class="editor-field">
          <label>标题</label>
          <input v-model="newPost.title" class="editor-input" placeholder="请输入帖子标题" />
        </div>
        <div class="editor-field">
          <label>内容</label>
          <textarea v-model="newPost.content" class="editor-textarea" rows="8" placeholder="请输入帖子内容，支持换行"></textarea>
        </div>
        <div class="editor-actions">
          <button class="editor-cancel" @click="showEditor = false">取消</button>
          <button class="editor-submit" :disabled="!canPublish" @click="handlePublish">发布</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { BOARD_CATEGORIES, MOCK_POSTS, MOCK_REPLIES } from '@/constants/discussion'

const currentBoard = ref('all')
const activePost = ref(null)
const showEditor = ref(false)
const replyText = ref('')
const newPost = ref({ board: 'quantao', title: '', content: '' })

const filteredPosts = computed(() => {
  if (currentBoard.value === 'all') return MOCK_POSTS
  return MOCK_POSTS.filter(p => p.board === currentBoard.value)
})

const currentBoardLabel = computed(() => {
  if (currentBoard.value === 'all') return '全部板块'
  const cat = BOARD_CATEGORIES.find(c => c.id === currentBoard.value)
  return cat ? `${cat.icon} ${cat.name}` : ''
})

const postReplies = computed(() => {
  if (!activePost.value) return []
  return MOCK_REPLIES.filter(r => r.postId === activePost.value.id)
})

const canPublish = computed(() => newPost.value.title.trim() && newPost.value.content.trim())

function selectBoard(id) {
  currentBoard.value = id
  activePost.value = null
}

function openPost(post) {
  activePost.value = post
  replyText.value = ''
}

function handlePublish() {
  if (!canPublish.value) return
  // 预留后端对接位：emit 或 API 调用
  console.log('发布帖子:', newPost.value)
  showEditor.value = false
  newPost.value = { board: 'quantao', title: '', content: '' }
}
</script>

<style lang="scss" scoped>
.discussion-page {
  min-height: 100vh;
  background: #f8f9fb;
}

.discussion-hero {
  padding: 100px 0 32px;
  text-align: center;
  background: $color-gradient-primary;
  color: #fff;

  h1 { font-size: $font-size-4xl; font-weight: $font-weight-bold; margin-bottom: 8px; }
  p { opacity: 0.85; font-size: $font-size-md; }
}

// 板块导航
.board-nav-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 32px 20px 8px;
}

.board-grid {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 16px;
}

.board-card {
  padding: 18px 12px;
  border: 2px solid #eee;
  border-radius: $radius-xl;
  background: #fff;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
  transition: all $transition-fast;

  &:hover, &.active {
    border-color: var(--board-color);
    background: color-mix(in srgb, var(--board-color) 5%, #fff);
    transform: translateY(-2px);
  }
}

.board-card-icon { font-size: 28px; }
.board-card-name { font-size: $font-size-sm; font-weight: $font-weight-semibold; color: $color-text-primary; }
.board-card-desc { font-size: $font-size-xs; color: $color-text-light; }

// 工具栏
.discussion-toolbar {
  max-width: $max-width;
  margin: 0 auto;
  padding: 20px 20px 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.toolbar-board-label { font-size: $font-size-lg; font-weight: $font-weight-bold; color: $color-text-primary; }
.toolbar-post-count { font-size: $font-size-sm; color: $color-text-muted; margin-left: 12px; }

.post-btn {
  padding: 10px 24px;
  background: $color-primary;
  color: #fff;
  border: none;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  cursor: pointer;
  transition: background $transition-fast;
  &:hover { background: $color-primary-dark; }
}

// 帖子列表
.post-list-section {
  max-width: $max-width;
  margin: 0 auto;
  padding: 16px 20px 60px;
}

.post-list { display: flex; flex-direction: column; gap: 12px; }

.post-item {
  background: #fff;
  border-radius: $radius-xl;
  padding: 20px 24px;
  box-shadow: $shadow-sm;
  cursor: pointer;
  transition: all $transition-fast;

  &:hover { box-shadow: $shadow-md; transform: translateY(-1px); }
  &.pinned { border-left: 4px solid $color-warning; }
}

.post-header { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }

.post-pin {
  font-size: $font-size-xs;
  color: $color-warning;
  font-weight: $font-weight-semibold;
  background: #fff3e0;
  padding: 2px 8px;
  border-radius: $radius-sm;
  white-space: nowrap;
}

.post-title { font-size: $font-size-md; font-weight: $font-weight-semibold; color: $color-text-primary; flex: 1; }

.post-meta {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 10px;
}

.post-author-avatar {
  width: 26px; height: 26px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff;
  font-size: $font-size-xs;
  font-weight: $font-weight-bold;
}

.post-author-name { font-size: $font-size-sm; color: $color-text-secondary; }
.post-date { font-size: $font-size-xs; color: $color-text-light; }

.post-tags { display: flex; gap: 6px; margin-left: auto; }
.post-tag {
  padding: 2px 10px;
  background: $color-primary-light;
  color: $color-primary;
  font-size: $font-size-xs;
  border-radius: $radius-full;
}

.post-stats { display: flex; gap: 16px; }
.post-stat { font-size: $font-size-sm; color: $color-text-muted; }

// 弹层
.post-overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,0.5);
  z-index: 100;
  overflow-y: auto;
  padding: 20px;
}

.post-detail-panel {
  max-width: 800px;
  margin: 40px auto;
  background: #fff;
  border-radius: $radius-2xl;
  padding: 40px;
  position: relative;
}

.editor-panel { padding: 32px; }

.close-btn {
  position: absolute; top: 16px; right: 20px; z-index: 20;
  width: 36px; height: 36px;
  border-radius: 50%; border: none;
  background: rgba(0,0,0,0.4); color: #fff; font-size: 18px;
  cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  &:hover { background: rgba(0,0,0,0.6); }
}

.post-detail-header {
  margin-bottom: 24px;
  h2 { font-size: $font-size-2xl; font-weight: $font-weight-bold; color: $color-text-primary; margin: 8px 0 12px; }
}

.post-detail-meta {
  display: flex; align-items: center; gap: 8px;
  font-size: $font-size-sm; color: $color-text-muted;
}

.post-detail-tags { margin-top: 10px; display: flex; gap: 6px; }

.post-detail-content {
  padding: 20px;
  background: $color-bg-page;
  border-radius: $radius-lg;
  line-height: 1.8;
  color: $color-text-body;
  font-size: $font-size-base;
  margin-bottom: 32px;
  white-space: pre-wrap;
}

// 回复
.post-replies { margin-bottom: 20px; }

.reply-section-title {
  font-size: $font-size-md; font-weight: $font-weight-semibold;
  color: $color-text-primary; margin-bottom: 16px;
  padding-bottom: 10px; border-bottom: 1px solid #eee;
}

.reply-empty { text-align: center; padding: 30px; color: $color-text-muted; }

.reply-item {
  padding: 16px 0;
  border-bottom: 1px solid #f0f0f0;
  &:last-child { border-bottom: none; }
}

.reply-header { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.reply-avatar {
  width: 28px; height: 28px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: $font-size-xs; font-weight: $font-weight-bold;
}
.reply-author { font-size: $font-size-sm; font-weight: $font-weight-medium; color: $color-text-secondary; }
.reply-floor { font-size: $font-size-xs; color: $color-primary; font-weight: $font-weight-semibold; }
.reply-date { font-size: $font-size-xs; color: $color-text-light; margin-left: auto; }

.reply-content {
  padding-left: 36px;
  font-size: $font-size-base;
  color: $color-text-body;
  line-height: 1.7;
  white-space: pre-wrap;
}

.reply-footer {
  padding-left: 36px;
  margin-top: 8px;
  display: flex; gap: 12px;
}

.reply-like-btn, .reply-quote-btn {
  padding: 3px 12px;
  border: 1px solid #e0e4ea;
  background: #fff;
  border-radius: $radius-full;
  font-size: $font-size-xs;
  color: $color-text-muted;
  cursor: pointer;
  &:hover { border-color: $color-primary; color: $color-primary; }
}

// 快速回复
.quick-reply { margin-top: 24px; }
.quick-reply-input {
  width: 100%;
  padding: 12px;
  border: 1.5px solid #e0e4ea;
  border-radius: $radius-lg;
  font-size: $font-size-sm;
  resize: vertical;
  outline: none;
  &:focus { border-color: $color-primary; }
}
.quick-reply-submit {
  margin-top: 10px;
  padding: 8px 24px;
  background: $color-primary;
  color: #fff;
  border: none;
  border-radius: $radius-full;
  font-size: $font-size-sm;
  cursor: pointer;
  &:disabled { opacity: 0.5; cursor: not-allowed; }
  &:not(:disabled):hover { background: $color-primary-dark; }
}

// 编辑器
.editor-title { font-size: $font-size-xl; font-weight: $font-weight-bold; margin-bottom: 20px; }
.editor-field { margin-bottom: 16px; }
.editor-field label { display: block; font-size: $font-size-sm; font-weight: $font-weight-medium; color: $color-text-secondary; margin-bottom: 6px; }
.editor-select, .editor-input {
  width: 100%;
  padding: 10px 14px;
  border: 1.5px solid #e0e4ea;
  border-radius: $radius-lg;
  font-size: $font-size-sm;
  outline: none;
  &:focus { border-color: $color-primary; }
}
.editor-textarea {
  width: 100%;
  padding: 12px 14px;
  border: 1.5px solid #e0e4ea;
  border-radius: $radius-lg;
  font-size: $font-size-sm;
  resize: vertical;
  outline: none;
  &:focus { border-color: $color-primary; }
}
.editor-actions { display: flex; justify-content: flex-end; gap: 12px; margin-top: 16px; }
.editor-cancel {
  padding: 8px 20px;
  border: 1.5px solid #e0e4ea; background: #fff;
  border-radius: $radius-full; font-size: $font-size-sm; cursor: pointer;
}
.editor-submit {
  padding: 8px 24px;
  background: $color-primary; color: #fff; border: none;
  border-radius: $radius-full; font-size: $font-size-sm; cursor: pointer;
  &:disabled { opacity: 0.5; cursor: not-allowed; }
  &:not(:disabled):hover { background: $color-primary-dark; }
}

.empty-state { text-align: center; padding: 60px; color: $color-text-muted; }

@include respond-to('tablet') {
  .board-grid { grid-template-columns: repeat(3, 1fr); }
  .post-detail-panel { margin: 20px; padding: 24px; }
}

@include respond-to('mobile') {
  .board-grid { grid-template-columns: repeat(2, 1fr); }
  .discussion-toolbar { flex-direction: column; gap: 12px; align-items: flex-start; }
}
</style>