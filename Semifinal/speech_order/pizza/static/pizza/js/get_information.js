var baseForm = '<form><img src="/static/pizza/images/microphone0.png">' +
    '<input type="text" id="data-input">' +
    '<button id="submit" type="submit">Enter</button></form>';
var integerForm = '<form><img src="/static/pizza/images/microphone0.png">' +
    '<input type="number" id="data-input" min="0" step="1">' +
    '<button id="submit" type="submit">Enter</button>' + '</form>';
var dateForm = '<form>' +
    '<input id="data-input" class="datetimepicker" type="text" >' +
    '<button id="submit" type="submit">Enter</button>' + '</form>';

var dataNames = [
    "Name",
    "Phone number",
    "Pizza",
    "Drink",
    "Pizzeria",
    "Address",
    "Method of payment",
    "Date of delivery"
];

var paymentMethodButtons = '<button class="payment" id="cash">cash</button>' +
    '<button class="payment" id="terminal">terminal</button>';
var yesNoButtons = '<form><button id="yes" type="submit">Yes</button>' +
    '<button id="no">No, rewrite</button></form>';
var confirmButtons = '<form><button id="good" type="submit">Everything is good</button>' +
    '<a href="/pizza"><button id="bad">There is an error</button></a></form>';
var warningPizzerias = "<small>Note: if the pizzeria is not supported, " +
    "your order will be sent to Our Pizzeria!</small>"

var dataToHtml = "";
var dataToServer = [];

var csrfToken = $( 'input[name="csrfmiddlewaretoken"]' ).val();

var dateTime = /\d\d\d\d\/\d\d\/\d\d \d\d:\d\d/;

var actionNumber = 0;


var question = function (dataName) {
    if (dataName !== "Date of delivery") {
        return "<h3>Enter your " + dataName.toLowerCase() + ":</h3>"
    } else {
        return "<h3>Enter the date when you prefer to get this order:</h3>"
    }
};

var checkingText = function (dataName, data) {
    return "Is your " + dataName.toLowerCase() + " <em>" + data + "</em>?";
};

var rightForm = function (actionNumber) {
    return (actionNumber === 1) ? integerForm :
           (actionNumber === 4) ? warningPizzerias + baseForm :
           (actionNumber === 6) ? paymentMethodButtons :
           (actionNumber === 7) ? dateForm:
           baseForm;
};

var rightSection = function (actionNumber) {
    return $( "section" ).html(
        "<div>" +
        question(dataNames[actionNumber]) +
        '<div id="input">' + rightForm(actionNumber) + "</div>" +
        "</div>" +
        '<div id="data-block">' + dataToHtml + "</div>"
    );
};

var DTPicker = function () {
    if (actionNumber === 7) {
            return $( ".datetimepicker" ).datetimepicker({
                minDate: 0
            });
        }
};


$( document ).keydown(function(event) {
    if (event.keyCode == 13) {
        $( 'button[type="submit"]' ).click();
    }
});


window.onbeforeunload = function () {
    if (actionNumber > 0 && actionNumber !== 7) {
        return "Are you sure? Order data will be lost!";
    }
};


$( document ).on("click", "#submit", function (e) {
    e.preventDefault();

    window.data = $("#data-input").val();

    recognition.stop();
    recognizing = false;

    if (window.data.length !== 0) {
        if (actionNumber !== 7 || dateTime.test(window.data)) {
            window.dataName = dataNames[actionNumber];
            $( "section" ).html(
                "<h3>" + checkingText(window.dataName, window.data) +
                "</h3>" + yesNoButtons
            );
        } else {
            $( "#input" ).html(
                rightForm(actionNumber) +
                "<p><small>Data in the field must look like " +
                "'<b>year/month/day hour:minute</b>' !</small></p>"
            );
            DTPicker()
        }
    } else {
        $( "#input" ).html(
            rightForm(actionNumber) +
            "<p><small>The field must not be empty!</small></p>"
        );
        DTPicker()
    }
});


$( document ).on("click", "#yes", function (e) {
    e.preventDefault();

    if (actionNumber === 0) {
        dataToHtml += "<h3>Your information:</h3>"
    }

    dataToHtml += "<em>" + window.dataName + ":</em> " + window.data + "<br>";
    dataToServer.push(window.data);

    if (actionNumber <= 6) {
        ++actionNumber;
        rightSection(actionNumber);
        DTPicker()
    } else {
        $( "section" ).html(
            '<div id="data-block">' + dataToHtml + "</div>" +
            confirmButtons
        );
    }
});


$( document ).on("click", "#no", function (e) {
    e.preventDefault();
    rightSection(actionNumber);
    DTPicker()
});


$( document ).on("click", ".payment", function (e) {
    e.preventDefault();

    window.data = $( this ).text();
    window.dataName = dataNames[actionNumber];

    $( "section" ).html(
        "<h3>" + checkingText(window.dataName, window.data) + "</h3>" +
        yesNoButtons
    )
});


$( document ).on("click", "#good", function (e) {
    e.preventDefault();

    $.ajax({
        type: "POST",
        url: "/pizza/",
        data: {
            name: dataToServer[0],
            phone_number: dataToServer[1],
            pizza: dataToServer[2],
            drink: dataToServer[3],
            pizzeria: dataToServer[4],
            address: dataToServer[5],
            payment_method: dataToServer[6],
            delivery_date: dataToServer[7],
            csrfmiddlewaretoken: csrfToken
        },
        success: function (json) {
            window.location.replace("/pizza/orders/" + json["slug"]);
        },
        error: function () {
            window.location.replace("/pizza/error/");
        }
    })
});