const apiUrl = 'https://fourtonfish.com/hellosalut/?lang=fr';
window.$.get(apiUrl, function (data) {
  window.$('#hello').text(data.hello);
});
