<template>
  <div class="about">
    <h1>Movie Information Page</h1>
    <FindBar :movies="movies"/>
    <MovieList :movies="movies"/>
    
  </div>
</template>


<script>
import axios from 'axios'
// import router from '@/router'
import MovieList from '../components/MovieList'
import FindBar from '../components/FindBar'

export default {
  name: 'About',
  data() {
    return {
      movies: [],
    }
  },
  components:{
    MovieList,
    FindBar,
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