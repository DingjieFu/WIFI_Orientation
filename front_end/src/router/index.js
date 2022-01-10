import { createRouter, createWebHashHistory } from 'vue-router'
// import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'indoor-map',
    component: () => import(/* webpackChunkName: "about" */ '../views/indoor_map.vue')
  },
  {
    path: '/室内地图区',
    name: 'indoor-map',
    component: () => import(/* webpackChunkName: "about" */ '../views/indoor_map.vue')
  },
  {
    path: '/指纹可视化区',
    name: 'finger-print-visualize',
    component: () => import(/* webpackChunkName: "about" */ '../views/finger_print_visualize.vue')
  },
  {
    path: '/定位结果区',
    name: 'orientation',
    component: () => import(/* webpackChunkName: "about" */ '../views/orientation.vue')
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
