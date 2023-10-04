$(document).ready(function() {
	function fetchTranslation() {
		const languageCode = $("INPUT#language_code").val();

		$.ajax({
			url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`,
			method: "GET",
			dataType: "json",
			function(data) {
				$("DIV#hello").text(data.hello);
			},
		});
	}

	$("INPUT#btn_translate").click(fetchTranslation);
	$("INPUT#language_code").keypress(function(event) {
		// 13 , becuase it is the code for "ENTER" on most jeyboards
		if (event.which === 13) {
			fetchTranslation();
		}
	});
});
