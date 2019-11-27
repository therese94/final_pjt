<template>
  <div class="about">
    <h1>Movie Information Page</h1>
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