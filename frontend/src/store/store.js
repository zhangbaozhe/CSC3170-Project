import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const state = {
  userID: -1,
  userName:"",

  hasLogin: false,
}

const mutations = {
    loginUpdate (state) {
        state.hasLogin = true
  },
    logoutUpdate (state) {
        state.hasLogin = false
  },
    userIDUpdate(state, id){
        state.userID = id
  },
    userNameUpdate (state, userName){
        state.userName = userName
  },

}

const actions = {
	
}

export default new Vuex.Store({
	state,
	actions,
	mutations,
  plugins: [createPersistedState()]
})



