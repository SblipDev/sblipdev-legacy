import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Posts from "../views/Posts.vue";
import Post from "../views/Post.vue";
import Contact from "../views/Contact.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/blogs",
    name: "Post",
    component: Posts,
  },
  {
    path: "/contact",
    name: "contact",
    component: Contact,
  },
  {
    path: "/blog/:slug",
    name: "postd",
    component: Post,
    props: true,
  },
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
