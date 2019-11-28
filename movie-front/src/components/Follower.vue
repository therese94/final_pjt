<template>
  <div>
    <p><strong> {{ follower.username }} 이 재밌게 본 영화! </strong></p>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import MovieList from '../components/MovieList'
import axios from 'axios'

export default {
  name: 'Follower',
  components: {
    MovieList,
  },
  data() {
    return {
      movies_id: [],
      movies: [],
    }
  },
  props: {
    follower: {
      type: Object,
      required: true,
    }
  },
  methods: {
    follower_movie() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const reviews = this.follower.reviews
      
      if (reviews.length >= 1) {
        reviews.forEach(element => {
          axios.get(`${SERVER_IP}/movies/review_detail/${element}/`)
            .then(response => {
              if (response.data['score'] >= 0) {
                axios.get(`${SERVER_IP}/movies/${response.data['movie']}/`)
                  .then(response => {
                    this.movies.push(response.data)
                  })
                  .catch(error => {
                    console.log(error)
                  })
                }
          });
        });
      }
    }
  },
  mounted() {
    this.follower_movie()
  },
}
</script>


<style>
.movie_content { height: 250px; margin-bottom: 20px; }
</style>