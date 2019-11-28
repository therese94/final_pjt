<template>
  <div class="Recommand-page">
    <h2>영화 추천 알고리즘</h2>
    <Follower v-for="follower in following_users" v-bind:key="follower.id" :follower="follower"/>
    <!-- <FollowersList :following_users="following_users"/> -->
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Follower from './Follower.vue'

export default {
  name: 'Recommand',
  data() {
    return {
    }
  },
  components: {
    Follower,
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
  mounted() {
    console.log('sefaioj')
  },
}
</script>

<style>

</style>