<template>
  <div class="todo-list">
    <div class="card mb-3" v-for="todo in todos" :key="todo.id">
      <div class="card-body d-flex justify-content-between">
        <span>{{ todo.title }}</span>
        <!-- <span @click="deleteTodo(todo)">삭제</span> -->
        <!-- <button class="btn btn-delete">삭제</button> -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
  methods: {
    findMovie()
  }
}
</script>

<style>

</style>