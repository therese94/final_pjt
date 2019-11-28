<template>
  <div class="story-wrap">
    
        <div class="story-content01 st-cont">
            <h3>SERVICE</h3>
            <p>Mooving은 영화 추천 웹서비스입니다.</p>
            <p>‘평점주기’, ‘볼래요’, ‘친구 팔로우’ 등 다양한 기능을제공합니다.</p>
            <div class="story-imgWrap01 st-imgWrap">
                <img src="../assets/main/story_content01.png" alt="스토리 이미지01" data-aos="fade-up" data-aos-duration='800'>
            </div>
        </div>
        <div class="story-content02 st-cont">
            <h3>STORY</h3>
            <p>감상한영화에 평점을 남기거나 보고싶은 영화에 ‘볼래요’를 눌러보세요!</p>
            <p>Mooving 서비스를 이용할수록 경험치가 쌓여 팝콘이 레벨업합니다!</p>
            <div class="story-imgWrap02 st-imgWrap">
                <img src="../assets/main/story_content02.png" alt="스토리 이미지02" data-aos="fade-up" data-aos-duration='800'>
            </div>
        </div>
        <div class="story-content03 st-cont">
            <h3>CI / BI</h3>
            <p>Mooving 은 Movie와 Moving의 합성어로</p>
            <p>감동을 전하고자하는 브랜드아이덴티티를 드러냅니다.</p>
            <div class="story-imgWrap03 st-imgWrap">
                <img src="../assets/main/story_content03.png" alt="스토리 이미지03" data-aos="fade-up" data-aos-duration='800'>
            </div>
        </div>
    
  </div>
</template>

// <script>
//   import { animateOnScroll } from "mdbvue";
//   export default {
//     name: "AnimationsPage",
//     directives: {
//       animateOnScroll
//     }
//   }
// </script>

<script>


export default {
  name: 'Story',
  components: {
    
  },
  data() {
    return {
      
    }
  },
  methods:{
    
  },
  mounted() {
    
  },
}
</script>

<style>
    .story-wrap { width: 100%; }
    .story-wrap h1 { color: #282118; }
    .st-imgWrap { height: 310px; margin-top: 50px; }
    .story-imgWrap01 { background-color: #f9f2d5; }
    .story-imgWrap01 img { margin-top: 50px; }
    .story-imgWrap02 img { margin-top: 50px; }
    .story-imgWrap03 { background-color: #f3f3f3; }
    .story-imgWrap03 img { margin-top: 70px; }
    .story-img { width:"1200px"; height: 1380px; }

    .st-cont {margin-bottom: 50px; margin-top: 30px; }
    .st-cont h3 { font-size: 26px; font-weight: bold; margin-bottom: 20px; margin-top: 80px; color: #282118; }
    .st-cont p {font-size: 14px; height: 16px; line-height: 16px; margin-bottom: 5px; }
</style>