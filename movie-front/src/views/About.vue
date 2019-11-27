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
// import MyPage from '../components/MyPage'

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
    // MyPage,
  },
  methods:{
    getMovie() {
      axios.get(`http://127.0.0.1:8000/movies/`)
      .then(response => {
        this.movies = response.data
        for (let index = 0; index < this.movies.length; index++) {
          this.movies[index]['id'] = index
        }
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

<style>
.about { width: 1200px; margin: 0 auto; }
.mooving_gif { width: 250px; height: 250px; }
</style>