<template>
  <div v-if="following_users != []">
    <span>{{ following_users }}</span>
  </div>
</template>

<script>
export default {
  name: 'FollowersList',
  // components: {
  //   MovieListItem,
  // },
  data() {
    return {
      followers_data: [],
    }
  },
  props: {
    following_users: {
      type: Array,
      required: false,
    }
  },
  methods: {
    get_followers_info(){
      console.log('뭐')
      console.log(this.following_users)
    },
    mounted() {
      this.get_followers_info()
    },
  },
  
}
</script>

<style>

</style>