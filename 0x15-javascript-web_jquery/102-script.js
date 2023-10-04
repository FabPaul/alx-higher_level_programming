$(document).ready(function() {
	$("INPUT#btn_translate").click(function() {
		const languageCode = $("INPUT#language_code").val();

		$.ajax({
			url: `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`,
			method: "GET",
			dataType: "json",
			function(data) {
				$("DIV#hello").text(data.hello);
			}
		});
	});
});
