import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  // This line tells Astro to process your Tailwind CSS
  integrations: [tailwind()],
});