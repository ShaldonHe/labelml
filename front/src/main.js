// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.css'

Vue.config.productionTip = false
Vue.use(Vuetify)

console.log(process.env.NODE_ENV, process.env.NODE_ENV === 'development')
let ENDPOINT
if (process.env.NODE_ENV === 'development') {
  ENDPOINT = 'http://localhost:5000'
} else {
  ENDPOINT = 'http://ml.beyes.com:11080'
}
console.log(ENDPOINT)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  vuetify: new Vuetify(),
  components: { App },
  template: '<App/>'
})
