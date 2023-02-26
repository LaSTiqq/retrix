const logo = document.getElementById("logo");

const scrollFunction = () => {
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
};

window.onscroll = () => {
  scrollFunction();
};

// Hide navbar after click
$(".navbar-collapse a").click(function () {
  $(".navbar-collapse").collapse("hide");
});
