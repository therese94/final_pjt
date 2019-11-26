<template>
  <div id="app">
    <div id="nav">
      <h1>JUNE'S MOVIE</h1>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <span v-if="isLoggedIn">
        <a @click.prevent="logout" href="/logout">Logout</a> |
      </span>
      <span v-else>
        <router-link to="/login">Login</router-link> |
        <a href="http://127.0.0.1:8000/accounts/signup/">Signup</a>
      </span>
    </div>
    <router-view/>
  </div>
</template>

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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
