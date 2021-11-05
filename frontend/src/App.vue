<template>

  <router-view/>

</template>

<script>
import {onMounted} from "vue"
import {useStore} from "vuex"

export default {
  name: 'Home',
  setup() {

    // data
    const store = useStore()

    async function getCategories() {
      await store.dispatch('requestCategories')
    }

    onMounted(() => getCategories())
  }
}
</script>
