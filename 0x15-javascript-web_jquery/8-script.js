const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
window.$.get(apiUrl, function (data) {
  window.$.each(data.results, function (index, movie) {
    window.$('#list_movies').append(`<li>${movie.title}</li>`);
  });
});
