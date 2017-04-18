// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import vueResource from 'vue-resource'
import VueRouter from 'vue-router'
import App from './App'
import Projects from './components/Projects.vue'
import Home from './components/Home.vue'

Vue.use(vueResource)
Vue.use(VueRouter)

const routes = [
  { path: '/projects', component: Projects },
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
  components: { App }
})
