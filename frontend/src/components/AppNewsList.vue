<template>
  <div class="card" v-for="(item, idx) in newsList.content" :key="item.id">
    <router-link :to="{ name: 'detail', params: { id: item.id}}" class="card__title">{{ item.title }}</router-link>
    <img :src="item.photo" alt="" v-if="item.photo" :class="newsList.content[idx].resize" @click="resizeChange(idx)">
    <img src="../assets/alt.jpg" alt="" v-else>
    <div class="card__content">
      <p class="content__text" v-if="item.isOpen">{{ item.content }}</p>
      <button class="btn" @click="openContent(idx)">{{ item.isOpen ? 'Свернуть': 'Развернуть'}}</button>
      <button class="btn" v-if="item.author === userName" @click="newsEdit(item.id)">Редактировать</button>
      <br/>
      <small><strong>Автор: </strong>{{ item.author }}</small>
      <br/>
      <small><strong>Категория: </strong>{{ item.category }}</small>
      <br/>
      <small><strong>Дата добавления: </strong>{{ item.created_at }}</small>
    </div>
  </div>
</template>

<script>
import {computed, inject, ref} from 'vue'
import {useStore} from "vuex"
import {useRouter} from 'vue-router'

export default {
  name: "AppNewsList",
  setup() {

    // data
    const store = useStore()
    const userName = computed(() => store.getters.userProfile.userName)
    const router = useRouter()
    const newsList = inject('news')

    let isOpen = false

    function openContent(idx) {
      newsList.value.content[idx].isOpen = !newsList.value.content[idx].isOpen
    }

    function newsEdit(id) {
      router.push({name: 'edit', params: {id: id}})
    }

    function resizeChange(idx) {
      if (newsList.value.content[idx].hasOwnProperty('resize') === false) {
        newsList.value.content[idx].resize = ''
        }
      if (newsList.value.content[idx].resize === '') {
        newsList.value.content[idx].resize = 'card_full'
      } else {
        newsList.value.content[idx].resize = ''
      }
    }

    return {
      userName, isOpen, newsList,
      openContent, newsEdit, resizeChange
    }
  }
}

</script>

<style scoped>

</style>