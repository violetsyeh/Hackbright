"use strict";


// PART 1: SHOW A FORTUNE

function showFortune(results) {

    // TODO: get the fortune and show it in the #fortune-text div
    $('#fortune-text').html(results);
	
}
function getFortune(){
	$.get('/fortune', showFortune)
}

$('#get-fortune-button').on('click', getFortune);




// PART 2: SHOW WEATHER
function showWeather(results){
	console.dir(results);
	alert("Today's forecast is: " + results['forecast']);
}


function getWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};


    // TODO: request weather with that URL and show the forecast in #weather-info
    $.get(url, formData, showWeather);

}


$("#weather-form").on('submit', getWeather);




// PART 3: ORDER MELONS

function showOrderResults(result){
	$('#order-status').html(result['msg']);
	console.log("Finished showOrderResults");
	console.log(result['code'])
}

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    // TODO: if the result code is ERROR, make it show up in red (see our CSS!)

    let formInputs = {
    	"qty": $("#qty-field").val(),
    	"melon_type": $("#melon-type-field").val(),
    };

    $.post('/order-melons.json',formInputs,showOrderResults);
}


$("#order-form").on('submit', orderMelons);


