<template>

  <AppCreateEditForm
  :completeNews="editedNews"
  :editNews="news"
  @complete-news="sendChange"
  :key="formKey">
      <h1>Ваша новость успешно изменена</h1>
  </AppCreateEditForm>

</template>

<script>
import AppCreateEditForm from "../components/AppCreateEditForm"
import {ref, onMounted} from 'vue'
import {useRoute} from "vue-router"
import {useStore} from "vuex"
import axios from "axios"

export default {
  name: "EditNewsPage",
  components: {AppCreateEditForm},
  setup() {
    // data
    const editedNews = ref(false)
    const news = ref({})
    const formKey = ref(0)
    const store = useStore()
    const route = useRoute()
    const id = ref(route.params['id'])

    // methods
    async function getEditingNews(id) {
      const {data} = await axios.get(`http://127.0.0.1:8000/api/v1/news/${id}/`)
      news.value = data
      formKey.value += 1
    }

    async function sendChange(newsChange) {
      await axios.put(`http://127.0.0.1:8000/api/v1/news/${id.value}/`, newsChange, {
        headers: {
          'authorization': 'Token ' + store.getters.userProfile.userToken,
          'content-type': 'multipart/form-data'
        }
      }).then(() => editedNews.value = true)
    }

    onMounted(() => getEditingNews(id.value))

    return {
      editedNews, news, formKey, sendChange
    }
  }
}
</script>

<style scoped>

</style>