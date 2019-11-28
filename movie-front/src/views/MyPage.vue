<template>
  <div class="my-page">
    <div class="mypage_con01">

      <div class="level_img" v-if="movies.length < 5">
        <img src="../assets/main/level01.png" alt="레벨 이미지">
      </div>
      <div class="level_img" v-else-if="movies.length < 10">
        <img src="../assets/main/level02.png" alt="레벨 이미지">
      </div>
      <div class="level_img" v-else-if="movies.length < 15">
        <img src="../assets/main/level03.png" alt="레벨 이미지">
      </div>
      <div class="level_img" v-else-if="movies.length < 30">
        <img src="../assets/main/level11.png" alt="레벨 이미지">
      </div>
      <p class="mypage_title"> {{ infos.username }}님의 MY PAGE</p>
      
    </div>
    

    <h2>볼래요한 영화</h2>
    <MovieList :movies="movies"/>
    <hr>
    <h1>유저들 목록!! 팔로우하려면 버튼 클릭!</h1>
    <span v-for="user in users" :key="user.id" style="margin-right: 20px">
      <button class="btn btn-success" v-on:click="follow(user)">{{ user.username }}</button>
    </span>
    <h2>당신이 팔로우한 사람들이 볼래요한 영화를 보려면 클릭!</h2>
    <FollowersList :following_users="following_users"/>
  </div>
</template>
<script>
import axios from 'axios'
import MovieList from '../components/MovieList'
import FollowersList from '../components/FollowersList'
import { mapGetters } from 'vuex'

export default {
  name: 'MyPage',
  components: {
    MovieList,
    FollowersList,
  },
  data() {
    return {
      movies: [],
      infos: [],
      users: [],
      following_users: [],
      temp: [],
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ])
  },
  methods:{
    getMyinfo() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/accounts/${this.userId}/`)
      .then(response => {
        this.infos = response.data
        // console.log(this.infos.potential_movies)
        const temp = this.infos.potential_movies
        for (let index = 0; index < temp.length; index++) {
          axios.get(`${SERVER_IP}/movies/${temp[index]}/`)
          .then(response => {
            this.movies.push(response.data)
          })
        }

        axios.get(`${SERVER_IP}/accounts/${this.userId}/`)
        .then(response => {
          const id_list = response.data.followers
          const temp = []
          for (let index = 0; index < id_list.length; index++) {
            var user_id = id_list[index]
            axios.get(`${SERVER_IP}/accounts/${user_id}/`)
              .then(response => {
                temp.push(response.data)
            })
          }
          this.following_users = temp
          console.log(this.following_users)
        })
      })
      .catch(error => {
        console.error(error)
      })
    },
    getUsers() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/accounts/`)
      .then(response => {
        this.users = response.data
      })
    },
    follow(user) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const data = {
        following_id: user.id,
        user: this.userId
      }
      axios.post(`${SERVER_IP}/accounts/follow/${data.user}/${data.following_id}/`)
      
      axios.get(`${SERVER_IP}/accounts/${data.user}/`)
        .then(response => {
          const id_list = response.data.followers
          const temp = []
          for (let index = 0; index < id_list.length; index++) {
            var user_id = id_list[index]
            axios.get(`${SERVER_IP}/accounts/${user_id}/`)
              .then(response => {
                temp.push(response.data)
            })
          }
          this.following_users = temp
          console.log(this.following_users)
        })
    },
  },
  mounted() {
    this.getUsers(),
    this.getMyinfo()
  },

}
</script>

<style>
  .my-page { width: 1200px; margin: 0 auto; }

  .mypage_con01{ width: 400px; height: 400px; padding: 40px 0; margin: 0 auto; margin-top: 80px; border: 1.5px solid #282118; margin-bottom: 50px; border-radius: 10px; }
  .mypage_title { font-size: 24px; color: #282118; font-weight: bolder; margin-top: 30px; margin-bottom: 50px; }
  .level_img { width: 250px; height: 250px; margin: 0 auto; }
  .level_img img { width: 250px; height: 250px; }

  .my-page h2 { font-size: 24px; color: #282118; font-weight: bold;  }
</style>