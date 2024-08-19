import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";


// https://vitejs.dev/config/
export default defineConfig(({ command }) => {
  return {
    plugins: [
      vue(),
    ],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: `
          @import "./src/styles/theme.scss";
        `,
        },
      },
    },
    server: {
      host: "0.0.0.0",
      hmr: {
        clientPort: 5173,
      },
      port: 5173,
      watch: {
        usePolling: true,
      },
    },
  };
});
