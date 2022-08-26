window.onscroll = function () {
  scrollFunction();
};

const logo = document.getElementById("logo");

function scrollFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // End values
    if (logo) {
      logo.style.width = "110px";
      logo.style.height = "60px";
    }
  } else {
    // Start values
    if (logo) {
      logo.style.width = "160px";
      logo.style.height = "80px";
    }
  }
}