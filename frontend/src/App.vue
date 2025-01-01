<template>
  <v-app>
    <div class="container">
      <nav><HeaderComponent /></nav>
      <aside><NavigationComponent /></aside>
      <main class="pa-5 bg-surface"><MainComponent /></main>
      <footer class="bg-surface"><FooterComponent /></footer>
    </div>
  </v-app>
</template>

<script>
/* Created header, main, footer, sidebar simultaneously in different views */
import HeaderComponent from "@/components/Header.vue";
import NavigationComponent from "./components/NavigationDrawer.vue";
import MainComponent from "@/components/Main.vue";
import FooterComponent from "@/components/Footer.vue";
import store from "@/store";
import { useTheme } from "vuetify";

export default {
  name: "App",
  components: {
    HeaderComponent,
    MainComponent,
    FooterComponent,
    NavigationComponent,
  },
  data() {
    return {
      theme: useTheme(),
    };
  },
  created() {
    /* 
      Check if there is stored themeMode in  localStorage
      if there is:
        get it's value and change theme appropriately
      if not:
        set new themeMode data to localStorage
        set that themeMode
    */
    if (localStorage.getItem("theme") === "false") {
      this.theme.global.name = "lightMode";
    } else if (localStorage.getItem("theme") === "true") {
      this.theme.global.name = "darkMode";
    } else {
      localStorage.setItem("theme", false);
    }
    if (window.innerWidth >= 992) {
      store.dispatch("updateDrawer", {
        drawer: !this.drawer,
      });
    }
    /* 
      Check if there if user data in cookies
      if true:
        get that data from cookies pass it to vuex storage      
     */
    if (this.$cookies.get("user")) {
      const user = this.$cookies.get("user");
      const password = this.$cookies.get("password");
      store.dispatch("updateUser", {
        user: user,
        password: password,
      });
    }
  },
};
</script>
<style>
body {
  padding: 0px;
  margin: 0px;
}
html {
  scrollbar-width: none;
}
nav {
  grid-area: header;
}
aside {
  grid-area: sidebar;
  z-index: 2000;
}
main {
  grid-area: main;
}
footer {
  grid-area: footer;
}
/* Used media queries for responsive web design */
@media screen and (max-width: 600px) {
  .container {
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto 1fr auto;
    grid-template-areas:
      "header"
      "sidebar"
      "main"
      "footer";
  }
}
@media screen and (min-width: 601px) {
  .container {
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr;
    grid-template-rows: auto auto 1fr auto;
    grid-template-areas:
      "header"
      "sidebar"
      "main"
      "footer";
  }
}
@media screen and (min-width: 992px) {
  .container {
    display: grid;
    grid-template-columns: 250px 1fr;
    grid-template-rows: auto 1fr auto;
    grid-template-areas:
      "header header"
      "sidebar main"
      "sidebar footer";
  }
}
</style>
