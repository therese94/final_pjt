<template>
  <div class="movie_content w-25 float-left d-block">
    <p><strong> {{ movie.title }} </strong></p>
    <img :src="movie.poster_url" width="110" alt="poster" data-toggle="modal" @click="get_review(movie.id)" :data-target="`#movie_${movie.id}`">
    <br>
    <MovieDetail @get_review="get_review" v-bind:movie="movie" :reviews="reviews"/>
  </div>
</template>

<script>
import MovieDetail from './MovieDetail.vue'
import axios from 'axios'

export default {
  name: 'MovieListItem',
  components: {
    MovieDetail,
  },
  data() {
    return {
      reviews: [],
    }
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  methods: {
    async get_review(movie_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const response = await axios.get(`${SERVER_IP}/movies/review/${movie_id}/`)
      this.reviews = response.data
      console.log(this.reviews)

      for (let index = 0; index < this.reviews.length; index++) {
        const user_id = this.reviews[index]['user']
        const response = await axios.get(`${SERVER_IP}/accounts/${user_id}/`)
        this.reviews[index]['username'] = response.data['username']
      }
      console.log(this.reviews)
    },
  },
}
</script>


<style>
.movie_content { height: 250px; margin-bottom: 20px; }
</style>