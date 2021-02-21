<template>
  <div class='postdetail-page'>
    <!-- <div class='half-page'>
      <h1 class="font-weight-bold" style="font-family: 'Yusei Magic', sans-serif;">Shaurya Pratap Singh</h1>
      <p class="font-weight-bold">Coder, Student, Geek and a <strike>flat</strike> globe earther. </p>
    </div><br><br> -->
    <div class="container">
      <div class="content">
        <h2>{{ post.title }}</h2>
        <p>Posted on: {{ post.created_at }} | Loves: {{ post.loves_count }}</p>
        <hr><br>
        <div v-html='post.body'></div>
        <br><br>
        <!-- <h3>Comments</h3><br>
         <span v-for="comment in replies" :key="comment.pk">
           <div class='comment'>
             <br>
             <div v-html="comment.body"></div><hr>
             <p>By: {{ comment.author }} | Commented on: {{ comment.created_at }} | Likes: {{ comment.loves_count }}</p>
           </div>
         </span><br> -->
    </div><br>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
    name:'Post',
    props: {
      slug: {
        type: String,
        required: true
      }
    },
    data(){
      return {
        post:{},
        requestUser:null,
        replies:null
      }
    },
    methods:{
      getPostData() {
        let endpoint = "/api/posts/" + this.slug + "/";
        apiService(endpoint)
          .then(data => {
            if (data) {
              this.post = data;
            } 
          })
      },
      setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    getPostReplies() {
      let endpoint = `/api/posts/${this.slug}/replies/`;
      apiService(endpoint)
        .then(data => {
          this.replies = data;
        })
    },
    },
    created() {
      this.getPostData();
      this.setRequestUser();
      this.getPostReplies();
    }
}
</script>

<style>
.postdetail-page {
  min-height: 100vh;
  background: black;
  color: white;
  padding-top:90px;
  background: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260") fixed;
}
/* .half-page{
  display: flex;
  align-items: center;
  justify-content: center;
  width:80vh;
  height:100vh;
  background:black;
  position:fixed;
  margin-right:45px;
  padding:20px;
}
@media only screen and (max-width: 1400px) {
  .half-page {
    display: none;
  }
  .postdetail-page{

  }
} */
.content{
  background:white;
  min-height:800px;
  color:black;
  padding:10px;
  border-radius:1px 15px 15px 15px;
}
.comment{
  border:3px solid black;
  border-radius:5px;
  padding:5px;
}
</style>