$(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
	if (status === 'success') {
	    let films = data.results;
	    for (let film in films) {
		$('UL#list_movies').append('<li>' + films[film].title + '</li>');
	    }
	}
    });
});
