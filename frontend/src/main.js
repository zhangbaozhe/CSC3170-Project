import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Axios from 'axios'

import store from './store/store.js'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';

Vue.use(ElementUI);

Vue.prototype.$axios = Axios;
Vue.config.productionTip = false
Vue.use(Vuex)
new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')

const whiteList = ["/login", "/signup"];

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