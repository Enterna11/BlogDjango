<template>
  <div class="detail-news">
    <div class="card">
      <a class="card__title">{{ news.title }}</a>
      <img :src="news.photo" alt="" v-if="news.photo">
      <img src="../assets/alt.jpg" alt="" v-else>
      <div class="card__content">
        <p class="content__text">{{ news.content }}</p>
        <button class="btn" v-if="news.author === userName">Редактировать</button>
        <br/>
        <small><strong>Автор: </strong>{{ news.author }}</small>
        <br/>
        <small><strong>Категория: </strong>{{ news.category }}</small>
        <br/>
        <small><strong>Дата добавления: </strong>{{ news.created_at }}</small>
      </div>
    </div>

    <div class="comments" v-if="news.news_comment.length !== 0">
      <div class="comment" v-for="comment in news.news_comment" :key="comment">
        <p class="comment__username">{{ comment.user }}</p>
        <p class="comment__content">{{ comment.content }}</p>
      </div>
    </div>

    <button class="btn" @click="isEditing = true">Добавить комментарий</button>
    <div class="create-login-form" id="comment-form" v-if="isEditing">
      <textarea v-model="comment.content" @keypress.enter="createComment"></textarea>
      <br/>
      <button class="btn" @click="createComment">Отправить</button>
      <button class="btn" @click="isEditing = false">Отмена</button>
    </div>
  </div>

</template>

<script>
import {computed, reactive, ref, watch, onMounted} from "vue"
import {useStore} from "vuex"
import {useRoute} from "vue-router"
import axios from "axios"

export default {
  name: "DetailNewsPage",
  setup() {

    // data
    const userName = computed(() => store.getters.userProfile.userName)
    const isEditing = ref(false)
    const store = useStore()
    const route = useRoute()
    const comment = reactive({
      'user': userName,
      'content': '',
      'news': route.params['id']
    })
    const news = ref({
      'title': '',
      'content': '',
      'is_published': '',
      'news_comment': [],
      'created_at': '',
      'photo': '',
      'author': ''

    })

    // methods
    async function getDetailNews(id) {
      const {data} = await axios.get(`http://127.0.0.1:8000/api/v1/news/${id}/`)
      news.value = data
    }

    async function createComment() {
      const {data} = await axios.post('http://127.0.0.1:8000/api/v1/news/comment/create', comment, {
        headers: {
          'authorization': 'Token ' + store.getters.userProfile.userToken,
        }
      })
      news.value.news_comment.push(data)
      isEditing.value = false
    }

    watch(isEditing, (value) => {
      if (value === true) {
        setTimeout(() => {
          const form = document.getElementById('comment-form')
          form.scrollIntoView({block: "center", behavior: "smooth"})
        }, 50)
      }
    })

    onMounted(() => getDetailNews(route.params['id']))

    return {
      news, isEditing, userName, comment,
      createComment
    }
  }
}
</script>

<style scoped>

</style>