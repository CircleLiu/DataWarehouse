import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'homeindex',
    component: () => import('./views/index.vue'),
  },
  {
  
    path: '/graphdata',
    name: 'graphdata',
    component: () => import('./views/graph.vue'),
  }
];

const router = new VueRouter({
  routes
});

export default router;
