import { createRouter, createWebHistory } from 'vue-router'
import Home from "../views/Home"
import CreateNewsPage from "../views/CreateNewsPage.vue"
import LoginPage from "../views/LoginPage.vue"
import DetailNewsPage from "../views/DetailNewsPage"
import EditNewsPage from "../views/EditNewsPage"

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/login', component: LoginPage },
    { path: '/create-news', component: CreateNewsPage },
    { path: '/edit-news/:id', component: EditNewsPage, name: 'edit' },
    { path: '/detail-news/:id', component: DetailNewsPage, name: 'detail' }
  ]
})
