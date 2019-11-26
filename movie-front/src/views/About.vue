<template>
  <div class="about">
    <h1>This is an about page</h1>
    <div class="w-25 m-0 mh-50 p-0 float-left d-block" v-for="movie in movies" :key="movie.id">
      <p>영화 제목: {{ movie.title }} </p>
      <img :src="movie.poster_url" width="300" alt="poster">
      <div>관람객 수: {{ movie.audiAcc }}</div>
      <div>영화 설명: {{ movie.description }}</div>
      <div>영화 장르: {{ movie.genres }}</div>
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
      for (let index = 1; index < 1000; index++) {
        axios.get(`http://127.0.0.1:8000/movies/${index}/`)
        .then(response => {
          this.movies.push(response.data)
        })
        .catch(error => {
          console.error(error)
        })
      }
    },
  },
  mounted() {
    this.getMovie()
  },
}

</script>