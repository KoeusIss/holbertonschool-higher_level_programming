window.$('#toggle_header').click(function () {
  if (window.$('HEADER').hasClass('green')) {
    window.$('HEADER').addClass('red').removeClass('green');
  } else {
    window.$('HEADER').addClass('green').removeClass('red');
  }
});
