<template>
  <div class="about">
    <h2><img alt="mooving" class="mooving_gif" src="../assets/main/mooving_animation.gif"></h2>
    <FindBar :movies="movies"/>
    <MovieList :movies="movies"/>
    <!-- <MyPage :movies="movies"/> -->
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

<style>
.about { width: 1200px; margin: 0 auto; }
.mooving_gif { width: 250px; height: 250px; }
</style>