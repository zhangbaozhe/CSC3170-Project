import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '../views/Login.vue'
import Course from '../views/Course.vue'
import Home from '../views/search.vue'
import SignUp from '../views/SignUp.vue'
import search from '../views/search.vue'

//Vue.use(Router)
Vue.use(VueRouter)
const routes=[

  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/login',
    name: 'Lgoin',
    component: Login
  },
  {
    path: '/course/:id',
    name: 'Course',
    component: Course
  },
  {
    path: '/home',
    name: 'Home',
    component:Home
  }, 
  {
    path: '/signup', 
    name: 'SignUp', 
    component: SignUp
  },
  {
    path: '/course/:id', 
    name: 'Course', 
    component: Course
  },
  {
    path: '/search', 
    name: 'search', 
    component: search
  },

]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
export default router