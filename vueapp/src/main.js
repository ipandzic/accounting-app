// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import vueResource from 'vue-resource'
import VueRouter from 'vue-router'
import App from './App'
import Projects from './components/Projects.vue'
import Parties from './components/Parties.vue'
import Transactions from './components/Transactions.vue'
import Home from './components/Home.vue'

Vue.use(vueResource)
Vue.use(VueRouter)

Vue.http.options.xhr = {withCredentials: true}

const routes = [
  { path: '/projects', component: Projects },
  { path: '/parties', component: Parties },
  { path: '/transactions', component: Transactions },
  { path: '/', component: Home }
]

const router = new VueRouter({
  routes,
  mode: 'history'
})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App },
  data: {
    selected: ''
  }
})
