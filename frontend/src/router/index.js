import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/students',
      name: 'students',
      component: () => import('../views/StudentListView.vue')
    },
    {
      path: '/students/create',
      name: 'student-create',
      component: () => import('../views/StudentCreateView.vue')
    },
    {
      path: '/students/:id/edit',
      name: 'student-edit',
      component: () => import('../views/StudentEditView.vue'),
      props: true
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('../views/NotFoundView.vue')
    }
  ],
  
  // 滾動行為
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

export default router