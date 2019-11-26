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
.movie_content { height: 250px; margin-bottom: 20px; }

</style>