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
