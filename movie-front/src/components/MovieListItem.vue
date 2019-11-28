<template>
  <div class="movie_content w-25 float-left d-block">
    <p class="movie-title"> {{ movie.title }} </p>
    <img :src="movie.poster_url" alt="poster" data-toggle="modal" @click="get_review(movie.id)" :data-target="`#movie_${movie.id}`">
    <br>
    <div class="detail-txt-Wrap">
      <span class="genre-txt"> {{ movie.genres }} </span>
      <span class="rating-txt"> {{ movie.audiRating }} </span>
    </div>
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
.movie_content { height: 280px; margin-bottom: 20px; padding-bottom: 50px; }
.movie-title { font-size: 20px; font-weight: bolder; }
.detail-txt-Wrap {margin-top: 20px; text-align: left; padding: 0 30px; }
.genre-txt, .rating-txt { border-radius: 20px; margin-top: 5px; text-align: center; font-weight: bold; color: #fff; }
.genre-txt { padding: 5px 5px 5px 8px; background-color: #666; margin-right: 15px; }
.rating-txt { padding: 5px 8px; border: 1px solid #282118; color: #282118; box-sizing: border-box; }
</style>