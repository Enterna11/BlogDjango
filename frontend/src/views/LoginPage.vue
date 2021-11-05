<template>
  <div class="wrapper">
    <router-link to="/" class="navbar__link">На главную</router-link>
    <div class="login-form on-center">
      <label for="login">Введите логин:</label>
      <input type="text" v-model="username" id="login">
      <label for="pass">Введите пароль:</label>
      <input type="password" v-model="password" id="pass" @keypress.enter="authorization">
      <button class="btn on-center" @click="authorization">Войти</button>
    </div>
  </div>
</template>

<script>
import {ref} from 'vue'
import {useStore} from "vuex"

export default {
  name: "LoginPage",
  setup() {

    // data
    const username = ref('')
    const password = ref('')
    const store = useStore()

    // methods
    async function authorization() {
      await store.dispatch('getToken', {username: username.value, password: password.value})
    }

    return {
      username, password,
      authorization
    }
  }
}
</script>

<style scoped>

</style>