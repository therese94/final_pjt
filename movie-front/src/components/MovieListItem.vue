<template>
  <div class="movie_content w-25 float-left d-block">
    <p><strong> {{ movie.title }} </strong></p>
    <!-- <div>관람객 수: {{ movie.audiAcc }}</div> -->
    <img :src="movie.poster_url" width="110" alt="poster" data-toggle="modal" :data-target="`#movie_${movie.id}`">
    <!-- <div>영화 설명: {{ movie.description }}</div> -->
    <!-- <div>영화 장르: {{ movie.genres }}</div> -->
    <br>
    <!-- {{ movie.id }}출력 -->
    <!-- <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie_${movie.id}`">영화 정보 상세보기</button> -->
    <MovieDetail v-bind:movie="movie"/>
  </div>
</template>

<script>
import MovieDetail from './MovieDetail.vue'

export default {
  name: 'MovieListItem',
  components: {
    MovieDetail,
  },
  data() {
    return {
    }
  },
  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  // mounted() {
  //   console.log('아래에 출력2')
  //   console.log(this.movie)
  // },
}
</script>


<style>
.movie_content { height: 250px; margin-bottom: 20px; }
</style>