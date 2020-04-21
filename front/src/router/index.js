import Vue from 'vue'
import Router from 'vue-router'
import Editor from '@/components/Editor'
import Login from '@/components/Login'
import Home from '@/components/Home'
import Contact from '@/components/Contact'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/project/:project',
      name: 'editor',
      component: Editor,
      props: true
    },
    { 
      path: '/', 
      name: 'home',
      component: Home,
    },
    { 
      path: '/login', 
      name: 'login',
      component: Login,
    },
    { 
      path: '/contact', 
      name: 'Contact',
      component: Contact,
  },
  ]
})
