<template>

  <AppCreateEditForm
  @complete-news="createNews"
  :completeNews="newsCreated">
      <h1>Поздравляем, Вы успешно добавили новость</h1>
  </AppCreateEditForm>

</template>

<script>
import AppCreateEditForm from "../components/AppCreateEditForm"
import {ref} from 'vue'
import {useStore} from "vuex"
import axios from "axios"

export default {
  name: 'CreateNews',
  components: {AppCreateEditForm},
  setup() {

    // data
    const store = useStore()
    const newsCreated = ref(false)

    // methods
    async function createNews(news) {
      await axios.post('http://127.0.0.1:8000/api/v1/news/create/', news, {
        headers: {
          'authorization': 'Token ' + store.getters.userProfile.userToken,
          'content-type': 'multipart/form-data'
        }
      }).then(() => newsCreated.value = true)
    }

    return {
      newsCreated,
      createNews
    }
  }
}
</script>