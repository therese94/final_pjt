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
        <div class="description_wrap">
          <h5 class="movie-title"><strong>{{ movie.title }}</strong></h5>
          <!-- 볼래요 -->
          <button class="see_btn btn" v-on:click="bolraeyo" v-if="bolraeyoTF=='bolraeyo'">볼래요</button>
          <button class="nosee_btn btn" v-on:click="bolraeyo" v-if="bolraeyoTF=='cancel'">볼래요 취소</button>
          <!-- <div class="rating">관람 평점 : {{ movie.star_rates }}</div> -->
          <div class="audi_cnt">누적 관객 : {{ movie.audiAcc }}</div>
          <p class="description">{{ movie.description }}</p>
        </div>
        <div class="poster_wrap"><img class="movie--poster poster_img" v-bind:src="movie.poster_url" v-bind:alt="movie.name"></div>
      </div>
      <div class="modal-body02">
        <!-- 평점 리뷰 들어갈 부분 -->
        <div class="modal02-wrap">
          <p>여러분의 리뷰를 남겨주세요!</p>
          <form class="input-group mb-3" @submit.prevent="onSubmit(movie.id)">
            <input v-model="score" type="number" class="rating_input" placeholder="평점" min="0" max="10" >
            <input v-model="content" type="text" class="review_input">
            <button type="submit" class="review_btn btn">등록</button>
          </form>
        </div>
      </div>

      <div class="modal-body03">
        <div class="modal03-wrap">
          <p>회원들의 리뷰를 확인해보세요!</p>
          <div class="review_content" v-for="review in reviews" :key="review.id">
            작성자: {{ review.user }} 평점: {{ review.score }}  내용: {{ review.content }}
            <span v-if="review.user===userId">
              <button class="delete-btn btn" @click="deleteReview(review.id)">삭제</button>
            </span>
          </div>
          
        </div>
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
  .modal-body { width: 800px; padding: 0 50px; padding-bottom: 30px; }

  .modal-body02, .modal-body03 { width: 800px; height: 150px; padding: 0 50px; padding-bottom: 50px; }
  .modal-body03 { overflow: hidden; }
  .modal02-wrap, .modal03-wrap { width: 100%; border-top: 1px solid #999; padding-top: 30px; }
  .modal02-wrap p, .modal03-wrap p { font-size: 16px; font-weight: bold; }
  

  .description_wrap { position: relative; width: 50%; float: left; }
  .movie-title { position: relative; width: 100%; height: 60px; line-height: 30px; font-size: 26px; color: #333; font-weight: bold; text-align: left; margin-bottom: 15px; border-bottom: 1px solid #999; border-top: 1px solid #999; padding: 15px 0; }
  
  .rating, .audi_cnt { width: 100%; height: 25px; line-height: 30px; font-size: 16px; font-weight: bold; text-align: left; margin-bottom: 15px; }
  .description { text-align: justify; line-height: 30px; font-size: 14px; }

  .poster_wrap { width: 45%; float: right; }
  .poster_img { width: 300px; float: right; }

  /* 볼래요 버튼 */
  .see_btn { box-sizing: border-box; position: absolute; top: 15px; right: 0; width: 75px; height: 35px; background-color: #f9f2d5; border: 1px solid #333; color: #333; font-weight: bold; }
  .see_btn:hover { background-color: #fce583; }

  .nosee_btn { box-sizing: border-box; position: absolute; top: 15px; right: 0; width: 100px; height: 35px; background-color: #f3f3f3; border: 1px solid #333; color: #333; font-weight: bold; padding-left: 5px; padding-right: 5px; }
  .nosee_btn:hover { background-color: #ededed; }

  .rating_input { box-sizing: border-box; width: 15%; display: block; float: left; margin-right: 5px; padding-left: 7px; }
  .review_input { box-sizing: border-box; width: 75%; display: block; float: left; margin-right: 5px; }
  .review_btn { box-sizing: border-box; display: block; float: left; top: 15px; right: 0; width: 60px; height: 30px; background-color: #f9f2d5; border: 1px solid #333; color: #333; font-weight: bold; padding: 0; line-height: 30px; text-align: center; }
  .review_btn:hover { background-color: #fce583; }

  .delete-btn { box-sizing: border-box; display: block; float: left; top: 15px; right: 0; width: 60px; height: 30px; background-color: #f3f3f3; border: 1px solid #333; color: #333; font-weight: bold; padding: 0; line-height: 30px; text-align: center; }
  .delete-btn:hover { background-color: #ededed; }

  .review_content { height: 25px; margin-bottom: 10px; }
</style>