$(document).ready(function() {
	$.ajax({
		url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
		methods: "GET",
		dataType: "json",
		function(data) {
			$("DIV#character").text(data.name);
		}
	});
});
