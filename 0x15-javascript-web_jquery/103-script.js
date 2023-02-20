$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    sayHello();
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      sayHello();
    }
  });
});

function sayHello () {
  const lan = $('INPUT#language_code').val();
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
