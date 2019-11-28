<template>
  <div v-if="following_users != []">
    <div v-for="user in following_users" :key="user.id">
      <button v-on:click="get_follower_info(user.id)">{{ user.username }}</button>
    </div>
    <div v-if="show_on == true">
      <MovieList :movies="movies"/>
    </div>
  </div>
</template>

<script>
import MovieList from '../components/MovieList'
import axios from 'axios'

export default {
  name: 'FollowersList',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      show_on: false,
    }
  },
  props: {
    following_users: {
      type: Array,
      required: false,
    }
  },
  methods: {
    get_follower_info(user_id){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/accounts/${user_id}/`)
      .then(response => {
        var temp = []
        const movie_ids = response.data.potential_movies
        console.log(movie_ids)
        for (let index = 0; index < movie_ids.length; index++) {
          axios.get(`${SERVER_IP}/movies/${movie_ids[index]}/`)
          .then(response => {
            temp.push(response.data)
          })
        }
        this.show_on = true
        this.movies = temp
      })
    },
    // mounted() {
    //   this.get_followers_info()
    // },
  },
  
}
</script>

<style>

</style>