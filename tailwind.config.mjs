/** @type {import('tailwindcss').Config} */
import daisyui from "daisyui";

export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      // If you want to use these colors outside of DaisyUI components 
      // (like text-primary), they will now map to your custom theme below.
    },
  },
  plugins: [daisyui],
  daisyui: {
    themes: [
      {
        emm: {
          "primary": "#a3e635",    // Lime Green (Sophisticated)
          "secondary": "#fb923c",  // Neutral Orange (Industrial)
          "accent": "#6ee7b7",     // Soft Emerald
          "neutral": "#1f2937",    // Dark Grey
          "base-100": "#000000",   // True Black Background
          "info": "#3abff8",
          "success": "#36d399",
          "warning": "#fbbd23",
          "error": "#f87272",
          
          // These ensure text colors are readable on your new buttons
          "--rounded-btn": "0rem", // Force sharp, industrial corners
          "--btn-text-case": "uppercase",
        },
      },
    ],
  },
}