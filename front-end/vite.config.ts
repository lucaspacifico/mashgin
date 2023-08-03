import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
  resolve: { alias: { "@": "/src" } },
  plugins: [react()],
  server: {
    host: true,
    port: 8080,
  },
});
