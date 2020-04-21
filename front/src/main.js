// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ApolloClient, {createNetworkInterface} from 'apollo-client';
import VueApollo from 'vue-apollo';
import Vuetify from 'vuetify'
// import VList from 'vuetify/src/components/VList'

var config = require('../config')
import '../node_modules/vuetify/dist/vuetify.css'
// import('../node_modules/vuetify/dist/vuetify.css')
// import('../node_modules/vuetify/dist/vuetify.')

console.log(process.env.NODE_ENV, process.env.NODE_ENV === 'development')
if (process.env.NODE_ENV === 'development') {
  var ENDPOINT = 'http://localhost:5000';
} else {
  var ENDPOINT = 'http://ml.beyes.com:11080';
}
Vue.config.productionTip = false

console.log(ENDPOINT);

const apolloClient = new ApolloClient({
  networkInterface: createNetworkInterface({
    uri: `${ENDPOINT}/graphql`,
    transportBatching: true,
    mode: 'no-cors',
  }),
});

Vue.use(VueApollo, {
  apolloClient,
});
Vue.use(Vuetify);

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
  defaultOptions: {
    $loadingKey: 'loading'
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  apolloProvider,
  router,
  template: '<App/>',
  components: { 
    App
  },
  vuetify: new Vuetify()
})
