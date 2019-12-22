import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import Index from "../views/index.vue";

Vue.use(VueRouter);

const route = [
  {
    path: '/',
    name: 'homeindex',
    component: Index,
  },
  {
  
    path: '/graphdata',
    name: 'graphdata',
    component: () => import('../views/graph.vue'),
  }
];

const router = new VueRouter({
  routes: route
});

export default router;
