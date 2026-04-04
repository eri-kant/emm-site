import { defineConfig } from 'astro/config';
import tailwind from "@astrojs/tailwind";

// https://astro.build/config
export default defineConfig({
  // Force static output to prevent 502 Gateway errors
  output: 'static',
  
  // Replace with your actual Cloudflare URL later if needed
  site: 'https://emm-site.pages.dev',

  integrations: [tailwind()],
});