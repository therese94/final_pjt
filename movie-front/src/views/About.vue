<template>
  <div class="about">
    <h1>This is an about page</h1>
    <!-- <div class="card mb-3" v-for="movie in movies" :key="movie.id"> -->
      포문 나오는지 확인!!
      <p>영화 제목: {{ movies.title }} </p>
      <p>url: {{ movies.poster_url }}</p>
      <!-- <img src={{ movies.poster_url }} alt="movie_img"> -->
      <img :src="movies.poster_url" alt="youtube-thumbnail">
      <div>관람객 수: {{ movies.audience }}</div>
      <div>영화 설명: {{ movies.description }}</div>
    <!-- </div> -->
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
      axios.get('http://127.0.0.1:8000/movies/1/')
      .then(response => {
        this.movies = response.data
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