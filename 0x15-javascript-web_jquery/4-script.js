$(document).ready(function() {
    $("DIV#toggle_header").click(function() {
      const $my_header = $("header");
      
      if ($my_header.hasClass("red")) {
        $my_header.removeClass("red").addClass("green");
      } else if ($my_header.hasClass("green")) {
        $my_header.removeClass("green").addClass("red");
      } else {
        $my_header.addClass("red");
      }
    });
  });
