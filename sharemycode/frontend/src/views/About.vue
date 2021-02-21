<template>
  <div class="about">

    <header class="masthead">
      <p class="masthead-intro">Hi I'm</p>
      <h1 class="masthead-heading">Shaurya Pratap Singh</h1>
    </header>
    <section class="introduction-section">
      <h1>Who am I?</h1>
      <p>
        I am a computer hobbyist, a student, a guitarist, a hard core harry
        potter fan and a massive star wars geek.
      </p>
      <p>I am also a species of human you may call a 'geek'.</p>
    </section>
    <section class="location-section">
      <h1>What do I know?</h1>
      <p>Here is a list of technologies, I know -></p>
      <ul>
        <li>Language: Python <i class="fab fa-python"></i></li>
        <li>Backend Framework: Django</li>
        <li>JavaScript Framework: Vue <i class="fab fa-vuejs"></i></li>
        <li>Frontend languages: html, css and js</li>
        <li>SQL: PostgreSQL <i class="fas fa-database"></i></li>
        <li>Data Science libraries: 
          <ul>
            <li>Numpy</li>
            <li>Pandas</li>
            <li>SKlearn</li>
            <li>Matplotlib</li>
            <li>Seaborn</li>
            <li>Plot.ly</li>
            <li>Tensorflow</li>
            <li>Keras</li>
          </ul>
        </li>
      </ul>
    </section>
    <section class="location-section">
      <h1>Where I'm From</h1>
      <p>I'm originally from New Delhi, India</p>
    </section>
    <section class="questions-section d">
      <h1>More About Me</h1>
      <h2>What are your favorite hobbies?</h2>
      <p>My favorite hobbies are coding, reading, and cycling etc.</p>
      <h2>Whats your dream?</h2>
      <p>Meeting and talking to Elon Musk, world peace, and that humanity becomes interplanetary.</p>
      <h2>What's your dream job?</h2>
      <p>My dream job is to work at spacex as the software guy.</p>
      <h2>Where do you live?</h2>
      <p>I live in an apartment in gurugram.</p>
      <h2>Why do you want to be a programer?</h2>
      <p>
        Because programming is awesome and programming for the internet is even
        more awesome.
      </p>
    

    </section>
  </div>
</template>
<script>

export default {
  name: "About",
};
</script>
<style>
.about {
  min-height: 102vh;
  background: black;
  padding-top: 200px;
  color: white;
  background: url("https://images.pexels.com/photos/2387793/pexels-photo-2387793.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260");
  background-repeat: no-repeat;
  background-size: cover;
  padding: 100px;
}
.content-footer,
.masthead-heading,
.masthead-intro {
  text-align: center;
}

.masthead {
  border-top: solid 1em #ffcf33;
}

.masthead-intro {
  /* Layout Declarations */
  margin-bottom: 0.1em;
  /* Typography Declarations */
  font-family: "Gentium Book Basic", Georgia, serif;
  font-size: 2em;
}

.masthead-heading {
  /* Layout Declarations */
  color: white;
  margin-top: -0.2em;
  /* Typography Declarations */
  font-family: "Open Sans", "Helvetica Neue", sans-serif;
  /* font-weight: bold; */
  font-size: 6em;
  /* letter-spacing: -0.02em; */
  text-transform: uppercase;
}



.introduction-section > p,
.location-section > p,
.questions-section,
.content-footer > p {
  /* Typography Declarations */
  font-weight: 300;
  letter-spacing: 0.05em;
}

.questions-section > h2 {
  font-family: "Gentium Book Basic", Georgia, serif;
  font-size: 1.2em;
  font-weight: bold;
  /* Layout */
  margin: 2em 0 1em 0;
}

section > h1 {
  margin-top: 2em;
}

.masthead-heading,
.masthead-intro {
  text-align: center;
}

.masthead {
  padding: 6em 0;
  border-top: solid 1em white;
}

.introduction > p,
.location > p,
.content-footer > p {
  /* Typography Declarations */
  font-weight: 300;
  letter-spacing: 0.05em;
}
.d h2 {
  /* Typography Declarations */
  font-family: "Gentium Book Basic", Georgia, serif;
  font-size: 1.2em;
  font-weight: bold;
}

.introduction-section,
.location-section,
.questions-section {
  max-width: 38em;
  margin-left: 20em;
  margin-right: 20em;
  margin-top: 2em;
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
    font-size: 4em;
    letter-spacing: -0.02em;
    text-transform: uppercase;
  }
  .introduction-section,
.location-section,
.questions-section {
  max-width: 38em;
  margin-left: 1em;
  margin-right: 1em;
  margin-top: 2em;
}
}

</style>