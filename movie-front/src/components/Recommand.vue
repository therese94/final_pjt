<template>

  <div class="Recommand-page">
    <MovieList :movies="movies"/>
    
    <Follower v-for="follower in following_users" v-bind:key="follower.id" :follower="follower"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Follower from './Follower.vue'
import MovieList from './MovieList.vue'
import axios from 'axios'

export default {
  name: 'Recommand',
  data() {
    return {
      reviews: [],
      movies: [],
    }
  },
  components: {
    Follower,
    MovieList,
  },
  props: {
    following_users:{
      type: Array,
      required: false,
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ])
  },
  methods: {
    get_recommended_movie(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/movies/reviews/`)
      .then(response => {
        this.reviews = response.data
        this.reviews.forEach(element => {
          if (element.score >= 8) {
            if (this.movies.length < 8) {
              axios.get(`${SERVER_IP}/movies/${element['movie']}/`)
                .then(response => {
                  this.movies.push(response.data)
                })
                .catch(error => {
                  console.error(error)
                })
            }
          }
        });
      })
      .catch(error => {
        console.error(error)
      })
    }
  },
  mounted() {
    console.log('Recommand Mount')
    this.get_recommended_movie()
    // $(document).ready(function(){
    //   $(".movie_content").addClass("test")
  
    // });

  },
}
</script>

<style>
.Recommand-page { text-align: center; margin: 0 auto; background-color: #ededed; }
.Movie-list { margin: 0 auto; padding-top: 30px; }
.movie_content { border: none; background-color: #fff; margin-left: 10px; margin-right: 10px; width: 280px; float: left; padding-top: 30px; padding-bottom: 30px; }

</style>