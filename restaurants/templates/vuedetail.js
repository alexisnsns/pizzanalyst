new Vue({
  el: "#app",
  delimiters: ["${", "}"],
  data: {
    isAnimated: false,
    PopupCommentStatus: false,
  },
  computed: {
    buttonText() {
      return this.isAnimated ? "Hide Comments" : "Display Comments";
    },
  },
  methods: {
    toggleAnimation() {
      this.isAnimated = !this.isAnimated;
    },
    togglePopupComment() {
      this.PopupCommentStatus = true;
    },
    closePopupComment() {
      this.PopupCommentStatus = false;
    },
    closePopupCommentOutside(event) {
      if (!event.target.closest(".popup-comment-content")) {
        this.closePopupComment();
      }
    },
  },
});
