<template>
  <nav class="navbar">
    <a class="navbar__link" @click.prevent="$emit('reset-page')">Главная</a>
    <div class="dropdown">
      <a>Категории</a>
      <ul class="dropdown__menu">
        <li v-for="category in categories">
          <a class="navbar__link" @click.prevent="$emit('open-category', category.title)">
            {{ category.title }}
          </a>
        </li>
      </ul>
    </div>
    <div class="navbar__search">
      <label class="navbar__item" for="search">Поиск: </label>
      <input id='search' type="text" v-model="result" @keypress.enter="searchNews">
    </div>
    <router-link class="navbar__link" to="/login" v-if="isAuthenticated === false">Войти</router-link>
    <div id='dropdown_2' class="dropdown" v-if="isAuthenticated">
      <a class="dropdown__trigger" >{{ userName }}</a>
      <ul class="dropdown__menu">
        <li class="dropdown__item"><a class="navbar__link" @click="$emit('search-news', userName)">Мои новости</a></li>
        <li class="dropdown__item">
          <router-link class="navbar__link" to="/create-news">Добавить новость</router-link>
        </li>
        <li class="dropdown__item">
          <a class="navbar__link" @click.prevent="logout">Выйти</a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
import {computed, ref} from 'vue'
import { useStore } from 'vuex'

export default {
  name: "AppNavBar",
  emits: ['search-news', 'open-category', 'reset-page'],
  setup(props, context) {

    // data
    const store = useStore()
    const categories = ref(store.getters.categories)
    const isAuthenticated = computed(() => store.getters.statusUser)
    const userName = computed(() => store.getters.userProfile.userName)
    const result = ref('')

    // methods
    async function logout() {
      await store.dispatch('logout')
    }

    function searchNews() {
      context.emit('search-news', result.value)
      result.value = ''
    }

    return {
      result, categories, isAuthenticated, userName,
      logout, searchNews
    }
  },
  components: {

  }
}
</script>

<style scoped>

</style>