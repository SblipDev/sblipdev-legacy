<template>
  <div class="post-page">
    <div class="container">
      <h2>Blogs by me:</h2>
      <br />
      <div id="retainable-rss-embed" 
data-rss="https://medium.com/feed/@sblip"
data-maxcols="2" 
data-layout="grid" 
data-poststyle="inline" 
data-readmore="Read more.." 
data-buttonclass="btn btn-light" 
data-offset="-100"></div>
  <script src="https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js" type="application/javascript"></script>

    </div>
  </div>
</template>

<script>
// import Vue from 'vue';
// Vue.loadScript("https://www.twilik.com/assets/retainable/rss-embed/retainable-rss-embed.js")

export default {
  name: "Posts",
  data() {
    return {
      posts: null,
    };
  },
  methods: {
   
  },
  created() {
  },
};
</script>

<style>
.post {
  min-height: 150px;
  width: 102%;
  border: 3px solid white;
  margin-bottom: 15px;
  border-radius: 5px;
  padding: 10px;

}
.post-page {
  min-height: 100vh;
  background: black;
  padding-top: 100px;
  color: white;
  background: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260")
    fixed;
  background-repeat: no-repeat;
  background-size: cover;
}
.atag{
  color:white;
}

.atag:hover{
  text-decoration: underline;
  color:white;
}
</style>