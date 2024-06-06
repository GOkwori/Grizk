// Mobile navbar collapse
document.addEventListener("DOMContentLoaded", function () {
  var navbarToggler = document.querySelector(".navbar-toggler");
  var pageContent = document.getElementById("page-content");
  var header = document.getElementById("main-header");
  var isNavCollapsed = true;

  navbarToggler.addEventListener("click", function () {
    setTimeout(function () {
      isNavCollapsed = !isNavCollapsed;
      if (!isNavCollapsed) {
        pageContent.style.marginTop = "30%";
      } else {
        pageContent.style.marginTop = "";
      }
    }, 100); // Delay to ensure the collapse animation completes
  });
});
