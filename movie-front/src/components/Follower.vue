<template>
  <div>
    <p><strong> {{ follower.username }} 이 재밌게 본 영화! </strong></p>
    <div class="recommend_movie"><MovieList :movies="movies"/></div>
    
  </div>
</template>


<script type="text/javascript" src="http://code.jquery.com/jquery-3.2.0.min.js" ></script>
<script>
import MovieList from '../components/MovieList'
import axios from 'axios'


  

export default {
  name: 'Follower',
  components: {
    MovieList,
  },
  data() {
    return {
      movies_id: [],
      movies: [],
    }
  },
  props: {
    follower: {
      type: Object,
      required: true,
    }
  },
  methods: {
    follower_movie() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const reviews = this.follower.reviews
      
      if (reviews.length >= 1) {
        reviews.forEach(element => {
          axios.get(`${SERVER_IP}/movies/review_detail/${element}/`)
            .then(response => {
              if (response.data['score'] >= 0) {
                axios.get(`${SERVER_IP}/movies/${response.data['movie']}/`)
                  .then(response => {
                    this.movies.push(response.data)
                  })
                  .catch(error => {
                    console.log(error)
                  })
                }
          });
        });
      }
    }
  },
  mounted() {
    console.log('Follower 오는지 확인')
    this.follower_movie()
    $(document).ready(function(){
      $(".Movie-list > div").addClass("test")
  
    });
    
    
  },
}
</script>


<style>
/* .movie_content { height: 250px; margin-bottom: 20px; } */
/* .recommend_movie > div > div { border: 10px solid black; } */
.test { background-color: blue; }

</style>