import { createRouter, createWebHistory } from 'vue-router'
import Office from '../components/Office.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'office',
      component: Office
    },
  ]
})

export default router
