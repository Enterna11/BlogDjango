<template>
  <header>
    <AppNavBar
        @open-category="sendCategoryName"
        @search-news="sendRequest"
        @reset-page="resetPage"
    />
  </header>

  <main>
    <AppNewsList/>
  </main>
</template>

<script>
import AppNewsList from "../components/AppNewsList"
import AppNavBar from "../components/AppNavBar"
import {ref, provide, onMounted} from "vue"
import axios from "axios";

export default {
  name: 'Home',
  setup() {

    // data
    const params = ref('')
    const newsType = ref('')
    const news = ref({
      'chapter': '',
      'next': '',
      'content': [],
    })

    // methods
    function sendCategoryName(data) {
      newsType.value = 'category'
      params.value = data
      getNews(1, true)
    }

    function sendRequest(data) {
      params.value = data
      newsType.value = 'search'
      getNews(1, true)
    }

    function resetPage() {
      newsType.value = 'all'
      params.value = ''
      getNews(1, true)
    }

    async function getNews(pageNum, resetContent = false) {
      const {data} = await axios.get(`http://127.0.0.1:8000/api/v1/news/${newsType.value}/${params.value}?page=${pageNum}`)
      await getNewsData(data, resetContent)
    }

    function getNewsData(data, resetContent) {
      if (resetContent === true) {
        news.value.content = []
      }
      news.value.chapter = data.chapter
      news.value.content = news.value.content.concat(data.results)
      news.value.next = data.link.next
    }


    let isLoading = false

    async function endlessScroll() {
      const height = document.body.offsetHeight
      const screenHeight = window.innerHeight
      const scrolled = scrollY
      const threshold = height - screenHeight / 5
      const position = scrolled + screenHeight
      if (position >= threshold && isLoading === false && Number(news.value.next) !== 0) {
        isLoading = true
        await getNews(Number(news.value.next))
        isLoading = false
      }
    }

    window.addEventListener('scroll', () => setTimeout(endlessScroll, 100))

    onMounted(() => resetPage())

    provide('news', news)

    return {
      news,
      resetPage, sendCategoryName, sendRequest
    }
  },
  components: {
    AppNavBar, AppNewsList
  }
}
</script>