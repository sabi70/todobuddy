<template>
  <v-card>
    <v-card-text>
      <v-switch
        inset
        label="Toggle between light and dark theme."
        v-model="darkMode"
        @change="changeTheme"
        color="success"
      >
      </v-switch>
    </v-card-text>
  </v-card>
</template>
<script>
// Used vuetify useTheme for dark and light theme mode switching;
import { useTheme } from "vuetify";

export default {
  name: "SettingsView",
  data() {
    return {
      theme: useTheme(),
      darkMode: false,
    };
  },
  methods: {
    // dark-light theme switcher method
    changeTheme() {
      this.theme.global.name = this.darkMode ? "darkMode" : "lightMode";
      localStorage.setItem("theme", this.darkMode);
    },
  },
  created() {
    // Checking themeMode's value from localStorage on created
    // lifecycle hook and changing themeMode appropriately:
    if (localStorage.getItem("theme") === "true") {
      this.darkMode = true;
    } else {
      this.darkMode = false;
    }
  },
};
</script>
