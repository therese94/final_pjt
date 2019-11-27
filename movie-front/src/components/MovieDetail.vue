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
        <!-- 영화 설명을 출력하세요. -->
        <!-- <div>관람객 수: {{ movie.audiAcc }}</div> -->
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
export default {
  name: 'MovieDetail',
  // 0. props 데이터를 받이 위하여 설정하시오.
  // movie 타입은 Object이며, 필수입니다.
  // 설정이 완료 되었다면, 상위 컴포넌트에서 값을 넘겨 주세요.
  // 그리고 적절한 곳에 사용하세요.
  data () {
    return {
    }
  },

  props: {
    movie: {
      type: Object,
      required: true,
    }
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