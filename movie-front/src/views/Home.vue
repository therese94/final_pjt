<template>
  <div class="home">
    
    
    <div class="main">
      <div class="main_img_wrap">
        <sequential-entrance fromTop >
          <img class="main_img main_img01" alt="메인이미지01" src="../assets/main/main_img_bg.png">
        </sequential-entrance>
        <sequential-entrance fromLeft >
          <img class="main_img main_img02" alt="메인이미지02" src="../assets/main/main_img_bg_line.png">
        </sequential-entrance>
        <sequential-entrance fromBottom >
          <img class="main_img main_img03" alt="메인이미지03" src="../assets/main/main_character.png">
        </sequential-entrance>
      </div>

      <div class="sub_img_wrap">
        <sequential-entrance fromTop >
          <img class="sub_img sub_img01" alt="서브이미지01" src="../assets/main/main_subimg_bg.png">
        </sequential-entrance>
        <sequential-entrance fromRight >
          <img class="sub_img sub_img02" alt="서브이미지02" src="../assets/main/main_subimg_bg_line.png">
        </sequential-entrance>
      </div>
    
      <div class="main_text_wrap">
        <div class="main_txt main_txt01">Mooving Movie <br> is Mooving</div>
        <div class="main_txt main_txt02">무빙에서 취향저격 영화를 찾고</div>
        <div class="main_txt main_txt03">나만의 무비리스트를 만들어보세요!</div>
        <div class="main_searchBtn"></div>
        <router-link to="/about" class="main_searchBtn"><img class="main_searchBtn_img" src="../assets/main/main_searchBtn.png"></router-link>
      </div>

    </div>
    <div class="main_content01">
      <div class="con01_titleWrap">
        <p class="con01_title"> MOVIE FOR YOU </p>
        <Recommand :following_users="following_users"/>
        <div class="con01"></div>
        <div class="con01_borderBottom"></div>
      </div>
    </div>
    
  </div>
  
</template>


<script>
// @ is an alias to /src
import Recommand from '../components/Recommand.vue'
import axios from 'axios'
import { mapGetters } from 'vuex'
import router from '@/router'

export default {
  name: 'home',
  components: {
    Recommand,
  },
  data() {
    return {
      following_users: [],
    }
  },
  computed: {
    // getters가 가지고 있는 모든 친구들을 computed 에 쫙 뿌려준다고 생각하면 된다.
    ...mapGetters([
      'isLoggedIn',
      'options',
      'userId'
    ])
  },
  methods: {
    checkLoggedIn() {
      if(!this.isLoggedIn) {
        router.push('/login')
      }
    },
    find_followers() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/accounts/${this.userId}/`)
        .then(response => {
          const id_list = response.data.followers
          const temp = []
          for (let index = 0; index < id_list.length; index++) {
            var user_id = id_list[index]
            axios.get(`${SERVER_IP}/accounts/${user_id}/`)
            .then(response => {
              temp.push(response.data)
            })
          }
          this.following_users = temp
          console.log(this.following_users)
        })
        .catch(error => {
          console.error(error)
        })
    },
  },
  mounted() {
      // if (this.isLoggedIn){
      //   this.checkLoggedIn()
      // }
      this.find_followers()
    },
}

</script>




<style>
  .home { width: 100% ; height: 1500px; margin: 0 auto; }

  .main { width: 1200px; position: relative; margin: 0 auto; height: 650px; }
  .main_content01 { width: 100%; height: 500px; }
  .con01_title { font-size: 24px; font-weight: bold; color: #353029; }

  .sub_img_wrap { width: 500px; height: 240px; position: absolute; top: -210px; right: 200px; z-index: -1; }
  .sub_img { position: absolute; }

  .main_img_wrap { width: 840px; height:550px; position: absolute; top: 0; left: 0; }

  .main_img { position: absolute; left: 0; }


  .main_text_wrap{ position: absolute; right: 0; top: 100px;  width: 410px; height: 550px; }
  .main_txt { right: 0; text-align: right; width: 410px; color: #353029; }
  .main_txt01 { height: 160px; font-size: 55px; font-weight: bold; margin-bottom: 20px; text-shadow: 2px 2px 2px #ededed; }
  .main_txt02 { font-size: 16px; margin-bottom: 10px; }
  .main_txt03 { font-size: 16px; margin-bottom: 40px; }

  .main_searchBtn { display: block; right: 0; text-align: right; }

  .con01_titleWrap { width: 100%; height: 45px; background-image: url(../assets/main/main_con01_border.png); text-align: center; background-repeat: no-repeat; background-position: center; }
  .con01_title { line-height: 45px; font-size: 26px; opacity: 80%; }
  .con01 { width: 1200px; margin: 0 auto; height: 450px;}
  .con01_borderBottom {width: 100%; height: 45px; background-image: url(../assets/main/main_con01_border_bottom.png); text-align: center; background-repeat: no-repeat; background-position: center;}

</style>
