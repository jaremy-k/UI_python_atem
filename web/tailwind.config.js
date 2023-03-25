module.exports = {
    content: ["./src/**/*.{html,js,php}"],
    theme: {
      extend: {},
    },
    plugins: [
      require('@tailwindcss/typography'),
      require('@tailwindcss/aspect-ratio'),
    ],
}