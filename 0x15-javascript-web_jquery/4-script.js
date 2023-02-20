$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ($('header').hasClass('red')) {
      $('header').toggleClass('red');
      $('header').addClass('green');
    } else {
      $('header').toggleClass('green');
      $('header').addClass('red');
    }
  });
});
