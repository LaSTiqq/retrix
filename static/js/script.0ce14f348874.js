const logo = document.getElementById("logo");
const navbar = document.querySelector(".navbar");
const buttons = document.querySelector(".navbar-nav");

const scrollFunction = () => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // End values
    if (logo && navbar && buttons) {
      logo.style.transform = "scale(0.8) translate(-10%, -2%)";
      navbar.style.height = "80px";
      buttons.style.transform = "translate(-8%, 0)";
    }
  } else {
    // Start values
    if (logo && navbar && buttons) {
      logo.style.transform = "scale(1) translate(0, 0)";
      navbar.style.height = "100px";
      buttons.style.transform = "translate(0, 0)";
    }
  }
};

window.onscroll = () => {
  scrollFunction();
};

// Hide navbar after click
$(".navbar-collapse a").click(function () {
  $(".navbar-collapse").collapse("hide");
});
