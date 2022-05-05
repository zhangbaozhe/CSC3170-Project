import Vue from 'vue'
import VueRouter from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '../views/Login.vue'
import Course from '../views/Course.vue'
import Home from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import Search from '../views/Search.vue'
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

const whiteList = ["login", "signup"]; // 定义一个白名单列表

router.beforeEach(async (to, from, next) => {
  var isTokenAvailable;
  isTokenAvailable = store.state.hasLogin; // 校验token是否失效
  if (!isTokenAvailable && whiteList.includes(to.path)) { // 如果是访问的白名单中的页面
    return next(); // 不需要校验，直接返回继续访问该页面
  }
  if (isTokenAvailable) { // 如果token未失效
    if(whiteList.includes(to.path)) { // 如果访问的是login页面，则回到首页
      next("/");
    } else { // 如果访问的不是login页面，则继续访问当前要访问的页面
      next();
    }
  } else { // 如果token失效了
    // const needLogin = to.matched.some(item => item.meta.needLogin); // 检测要访问的页面是否需要登录才能访问
    // if(needLogin) { // 如果访问的页面是需要登录的
    //   next("/login"); // 跳转到登录页面
    // } else { // 如果访问的页面是不需要登录的，则直接继续访问
    //   next();
    next("/login");
    // }
  }
});
export default router