<template>
  <div class="Movie-list">
    <!-- <select class="form-control">
      <option>
      </option>
    </select> -->
    <MovieListItem v-for="movie in movies" v-bind:key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  data() {
    return {
    }
  },
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  // mounted() {
  //   console.log('아래에 출력')
  //   console.log(this.movies)
  // },
}
</script>

<style>
.Movie-list { width: 1200px; overflow: auto; }
.movie_content { width: 300px; height: 480px; margin-top: 15px; padding: 30px 0; border-bottom: 1px solid #ededed; }
.movie_content img { width: 80%; }
</style>