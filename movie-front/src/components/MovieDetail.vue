<template>
<!-- vue 콘솔에서 확인하여, 추가 정보들도 출력하세요. -->
<!-- 고유한 모달을 위해 id 속성을 정의하시오. 예) movie-1, movie-2, ... -->
<div class="modal fade" tabindex="-1" role="dialog" v-bind:id="`movie_${movie.id}`">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <!-- 영화 제목을 출력하세요. -->
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <!-- 볼래요 및 평점 리뷰가 들어갈 부분 -->
        <button class="btn btn-success" v-on:click="bolraeyo" v-if="bolraeyoTF=='bolraeyo'">볼래요</button>
        <button class="btn btn-success" v-on:click="bolraeyo" v-if="bolraeyoTF=='cancel'">볼래요 취소</button>
        <!-- 평점 리뷰 들어갈 부분 -->
        <form class="input-group mb-3" @submit.prevent="onSubmit(movie.id)">
          <input v-model="score" type="text" class="form-control">
          <input v-model="content" type="text" class="form-control">
          <button type="submit" class="btn btn-success">리뷰 남기기</button>
        </form>
        <div v-for="review in reviews" :key="review.id">
          작성자: {{ review.user }} 평점: {{ review.score }}  내용: {{ review.content }}
          <span v-if="review.user===userId">
            <button class="btn btn-delete" @click="deleteReview(review.id)">삭제</button>
          </span>
        </div>
        <div class="description_wrap">
          <h5 class="movie-title"><strong>{{ movie.title }}</strong></h5>
          <!-- <div class="rating">관람 평점 : {{ movie.star_rates }}</div> -->
          <div class="audi_cnt">누적 관객 : {{ movie.audiAcc }}</div>
          <p class="description">{{ movie.description }}</p>
        </div>
        <div class="poster_wrap"><img class="movie--poster poster_img" v-bind:src="movie.poster_url" v-bind:alt="movie.name"></div>
      </div>
      <!--<div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div> -->
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieDetail',
  // 0. props 데이터를 받이 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  data () {
    return {
      score: '',
      content: '',
      bolraeyoTF: 'cancel',
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
    },
    reviews: {
      type: Array,
      required: false,
    },
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
          this.bolraeyoTF = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },

    async onSubmit(movie_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const user_id = this.userId
      const data = {
        score: this.score,
        content: this.content
      }
      await axios.post(`${SERVER_IP}/movies/create_review/${movie_id}/${user_id}/`, data)

      this.$emit('get_review', movie_id)
    },
    deleteReview(review_id) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.delete(`${SERVER_IP}/movies/delete_review/${review_id}/`)
        .then(response => {
          console.log(response)
          this.reviews.splice(review_id, 1)
          this.$emit('get_review', this.movie.id)
        })
        .catch(error => {
          console.log(error)
        })
    },
  },
}
</script>

<style scoped>
  .modal-dialog { max-width: 1000px; margin-top: 10%; }
  .modal-header{ border: none; }
  .modal-content { width: 800px; margin: 0 auto; }
  .modal-body { width: 800px; padding: 0 50px; padding-bottom: 50px; }

  .description_wrap { width: 50%; float: left; }
  .movie-title {width: 100%; height: 60px; line-height: 30px; font-size: 26px; color: #333; font-weight: bold; text-align: left; margin-bottom: 15px; border-bottom: 1px solid #999; border-top: 1px solid #999; padding: 15px 0; }
  
  .rating, .audi_cnt { width: 100%; height: 25px; line-height: 30px; font-size: 16px; font-weight: bold; text-align: left; margin-bottom: 15px; }
  .description { text-align: justify; line-height: 30px; font-size: 14px; }

  .poster_wrap { width: 45%; float: right; }
  .poster_img { width: 300px; float: right; }
</style>