<template>
  <div class="success on-center" v-if="completeNews">
    <slot></slot>
    <router-link to="/">На главную</router-link>
  </div>

  <form class="create-form" v-if="isAuthenticated  && completeNews === false" @submit.prevent="isValid">
    <label for="title">Введите название:</label>
    <input type="text" v-model="newsData.title" id="title">
    <small class="errors" v-if="errors.title">Вы не ввели название</small>
    <label>Выберите категорию: </label>
    <select v-model="newsData.category">
      <option v-for="category in categories" :key="category.id">{{ category.title }}</option>
    </select>
    <label>Введите текст:</label>
    <textarea v-model="newsData.content" id="content"></textarea>
    <small class="errors" v-if="errors.content">Вы не ввели текст</small>
    <div class="file">
      <label for="file" class="file__label">Выберите изображение</label>
      <input type="file" id="file" @change="getImage">
      <br/>
      <img :src="newsData.photo" alt="">
    </div>
    <div class="checkbox">
      <label for="show" style="display: inline">Опубликовать?</label>
      <input v-model="newsData.is_published" type="checkbox" id="show">
    </div>
    <button class="btn" type="submit">Отправить</button>
  </form>
</template>

<script>
import {useStore} from "vuex"
import {ref, reactive, onMounted} from 'vue'

export default {
  name: "CreateNewsPage",
  emits: ['complete-news'],
  props: ['completeNews', 'editNews'],
  setup(props, context) {

    // data
    const store = useStore()
    const categories = ref(store.getters.categories)
    const isAuthenticated = ref(store.getters.statusUser)
    const news = new FormData()
    const newsData = ref({
      'title': '',
      'category': 'Наука',
      'content': '',
      'is_published': '',
      'photo': ''
    })
    const errors = reactive({
      'title': '',
      'content': '',
    })

    // methods
    async function sendNews() {
      await getFormData()
      context.emit('complete-news', news)
    }

    function getFormData() {
      for (let item in newsData.value) {
        console.log(newsData.value[item])
        news.append(item, newsData.value[item])
      }
    }

    function isValid() {
      if (newsData.value.title.length === 0) {
        errors.title = 'Не может быть пустым'
      } else if (newsData.value.content.length === 0) {
        errors.content = 'Вы не добавили текст статьи'
      } else {
        errors.title = null
        errors.content = null
        sendNews()
      }
    }

    function getImage(event) {
      news.append('photo', event.target.files[0])
      const reader = new FileReader()
      const image = event.target.files[0]
      reader.onload = () => {
        newsData.value['photo'] = reader.result
      }
      if (image) {
        reader.readAsDataURL(image)
      } else {
        newsData.value.photo = ''
      }
    }

    function check() {
      if (props.editNews) {
        newsData.value = props.editNews
      }
    }

    onMounted(() => check())

    return {
      categories, isAuthenticated, errors, newsData,
      getImage, isValid
    }
  }
}
</script>

<style scoped>

</style>