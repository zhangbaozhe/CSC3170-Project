import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '../views/Login.vue'
import Course from '../views/Course.vue'
import Home from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import Search from '../views/Search.vue'
import Admin from '../views/Admin.vue'
import store from '../store/store.js'

//Vue.use(Router)
Vue.use(VueRouter)
const routes=[

  {
    path: '/',
    name: 'HelloWorld',
    component: HelloWorld
  },
  {
    path: '/admin', 
    name: 'Admin', 
    component: Admin
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
  // {
  //   path: '/course/:id', 
  //   name: 'Course', 
  //   component: Course
  // },
  {
    path: '/Search', 
    name: 'Search', 
    component: Search
  },

]
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

const whiteList = ["/login", "/signup"]; // 定义一个白名单列表

router.beforeEach(async (to, from, next) => {
  var isTokenAvailable;
  isTokenAvailable = store.state.hasLogin; // 校验token是否失效
  console.log(to.path)
  if(to.path == "/admin" && store.state.userName != "CSC3170"){
    return next("/login")
  }
  if (!isTokenAvailable && !whiteList.includes(to.path)) { // 如果是访问的白名单中的页面
    return next("/login"); // 不需要校验，直接返回继续访问该页面
  }
  else {
    return next()
  }
});
export default router