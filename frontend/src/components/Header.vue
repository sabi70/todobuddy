<template>
  <v-app-bar app fixed :elevation="3" class="bg-info">
    <v-app-bar-nav-icon
      @click="updateSidebar"
      :icon="drawer ? 'mdi-close' : 'mdi-menu'"
      v-if="windowWidth < 992"
    ></v-app-bar-nav-icon>
    <v-app-bar-title class="text-center" v-if="windowWidth < 992">
      todo
    </v-app-bar-title>
    <v-container v-if="windowWidth >= 992">
      <v-row>
        <v-col>
          <div id="logo-container">
            <img :src="require('@/assets/aim.png')" id="logo" />
            <h1>todo</h1>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <template v-slot:append>
      <v-divider vertical color="white"></v-divider>
      <v-btn
        variant="outlined"
        color="success_button"
        append-icon="mdi-account-plus"
        class="ml-3 mr-2"
        v-if="windowWidth > 992"
        to="register"
      >
        Sign-in
      </v-btn>
      <v-btn
        variant="outlined"
        color="success_button"
        append-icon="mdi-login"
        class="ml-3 mr-2"
        to="login"
      >
        Login
      </v-btn>
    </template>
  </v-app-bar>
</template>
<script>
import store from "@/store";
import { mapState } from "vuex";

export default {
  name: "HeaderComponent",
  components: {},
  data() {
    return {};
  },
  methods: {
    updateSidebar() {
      store.dispatch("updateDrawer", {
        drawer: !this.drawer,
      });
    },
  },
  computed: {
    ...mapState(["drawer"]),
    windowWidth() {
      return this.$vuetify.display.width;
    },
  },
};
</script>
<style>
#logo-container {
  display: flex;
  align-items: center;
}
#logo {
  width: 50px;
  margin-right: 10px;
  border-radius: 50px;
  background-image: linear-gradient(to right, #8360c3, #2ebf91);
}
</style>
