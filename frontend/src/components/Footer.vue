<template>
  <v-footer class="bg-info mt-10">
    <v-container>
      <v-row no-gutters>
        <v-col>
          <div id="logo-container" class="pr-15">
            <img :src="require('@/assets/aim.png')" id="logo" />
            <h1>todo</h1>
          </div>
        </v-col>
        <v-col class="d-flex flex-column">
          <router-link
            v-for="link in pageLinks"
            :key="link"
            :to="link.url"
            class="text-uppercase text-start"
            id="footer-links"
          >
            {{ link.title }}
          </router-link>
        </v-col>
        <v-col v-if="windowWidth >= 992">
          <v-container class="d-flex align-content-start flex-wrap pt-0 pl-0">
            <img
              v-for="badge in badgeList"
              :key="badge"
              :src="badge"
              @contextmenu.prevent
              @mousedown.prevent
            />
          </v-container>
        </v-col>
      </v-row>
      <v-row>
        <p class="text-center w-100 pt-5">django-vue project 2024</p>
      </v-row>
      <v-row>
        <p class="w-100 text-center text-subtitle-1 text-decoration-underline">
          sabi_co
        </p>
      </v-row>
    </v-container>
  </v-footer>
</template>
<script>
export default {
  name: "FooterComponent",
  data() {
    return {
      smIcons: ["mdi-gmail", "mdi-github", "mdi-reddit", "mdi-instagram"],
      pageLinks: [
        { title: "Home", url: "/" },
        { title: "Settings", url: "/settings" },
        { title: "Register", url: "/register" },
        { title: "Login", url: "/login" },
        { title: "Statistic", url: "/statistic/sabi" },
        { title: "About", url: "/about" },
      ],
      badgeList: [
        "https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green",
        "https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white",
        "https://img.shields.io/badge/axios-671ddf?&style=for-the-badge&logo=axios&logoColor=white",
        "https://img.shields.io/badge/Vue%20js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D",
        "https://img.shields.io/badge/Vuetify-1867C0?style=for-the-badge&logo=vuetify&logoColor=white",
        "https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white",
        "https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white",
        "https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E",
        "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue",
        "https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white",
        "https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white",
        "https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black",
        "https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white",
      ],
    };
  },
  computed: {
    windowWidth() {
      return this.$vuetify.display.width;
    },
  },
};
</script>
<style scoped>
#logo-container {
  display: flex;
  align-items: center;
}
#footer-links {
  font-weight: 300;
  font-size: 18px;
}
#footer-links:hover {
  transition: 0.2s;
  text-decoration: underline;
  font-size: 20px;
  font-weight: 500;
}
a {
  text-decoration: none;
}
a:link {
  color: white;
}
a:visited {
  color: white;
}
a:active {
  color: white;
  text-decoration: underline;
  font-size: 20px;
  font-weight: 500;
}
</style>
