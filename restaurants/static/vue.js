new Vue({
  el: '#app',
  data: {
      PopupStatus: false,
  },
  methods: {
      togglePopup() {
          this.PopupStatus = true;
      },
      closePopup() {
          this.PopupStatus = false;
      },
      closePopupOutside(event) {
        if (!event.target.closest('.popup-content')) {
            this.closePopup();
        }
      }
  },
});
