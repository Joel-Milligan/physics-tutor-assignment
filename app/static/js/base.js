function blurElse() {
  //blur other divs
  $("div.grey_box:not(this)").css("filter", "blur(4px)");
  $("this").css("filter", "blur(0x)");
}

$(document).ready(function () {
  //$(".grey_box").click(blurElse);
});
