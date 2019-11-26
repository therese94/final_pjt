<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
// import axios from 'axios'
import { mapGetters } from 'vuex'
import router from '@/router'

export default {
  name: 'home',
  components: {
    HelloWorld
  },
  computed: {
    // getters가 가지고 있는 모든 친구들을 computed 에 쫙 뿌려준다고 생각하면 된다.
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  methods: {
    // 사용자 로그인 유무를 확인하여 로그인되어있지 않을 시 로그인 페이지로 보내겠다.
    checkLoggedIn() {

      // 여기도 이제 필요 없어짐에 따라 지우는 것.
      // 1. 세션을 시작해서
      // this.$session.start()
      // 2. 'jwt' 가 있는지 확인하겠다.
      // if(!this.$session.has('jwt')){

      if(!this.isLoggedIn) {
        // 로그인 페이지로 보내겠다.
        router.push('/login')
      }
    },
    mounted() {
      if (this.isLoggedIn){
        this.checkLoggedIn()
      }
    },
    // watch: {
    //   isLoggedIn() {
    //   }
    // },
  },
}
</script>
