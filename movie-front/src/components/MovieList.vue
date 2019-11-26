<template>
  <div class="todo-list">
    <div class="w-25 m-0 mh-50 p-0 float-left d-block" v-for="movie in movies" :key="movie.id">
      <p>영화 제목: {{ movie.title }} </p>
      <!-- <div>관람객 수: {{ movie.audiAcc }}</div> -->
      <img :src="movie.poster_url" width="200" alt="poster">
      <hr>
      <!-- <div>영화 설명: {{ movie.description }}</div> -->
      <!-- <div>영화 장르: {{ movie.genres }}</div> -->
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieList',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  }
}
</script>

<style>

</style>