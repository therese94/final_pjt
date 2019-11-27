<template>
<!-- vue 콘솔에서 확인하여, 추가 정보들도 출력하세요. -->
<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<div class="modal fade" tabindex="-1" role="dialog" v-bind:id="`movie_${movie.id}`">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <!-- 영화 제목을 출력하세요. -->
        <h5 class="modal-title">{{ movie.title }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <!-- 영화 설명을 출력하세요. -->
        <div>관람객 수: {{ movie.audiAcc }}</div>
        <img class="movie--poster my-3" v-bind:src="movie.poster_url" v-bind:alt="movie.name">

        <!-- 볼래요 및 평점 리뷰가 들어갈 부분 -->
        <button class="btn btn-success" v-on:click="bolraeyo">볼래요</button>

        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'


export default {
  name: 'MovieDetail',
  
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },

  props: {
    movie: {
      type: Object,
      required: true,
    }
  },
  methods: {
    bolraeyo() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP

      const data = {
        movie_id: this.movie.id,
        user: this.userId
      }

      axios.post(`${SERVER_IP}/accounts/potential/${data.user}/${data.movie_id}/`, data)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
}
</script>

<style scoped>
</style>