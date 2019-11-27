import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  // 상태 (data)
  state: {
    token: null,
  },
  // same with computed
  getters: {
    isLoggedIn(state) {
      return state.token ? true : false
    },
    options(state) {
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state) {
      // 토큰이 있다면 해석해서 return하고 없다면 null을 리턴해라.
      return state.token ? jwtDecode(state.token).user_id : null
    },
  },
  // 상태를 변경하는 함수
  // state만 변경하고 어떤 다른 행동도 하지 않는다.
  mutations: {
    setToken(state, token) {
      state.token = token
      // 상태를 정의했고 변경하는 함수를 만들었다.
    }
  },
  // method
  actions: {
    login(context, token) {
      context.commit('setToken', token)
      // login을 하게 되면 이 것을 실행해주겠다. 라는 뜻.
    },
    logout(context) {
      context.commit('setToken', null)
    }
  },
})
