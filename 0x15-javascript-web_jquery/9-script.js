$(document).ready(function() {
	$.ajax({
		url: "https://fourtonfish.com/hellosalut/?lang=fr",
		methods: "GET",
		dataType: "json",
		function(data) {
			$("DIV#hello").text(data.hello);
		}
	});
});
