new Vue({
  el: "#confirmation",
  data: {
    PopupStatus: false,
  },
  methods: {
    togglePopup() {
      this.PopupStatus = true;
      console.log("clicked on restaurant delete");
    },
    closePopup() {
      this.PopupStatus = false;
    },
    closePopupOutside(event) {
      if (!event.target.closest(".popup-content")) {
        this.closePopup();
      }
    },
  },
});
