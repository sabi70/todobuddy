// Styles
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";
// Custom light theme
const lightMode = {
  dark: false,
  colors: {
    background: "#FFFBE6",
    surface: "#FFFBE6",
    primary: "#3f51b5",
    secondary: "#03dac6",
    error: "#f44336",
    info: "#2196F3",
    success: "#4caf50",
    warning: "#fb8c00",
    success_button: "#FFFBE6",
  },
};
// Custom dark theme
const darkMode = {
  dark: false,
  colors: {
    background: "#121212",
    surface: "#1e1e1e",
    primary: "#bb86fc",
    secondary: "#03dac6",
    error: "#cf6679",
    info: "#1e1e1e",
    success: "#4caf50",
    warning: "#ffb300",
    success_button: "#4caf50",
  },
};

export default createVuetify({
  theme: {
    defaultTheme: "lightMode",
    themes: {
      lightMode,
      darkMode,
    },
  },
});
// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
