document.addEventListener("DOMContentLoaded", function () {
  let countrySelected = $("#id_default_country").val();
  if (!countrySelected) {
    $("#id_default_country").css("color", "#050f1a");
  }
  $("#id_default_country").change(function () {
    countrySelected = $(this).val();
    if (!countrySelected) {
      $(this).css("color", "#050f1a);
    } else {
      $(this).css("color", "#000");
    }
  });
});
