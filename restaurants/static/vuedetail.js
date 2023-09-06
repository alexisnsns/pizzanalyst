new Vue({
  el: '#app',
  delimiters: ['${', '}'], 
  data: {
      isAnimated: false,
  },
  computed: {
    buttonText() {
        return this.isAnimated ? 'Hide Comments' : 'Display Comments';
    },
},
  methods: {
      toggleAnimation() {
          this.isAnimated = !this.isAnimated;
      },
  },
});
