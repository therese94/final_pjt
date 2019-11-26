<template>
  <div class="about">
    <h1>Movie Information Page</h1>

    <MovieList :movies="movies"/>
    <div class="w-25 m-0 mh-50 p-0 float-left d-block" v-for="movie in movies" :key="movie.id">
      <p>영화 제목: {{ movie.title }} </p>
      <div>관람객 수: {{ movie.audiAcc }}</div>
      <img :src="movie.poster_url" width="200" alt="poster">
      <hr>
      <!-- <div>영화 설명: {{ movie.description }}</div> -->
      <!-- <div>영화 장르: {{ movie.genres }}</div> -->
    </div>
  </div>
</template>


<script>
import axios from 'axios'
// import router from '@/router'

export default {
  name: 'About',
  data() {
    return {
      movies: [],
    }
  },
  methods:{
    getMovie() {
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then(response => {
        this.movies = response.data
        console.log(this.movies)
      })
      .catch(error => {
        console.error(error)
      })
    },  
  },
  mounted() {
    this.getMovie()
  },
}

</script>