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
.movie_content { width: 290px; height: 500px; margin-top: 15px; padding: 30px 0;  }
.movie_content img { width: 240px; overflow: hidden; }
</style>