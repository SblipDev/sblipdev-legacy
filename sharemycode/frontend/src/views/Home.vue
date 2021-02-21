<template>
  <div class="home">
    <div class="middle">
        <img src="@/assets/avatar-min.jpg" alt="" class='avatar'><br /><br>
      <h1 class="font-weight-bold" style="font-family: 'Yusei Magic', sans-serif;">Shaurya Pratap Singh</h1>
      <p class="font-weight-bold">Coder, Student, Geek and a <strike>flat</strike> globe earther. </p>
      <a href="https://codepen.io/shaurya-blip" target="_blank"><i class="fab fa-codepen facon"></i></a>
      <a href="https://github.com/shaurya-blip/" target="_blank"><i class="fab fa-github facon"></i></a>
      <a href="https://create.arduino.cc/projecthub/shauryapsingh21" target="_blank"><i class="fas fa-microchip facon"></i></a>
      <a href="https://sblip.medium.com/" target="_blank"><i class="fab fa-medium-m facon"></i></a>
      <a href="https://sblip.dev"><i class="fas fa-wifi facon" target="_blank"></i></a>
    </div>
  </div>
</template>
<script>
// @ is an alias to /src
// import Vue from 'vue'


export default {
  name: "Home",
  data() {
    return {
      error:'hello!'
    };
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Yusei+Magic&display=swap');
.home {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background: black;
  color: white;
  text-align: center;
  background-image: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260");
}
.avatar {
  border-radius: 10%;
  height: 415px;
  width: 190px;
  background:url('https://shauryaservo.pythonanywhere.com/static/avatar-min.jpg');
  background-size:180px 190px;
  border-top: 20px solid white;
  border-bottom: 17px solid white;
}
.facon {
  font-size: 30px;
  padding: 10px;
  transition: all 0.3s;
  color:white;
}
.facon:hover {
  background-color: white;
  color:black;
  padding: 15px;
}


</style>
