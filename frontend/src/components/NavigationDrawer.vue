<template>
  <!-- Used custom transition for my sidebar from vuetify -->
  <v-slide-y-transition>
    <div
      v-show="drawer"
      id="sidebar"
      class="elevation-5 overflow-auto bg-background"
    >
      <v-list dense>
        <v-list-item
          v-for="(item, index) in sidebarItems"
          :key="index"
          :value="item"
          :to="item.url"
          @click="sidebarRoute"
        >
          <v-list-item-title v-text="item.title"></v-list-item-title>
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>
        </v-list-item>
      </v-list>
      <v-divider class="pa-2" v-if="windowWidth > 992"></v-divider>
      <v-expansion-panels
        variant="inset"
        class="pb-10"
        v-if="windowWidth >= 992"
      >
        <v-expansion-panel v-model="panel">
          <v-expansion-panel-title>Users</v-expansion-panel-title>
          <v-expansion-panel-text>
            <v-list>
              <v-list-item
                variant="plain"
                v-for="(item, index) in usersList"
                :key="index"
                :value="item.username"
                append-icon="mdi-arrow-right"
                @click="goToUser(item.username)"
              >
                <v-list-item-title>{{ item.username }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-expansion-panel-text>
        </v-expansion-panel>
      </v-expansion-panels>
    </div>
  </v-slide-y-transition>
</template>
<script>
import { mapState } from "vuex";
import store from "@/store";
import axios from "axios";

export default {
  name: "NavigationComponent",
  data() {
    return {
      USERS_LIST_URL: "http://192.168.1.115:8000/auth/users/all/",
      usersList: null,
      sidebar: true,
      sidebarItems: [
        { title: "Home", url: "/", icon: "mdi-home-outline" },
        { title: "Settings", url: "/settings", icon: "mdi-cog-outline" },
        { title: "Register", url: "/register", icon: "mdi-account-plus" },
        { title: "Login", url: "/login", icon: "mdi-login" },
        { title: "About", url: "/about", icon: "mdi-information-outline" },
      ],
    };
  },
  methods: {
    /* Updating sidebar variable in vuex storage */
    updateSidebar() {
      store.dispatch("updateDrawer", {
        drawer: !this.drawer,
      });
    },
    sidebarRoute() {
      if (this.windowWidth > 992) {
        null;
      } else {
        this.updateSidebar();
      }
    },
    /* Getting users list from backend */
    async getUsers() {
      try {
        const response = await axios.get(this.USERS_LIST_URL);
        if (response.status == 200) {
          this.usersList = response.data;
        }
      } catch (err) {
        console.log(err);
      }
    },
    /* Function that allow us to route to user's statistic pages */
    goToUser(username) {
      this.$router.push({ name: "statistic", params: { username } });
    },
  },
  computed: {
    /* Mapping the  data from vuex storage */
    ...mapState(["drawer"]),
    windowWidth() {
      return this.$vuetify.display.width;
    },
  },
  async mounted() {
    // Getting user list on mounted lifecycle hook,
    // API permission is set to: [AllowAny]
    await this.getUsers();
  },
};
</script>
<style scoped>
/* Media queries for responsive design */
@media screen and (max-width: 600px) {
  #sidebar {
    position: fixed;
    top: 64px;
    width: 100%;
  }
}
@media screen and (max-width: 768px) {
  #sidebar {
    position: fixed;
    top: 64px;
    width: 100%;
  }
}
@media screen and (min-width: 992px) {
  #sidebar {
    position: fixed;
    top: 64px;
    width: 250px;
    height: 100%;
    padding-bottom: 50px;
  }
}
</style>
