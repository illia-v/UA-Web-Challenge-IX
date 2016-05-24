var recognition = new webkitSpeechRecognition(),
    recognizing = false;

recognition.lang = "en-US";
recognition.continuous = true;


recognition.onstart = function () {
    recognizing = true;
    $( "img" ).replaceWith('<img src="/static/pizza/images/microphone1.png">')
};

recognition.onend = function () {
    recognizing = false;
    $( "img" ).replaceWith('<img src="/static/pizza/images/microphone0.png">')
};

recognition.onresult = function (event) {
    for (var i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
            var transcript = event.results[i][0].transcript;
        }
    }
    $("input").val(transcript)
};

$( document ).on("click", "img", function() {
    if (recognizing) {
        recognition.stop();
    } else {
        recognition.start();
    }
});