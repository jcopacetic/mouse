$(document).ready(function() {
  /** Header Account Dropdown **/

  var accountTrigger = $("header .nav-account");

  accountTrigger.on("click touch", function() {
    if ($(this).hasClass("open")) {
      $(this).removeClass("open");
    } else {
      $(this).addClass("open");
    }
  });
});
