<template>
  <div class="todo-input">
    <form class="input-group mb-3 search-bar" @submit.prevent="onSubmit">
      <input v-model="title" type="text" class="form-control">
      <button type="submit" class="btn btn-success">검색</button>
    </form>
    <div class="search-result" v-if="show_on == true">
      <h3>영화를 찾았어요!</h3>
      <p>제목: {{ movie.title }}</p>
      <div>관람객 수: {{ movie.audiAcc }}</div>
      <img :src="movie.poster_url" width="200" alt="poster">
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FindBar',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  data(){
    return {
      title: '',
      movie: '',
      show_on: false
    }
  },
  methods: {
    onSubmit() {
      this.movies.forEach(temp_movie => {
        if (temp_movie.title.includes(this.title) === true) {
          return this.movie = temp_movie
        }
      });
      this.title = ''
      this.show_on = true
    // is_title(this.title) {
    //   if (this.title === '') {
    //     return false
    //   }
    //   else {
    //     return true
    //   }
    // },
    },
    // findMovie(title) {
    //   console.log('여기가 되야지')
    //   this.movies.forEach(temp_movie => {
    //     console.log('잡았다')
    //     if (temp_movie.title == title) {
    //       console.log('잡았다')
    //       return this.movie = temp_movie
    //     }
    //   });
    // }
  }
}
</script>

<style>
  .search-bar { margin-bottom: 100px; }
  .search-result { margin: 50px 0;}
</style>