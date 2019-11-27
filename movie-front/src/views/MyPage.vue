<template>
  <div class="my-page">
    <h1>This is your Page. Enjoy your Life!</h1>
    <h1>환영합니다. {{ infos.username }} 님</h1>
    <h2>볼래요한 영화 목록!!</h2>
    <MovieList :movies="movies"/>
    여기는 구분
    <hr>
    <h1>유저들 목록!! 팔로우하려면 버튼 클릭!</h1>
    <span v-for="user in users" :key="user.id" style="margin-right: 20px">
      <button class="btn btn-success" v-on:click="follow(user)">{{ user.username }}</button>
    </span>
    <h2>당신이 팔로우한 사람들</h2>
    <!-- <span v-for="id in following_users">
      users.
    </span> -->

    <!-- <div v-for="user in users" :key="user.id">
      {{ user.username }}
    </div> -->
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '../components/MovieList'
import { mapGetters } from 'vuex'

export default {
  name: 'MyPage',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      infos: [],
      users: [],
      // following_users: [],
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ])
  },
  methods:{
    getMyinfo() {
      // const data = {
      //   user_id: this.userId
      // }
      
      // console.log(this.userId)
      axios.get(`http://127.0.0.1:8000/accounts/${this.userId}/`)
      .then(response => {
        this.infos = response.data
        // console.log(this.infos.potential_movies)
        const temp = this.infos.potential_movies
        for (let index = 0; index < temp.length; index++) {
          axios.get(`http://127.0.0.1:8000/movies/${temp[index]}/`)
          .then(response => {
            this.movies.push(response.data)
          })
        }
        // console.log(this.infos)
        // const following_users_id = this.infos.followers
        // for (let index = 0; index < following_users_id.length; index++) {
          // const data = {
          //   id: following_users_id[index],
          //   name: users[following_users_id[index]]
          // }
        //   this.following_users.push(following_users_id[index])
        // }
        // console.log(this.following_users)
        // // console.log(data)
        // // console.log(this.movies)
        // console.log(this.users)
      })
      .catch(error => {
        console.error(error)
      })
    },
    getUsers() {
      axios.get('http://127.0.0.1:8000/accounts/')
      .then(response => {
        this.users = response.data
        // console.log(this.users)
      })
    },
    follow(user) {
      const SERVER_IP = 'http://127.0.0.1:8000'
      const data = {
        following_id: user.id,
        user: this.userId
      }
      console.log(data)
      axios.post(`${SERVER_IP}/accounts/follow/${data.user}/${data.following_id}/`)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      console.log(this.users[0])
    },
  },
  mounted() {
    this.getUsers(),
    this.getMyinfo()
    
  },
  // watch: {
  //   isLoggedIn() {
  //     this.getMyinfo()
  //     this.getUsers()
  //   }
  // },
}
</script>

<style>

</style>