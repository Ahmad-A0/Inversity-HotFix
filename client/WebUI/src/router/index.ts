import {
  createRouter,
  createWebHistory,
} from "vue-router";


const HomeView = () => import("../views/HomeView.vue");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // Homepage
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        requiresRegisteredUser: true,
      },
    },
  ],
});


export { router };
