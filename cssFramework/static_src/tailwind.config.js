
module.exports = {
    content: [

        '../templates/**/*.html',


        '../../templates/**/*.html',

        '../../**/templates/**/*.html',


    ],
    theme: {
      screens:{
        'mobile': '450px',
          },
        extend: {
          
          animation: {
            'slide-in': 'slide-in 0.75s ease-out',
            'fade-in': 'fade-in 0.5s ease',
            'popup': 'popup 0.5s ease',
          },
          keyframes: {
            'slide-in': {
              '0%': { transform: 'translateY(80%)' },
              '100%': { transform: 'translateY(0)' },
            },
            'popup': {
              '0%': { transform: 'translateY(100%)' },
              '100%': { transform: 'translateY(0)' },
            },
            
            'fade-in': {
              '0%': { opacity: '0' },
              '100%': { opacity: '1' },
            },
          },
            colors: {
              'main1': '#e0e0e0',
              'main1-t': '#F5F5F5DD',
              'main5': '#1F1F1F',
              'main5-t': '#1F1F1FDD',
              'main4': '#4A4A4A',
              'main4-t100': '#4A4A4A40',
              'main4-t': '#4A4A4ADD',
              'main2': '#C78F38',
              'main2-t': '#C78F38DD',
              'main3': '#007B6B',
              'main3-t': '#007B6BDD',
              'main3-t100': '#007B6B40',

              'rows' : '#F5F5F573',
              }
        },
    },
    plugins: [
        require("tailwindcss-animation-delay"),
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
