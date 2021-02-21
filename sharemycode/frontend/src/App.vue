<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg fixed-top py-3">
      <div class="container">
        <a
          href="/"
          class="navbar-brand text-uppercase font-weight-bold"
          style="font-size: 30px"
          >Shaurya Pratap Singh</a
        >
        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="fa fa-bars icon"></i>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto">
            <li class="nav-item">
              <a
                href="/"
                class="nav-link middle text-uppercase font-weight-bold"
                >Home</a
              >
            </li>
            <li class="nav-item">
              <a
                href="/about/"
                class="nav-link text-uppercase middle font-weight-bold"
                >About</a
              >
            </li>
            <li class="nav-item">
              <a
                href="/blogs/"
                class="nav-link text-uppercase middle font-weight-bold"
                >Blogs</a
              >
            </li>
            <li class="nav-item">
              <a
                href="/contact/"
                class="nav-link text-uppercase middle font-weight-bold"
                >Contact</a
              >
            </li>
           
              <li class='nav-item' style='color:white;' v-if="user_info.is_authenticated"><a href="/accounts/logout/"  class="nav-link text-uppercase middle font-weight-bold">Logout</a></li>
              <li class='nav-item text-uppercase middle font-weight-bold nav-link' style='color:white;' v-if="user_info.is_authenticated">Welcome back {{ user.username }}!</li>
              <li class="nav-item" v-else>
              <!-- <a
                href="/accounts/register/"
                class="nav-link text-uppercase middle font-weight-bold"
                >Sign up for Newsletter</a
              > -->
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view />
    <div class="footer"></div>
  </div>
</template>
<script
  src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
  integrity="sha256-4+XzXVhsDmqanXGHaHvgh1gMQKX40OUvDEBTu8JcmNs="
  crossorigin="anonymous"></script>
<script>
import { apiService } from "@/common/api.service.js";
import $ from "jquery";
$(function () {
  $(window).on("scroll", function () {
    if ($(window).scrollTop() > 10) {
      $(".navbar").addClass("active");
    } else {
      $(".navbar").removeClass("active");
    }
  });
});
export default {
  name: "App",
  data(){
    return{
      user_info:null,
      user:null,
    }
  },
  methods: {
    getUserAuth() {
      let endpoint = "/api/info-user/";
      apiService(endpoint).then((data) => {
        this.user_info = data;
      });
    },
    getUserDetails() {
      let endpoint = "/api/rest-auth/user/";
      apiService(endpoint).then((data) => {
        this.user = data;
      });
    },
    setUserInfo() {
      // add the username of the logged in user to localStorage
      const requestUser = user["username"];
      window.localStorage.setItem("username", requestUser);
    }
    },

  created() {
    this.getUserAuth();
    this.getUserDetails()
    this.setUserInfo();
  },
};
</script>
<style>
.navbar {
  transition: all 0.5s;
  opacity: 0.9;
}

.navbar .nav-link {
  color: white;
  opacity: 1;
}

.navbar .nav-link:hover,
.navbar .nav-link:focus {
  color: white;
  text-decoration: none;
}
.navbar .navbar-brand {
  color: white;
}

hr.style-seven {
    height: 5px;
    border: 0;
    box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);
}
/* Change navbar styling on scroll */
.navbar.active {
  background: #fafafa;
}

.navbar.active .nav-link {
  background-color: rgb(117, 117, 117);
}

.navbar.active .nav-link:hover {
  background-color: black;
}

.navbar.active .navbar-brand {
  color: black;
}
a.middle::after {
  content: "";
  width: 0;
  height: 2px;
  background: white;
  display: block;
  margin: auto;
  transition: 0.5s;
}
a.middle:hover::after {
  width: 100%;
}
.navbar.active a.middle::after {
  content: "";
  width: 0;
  height: 2px;
  background: white;
  display: block;
  margin: auto;
  transition: 0.5s;
}
.navbar.active a.middle:hover::after {
  width: 100%;
}

.icon {
  color: white;
}
.navbar.active .icon {
  color: black;
}

@media only screen and (max-width: 768px) {
  a.middle {
    text-decoration: none;
  }
  .masthead-heading {
    /* Layout Declarations */
    color: white;
    margin-top: -0.2em;
    /* Typography Declarations */
    font-family: "Open Sans", "Helvetica Neue", sans-serif;
    font-weight: bold;
    font-size: 3em;
    letter-spacing: -0.02em;
    text-transform: uppercase;
  }
  .navbar.nav-link {
  background-color: rgb(117, 117, 117);
}
}
#app{
  background: black;
}
pre{
  background:white;
  padding:4px;
  border-radius:2px;
}
</style>
