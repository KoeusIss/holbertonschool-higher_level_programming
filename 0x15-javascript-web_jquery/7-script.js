const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
window.$.get(apiUrl, function (data) {
  window.$('#character').text(data.name);
});
