$("label:contains('Relative')").html("Neyin?")
$("span:contains('First')").html("İlk üyesi")
$('option[value="first-child"]').text("İlk üyesi")
$('option[value="left"]').text("Önce")
$('option[value="right"]').text("Sonra")
$('label[for="id_description"]').html("Açıklama")
$('label[for="id_is_public"]').remove()
$("span.help-block:contains('Birden')").remove()
$("td:contains('True')").html("Evet")
$("td:contains('False')").html("Hayır")
$('option[value="0"]').text("Kök")