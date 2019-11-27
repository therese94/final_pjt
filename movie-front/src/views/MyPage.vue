<template>
  <div class="my-page">
    <h1>This is your Page. Enjoy your Life!</h1>
    <h2>환영합니다. {{ infos.username }} 님</h2>
    <MovieList :movies="movies"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '../components/MovieList'

export default {
  name: 'MyPage',
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      infos: [],
    }
  },
  methods:{
    getMyinfo() {
      axios.get(`http://127.0.0.1:8000/accounts/2/`)
      .then(response => {
        this.infos = response.data
        console.log(this.infos.potential_movies)
        const temp = this.infos.potential_movies
        for (let index = 0; index < temp.length; index++) {
          axios.get(`http://127.0.0.1:8000/movies/${temp[index]}/`)
          .then(response => {
            this.movies.push(response.data)
          })
        }
        console.log(this.movies)
      })
      .catch(error => {
        console.error(error)
      })
    },  
  },
  mounted() {
    this.getMyinfo()
  },
}
</script>

<style>

</style>