/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "index.html",
    "sections/**/*.html",
    "sites/**/*.html",
    "build.py",
    "gen.py",
    "gen2.py",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#1a1510",
        stone: "#5c5347",
        paper: "#f5efe6",
        surface: "#fffdf8",
        vermillion: "#a01e14",
        "accent-hover": "#8a1810",
        rule: "#e2d7c8",
        gold: "#b48a4f",
        "tag-green": "#166534",
        "tag-green-bg": "#dcfce7",
        "tag-yellow": "#92400e",
        "tag-yellow-bg": "#fef3c7",
        "tag-orange": "#9a3412",
        "tag-orange-bg": "#ffedd5",
        "tag-red": "#991b1b",
        "tag-red-bg": "#fee2e2",
      },
      fontFamily: {
        display: ['"Cormorant Garamond"', '"Noto Serif SC"', "Georgia", '"Songti SC"', "serif"],
        body: ['"IBM Plex Sans"', '"Noto Sans SC"', "system-ui", "sans-serif"],
        mono: ["IBM Plex Mono", "monospace"],
      },
    },
  },
  plugins: [],
};