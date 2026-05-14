import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import CoursePage from '../views/CoursePage.vue'
import AboutPage from '../views/AboutPage.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import CourseService from '../views/services/CourseService.vue'
import QuizService from '../views/services/QuizService.vue'
import MentorService from '../views/services/MentorService.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/courses', name: 'courses', component: CoursePage },
  { path: '/services/courses', name: 'service-courses', component: CourseService },
  { path: '/services/quiz', name: 'service-quiz', component: QuizService },
  { path: '/services/mentor', name: 'service-mentor', component: MentorService },
  { path: '/about', name: 'about', component: AboutPage },
  { path: '/login', name: 'login', component: LoginPage },
  { path: '/register', name: 'register', component: RegisterPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router