const logo = document.getElementById("logo");

const scrollFunction = () => {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    // End values
    if (logo) {
      logo.style.width = "130px";
      logo.style.height = "70px";
    }
  } else {
    // Start values
    if (logo) {
      logo.style.width = "170px";
      logo.style.height = "90px";
    }
  }
};

window.onscroll = () => {
  scrollFunction();
};

// Hide navbar after click when navbar collapsed
const navbarLinks = document.querySelectorAll(".navbar-collapse a");

navbarLinks.forEach((link) => {
  link.addEventListener("click", () => {
    const navbarCollapse = document.querySelector(".navbar-collapse");
    if (navbarCollapse.classList.contains("show")) {
      navbarCollapse.classList.remove("show");
    }
  });
});

// Loader to slow speed connection
window.onload = () => {
  const images = document.getElementsByTagName("img");
  const loader = document.querySelector(".loader-container");
  const content = document.querySelector(".wrapper");
  let loaded = 0;

  for (let i = 0; i < images.length; i++) {
    if (images[i].complete) {
      loaded++;
    }
  }

  if (loaded == images.length) {
    loader.style.display = "none";
    content.style.display = "flex";
  }
};
