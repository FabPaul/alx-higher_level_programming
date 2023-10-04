const $my_header = $("header")

const $DIVRed_header = $("DIV#red_header")

$DIVRed_header.on("click", function () {
  $my_header.css("color", "#FF0000");
});
