$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
