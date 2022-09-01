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

// Captcha
$(".captcha").click(function () {
  $.getJSON("/captcha/refresh/", function (result) {
    $(".captcha").attr("src", result["image_url"]);
    $("#id_captcha_0").val(result["key"]);
  });
});

// Hide navbar after click
$(".navbar-collapse a").click(function () {
  $(".navbar-collapse").collapse("hide");
});
