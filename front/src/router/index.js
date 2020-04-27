import Vue from 'vue'
import Router from 'vue-router'
// import Editor from '@/components/annotator/Editor'
// import Viewer from '@/components/dataest/Viewer'
// import Regist from '@/components/user/Regist'
// import Home from '@/components/Home'
// import Contact from '@/components/Contact'
// import ContactCH from '@/components/ContactCH'
// import ContactEN from '@/components/ContactEN'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'home',
    component: () => import('@/components/Home')
  },
  {
    path: '/user/login',
    name: 'login',
    component: () => import('@/components/user/Login'),
    props: true
  },
  {
    path: '/user/regist',
    name: 'regist',
    component: () => import('@/components/user/Regist'),
    props: true
  },
  {
    path: '/annotator/:project',
    name: 'editor',
    component: () => import('@/components/annotator/Editor'),
    props: true
  },
  {
    path: '/ch',
    name: 'ContactCH',
    component: () => import('@/components/ContactCH')
  },
  {
    path: '/en',
    name: 'ContactEN',
    component: () => import('@/components/ContactEN')
  },
  {
    path: '/project/:project',
    name: 'editor',
    component: () => import('@/components/annotator/Editor'),
    props: true
  },
  {
    path: '/contact',
    name: 'Contact',
    component: () => import('@/components/Contact')
  },
  {
    path: '/viewer/:project',
    name: 'Viewer',
    component: () => import('@/components/project/Viewer')
  }
  ]
})

// export default new Router({
//   routes: [

//     {
//       path: '/login',
//       name: 'login',
//       component: Login
//     },
//     {
//       path: '/contact',
//       name: 'Contact',
//       component: Contact
//     },
//     {
//       path: '/viewer/:project',
//       name: 'Viewer',
//       component: Viewer
//     },
//     {
//       path: '/regist',
//       name: 'Regist',
//       component: Regist
//     }
//   ]
// })
