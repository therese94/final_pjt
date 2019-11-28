<template>
  <div class="Movie-list">
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
}
</script>

<style>
.Movie-list { width: 1200px; overflow: auto; }
.movie_content { width: 300px; height: 480px; margin-top: 15px; padding: 30px 0; border-bottom: 1px solid #ededed; }
.movie_content img { width: 240px; height: 340px; overflow: hidden; }
</style>