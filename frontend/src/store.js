import { createStore } from "vuex"
import axios from "axios"
import createPersistedState from 'vuex-persistedstate'
import {router} from "./router"

export const store = createStore({
    plugins: [createPersistedState()],
    state() {
        return {
            isAuthenticated: false,
            categoriesList: [],
            newsEdit: {},
            userProfile: {
                'email': '',
                'userName': '',
                'userToken': '',
            },
        }
    },
    mutations: {
        saveCategory(state, data) {
            state.categoriesList = data
        },

        saveUserProfile(state, data) {
            state.userProfile.email = data[0].email
            state.userProfile.userName = data[0].username
            state.userProfile.userToken = data[1]
            state.isAuthenticated = true
        },

        clearData(state) {
            state.isAuthenticated = false
            state.userProfile.email = ''
            state.userProfile.userName = ''
            state.userProfile.userToken = ''
        },

        saveEditNews(state, data) {
            state.newsEdit = data
        },

        clearEditNews(state) {
            state.newsEdit = {}
        }
    },
    getters: {
        categories(state) {
            return state.categoriesList
        },

        statusUser(state) {
            return state.isAuthenticated
        },

        userProfile(state) {
            return state.userProfile
        },

        newsEdit(state) {
            return state.newsEdit
        }
    },
    actions: {
        async requestCategories(context) {
            const {data} = await axios.get('http://127.0.0.1:8000/api/v1/news/category/all/')
            context.commit('saveCategory', data)
        },

        async getToken(context, userData) {
            await axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/api/v1/auth/token/login/',
                data: {
                    username: userData.username,
                    password: userData.password
                }
            }).then(async response => {
                    if (response.status === 200) {
                        await context.dispatch('getProfile', response.data['auth_token'])
                        await router.replace('/')
                    }
                })
            .catch(er => {
                alert('Проверьте правильность введенных данных')
            })
        },

        async getProfile(context, userToken) {
            const {data} = await axios({
                method: 'get',
                headers: {'authorization': 'Token ' + userToken},
                url: 'http://127.0.0.1:8000/api/v1/auth-dj/users/me'
            })
            context.commit('saveUserProfile', [data, userToken])
        },

        async logout(context) {
            await axios({
                method: 'post',
                headers: {'authorization': 'Token ' + context.state.userProfile.userToken},
                url: 'http://127.0.0.1:8000/api/v1/auth/token/logout'
            })
            context.commit('clearData')
            await router.replace('/')
        }
    }
})