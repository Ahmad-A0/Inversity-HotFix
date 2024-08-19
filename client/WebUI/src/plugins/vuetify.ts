// Styles
import "@mdi/font/css/materialdesignicons.css"; // Ensure you are using css-loader
import "vuetify/styles";

// Vuetify
import { createVuetify } from "vuetify";

let components = {};
let directives = {};

/*
In a development environment (ie not static build) we can dynamically import the components and directives
as otherwise each time we load a new page Vite will try to re-optimize the build
*/
components = await import("vuetify/components");
directives = await import("vuetify/directives");

const inversityTheme = {
  dark: false,
  colors: {
    background: "#FFFFFF",
    surface: "#F8F8F8",
    "surface-darken-1": "#F0F0F0",
    primary: "#091B2D",
    secondary: "#C62E65",
    tertiary: "#FF7373",
    error: "#FF7373",
    info: "#2196F3",
    success: "#7FFD94",
    warning: "#e00d11",
    text: "#000000",
    "text-lighten-1": "#171B26",
    "text-lighten-2": "#585C67",
    membership: "#FFD700",
    "gray-100": "#899499",
  },
};

export default createVuetify({
  theme: {
    defaultTheme: "inversityTheme",
    themes: {
      inversityTheme: inversityTheme,
    },
  },
  components: components,
  directives: directives,
  icons: {
    defaultSet: "mdi",
  },
  defaults: {
    VBtn: {
      class: "text-none",
      rounded: true,
    },
  },
});
