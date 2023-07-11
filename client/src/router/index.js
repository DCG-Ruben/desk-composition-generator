import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import Ping from '../components/Ping.vue'
import Office from '../components/Office.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/office',
      name: 'office',
      component: Office
    },
  ]
})

export default router
