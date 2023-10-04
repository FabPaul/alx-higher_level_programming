$(document).ready(function() {
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
		methods: "GET",
		dataType: "json",
		function(data) {
			data.results.forEach(function (movie) {
				$("<li>").text(movie.title).appendTo("UL#list_movies");
			});
		}
	});
});
