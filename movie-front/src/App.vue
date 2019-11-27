<template>
  <div id="app">
    <div id="nav">
      <router-link to="/" class="main_logo"><h1><img alt="Vue logo" src="./assets/main/main_logo.png"></h1></router-link>
      <div class="nav_wrap">
        <router-link to="/" class="nav_menu">HOME</router-link>
        <router-link to="/about" class="nav_menu">MOVIE</router-link>
        <span v-if="isLoggedIn">
          <router-link to="/mypage" class="nav_menu">MY PAGE</router-link>
          <a @click.prevent="logout" href="/logout" class="nav_menu">LOGOUT</a>
        </span>
        <span v-else>
          <router-link to="/login" class="nav_menu">LOGIN</router-link>
          <a href="http://127.0.0.1:8000/accounts/signup/" class="nav_menu">SIGNUP</a>
        </span>
       </div> 
    </div>
    <router-view/>
  </div>
</template>


<script src="./assets/js/jquery-1.12.0.min.js"></script>
<script src="./assets/js/jquery.flexslider-min.js"></script>
<script src="./assets/js/swiper.min.js"></script>
<script src="./assets/js/slick.min.js"></script>
<script src="./assets/js/jquery.flowslider.js"></script>
<script src="./assets/js/common.js"></script>
<script src="./assets/js/main.js"></script>
<script>
import router from '@/router'

export default {
  name: 'App',

  computed: {
    isLoggedIn() {
      return this.$store.getters.isLoggedIn
    }
  },
  // 최상위 App 컴포넌트가 렌더링 되면 실행하는 함수
  mounted() {
    if(this.$session.has('jwt')) {
      const token = this.$session.get('jwt')
      this.$store.dispatch('login', token)
    }
  },
  methods: {
    logout() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('/login')
    }
  },
}

</script>


<style>
.main_logo { display: block; float: left; width: 300px; height: 100px; }
#app {
  width: 1600px; margin: 0 auto;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.nav_wrap { width: 720px; height:100px; display: block; float: right; font-size: 25px;  }

#nav {
  
  width: 1200px;
  height: 100px;
  margin: 0 auto;
  margin-bottom: 25px;
}

.nav_menu { width: 180px; height: 100px; line-height: 100px; position: center; display: block; float:left; }

#nav a {
  font-weight: thin; color: #353029;
}

/*  .nav_menu:hover { background-color: #fce583; text-decoration: none; font-weight: bold; } */

#nav a.router-link-exact-active {
  /* color: #42b983; */
  
}
</style>
