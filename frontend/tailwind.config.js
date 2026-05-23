/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,ts}",
    "./src/app/auth/login/login.html"
  ],
  theme: {
    extend: {
      colors: {
        'ibus-blue': '#081E37',
        'ibus-light-blue': '#175AA5',
        'ibus-bg-blue': '#D1DEED',
        'ibus-yellow': '#F9B233',
        'ibus-gray': '#D9D9D9',
        'ibus-text-gray': '#6C6C6C',
        'ibus-red': '#FFB9B9',
        'ibus-dark-red': '#AF0000',
      },
      fontFamily: {
        barlow: ['Barlow', 'sans-serif'],
        roboto: ['Roboto', 'sans-serif'],
        inter: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
