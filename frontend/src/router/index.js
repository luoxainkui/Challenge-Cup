import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import CoursesPage from '../views/CoursesPage.vue'
import AboutPage from '../views/AboutPage.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import CourseService from '../views/services/CourseService.vue'
import QuizService from '../views/services/QuizService.vue'
import QuizPracticePage from '../views/QuizPracticePage.vue'
import QuizChapterPage from '../views/quiz/QuizChapterPage.vue'
import QuizMockPage from '../views/quiz/QuizMockPage.vue'
import QuizRealPage from '../views/quiz/QuizRealPage.vue'
import QuizMistakePage from '../views/quiz/QuizMistakePage.vue'
import MentorService from '../views/services/MentorService.vue'
import ConsultationPage from '../views/ConsultationPage.vue'

const routes = [
  { path: '/', name: 'home', component: HomePage },
  { path: '/courses', name: 'courses', component: CoursesPage },
  { path: '/services/courses', name: 'service-courses', component: CourseService },
  { path: '/services/quiz', name: 'service-quiz', component: QuizService },
  { path: '/quiz/practice', name: 'quiz-practice', component: QuizPracticePage },
  { path: '/quiz/chapter', name: 'quiz-chapter', component: QuizChapterPage },
  { path: '/quiz/mock', name: 'quiz-mock', component: QuizMockPage },
  { path: '/quiz/real', name: 'quiz-real', component: QuizRealPage },
  { path: '/quiz/mistake', name: 'quiz-mistake', component: QuizMistakePage },
  { path: '/services/mentor', name: 'service-mentor', component: MentorService },
  { path: '/consultation', name: 'consultation', component: ConsultationPage },
  { path: '/about', name: 'about', component: AboutPage },
  { path: '/login', name: 'login', component: LoginPage },
  { path: '/register', name: 'register', component: RegisterPage },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router