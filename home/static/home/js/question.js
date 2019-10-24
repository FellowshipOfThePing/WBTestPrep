// ----------- QUESTION JS ------------- 

var solved = false;


// Hint Button Click Listener
$("#hintButton").on('click', function(event) {
    if(solved != true) {
        event.preventDefault();
        $("#resultBoxTitle").addClass("text-info");
        $("#resultBoxTitle").text("Hint:")
        $("#hintBox").fadeTo(500, 1);
    }
});


// Submit Button Click Listener
// $("#questionSubmit").on('click', function() {
//     if(solved != true) {
//         checkAnswer();
//     }
// });


// Next Page Button Click Listener. 
// $("#nextPageButton").on('click', function() {
//     if(solved == true) {
//         nextPage();
//     }
// });


// Check if answer is correct or not, return true if correct, false if wrong
function checkAnswer() {
    var radios = $("input")
    var labels = $("label")
    for(var i = 0; i < radios.length; i++){
        if(radios[i].checked) {
            if ($(radios[i]).hasClass("correct")) {
                correct(labels[i]);
                solved = true;
            } else {
                wrong(labels[i]);
            }
        }
    }
}


// Answer is correct, highlight answer label green, change resultBox h4 text to Green "Correct!", fadeTo box
function correct(label) {
    $(label).css("background", "rgba(88, 217, 88, 0.6)");
    $("#resultBoxTitle").css("color", "green");   
    $("#resultBoxTitle").removeClass("text-info");
    $("#resultBoxTitle").text("Correct!");
    $("#resultBoxText").text("");
    $("#resultBox").fadeTo(500, 1);
    // reveal "next question" button that has "href" to next page (PAGINATE)
    $("#nextPageButton").delay(700).fadeTo(500, 1);
}


// Answer is wrong, highlight answer label red, Change resultBox elements, show result box
function wrong(label) {
    $(label).css("background", "rgba(238, 21, 21, 0.52)");
    $("#resultBoxTitle").css("color", "rgba(238, 21, 21, 0.52)"); 
    $("#resultBoxTitle").removeClass("text-info");   
    $("#resultBoxTitle").text("Incorrect: ");
    $("#resultBox").fadeTo(500, 1);
}


// If question is solved, get current url, increment last path element, and redirect
// function nextPage(){
//     var url = window.location.pathname,
//         parts = url.split("/"),
//         questionNum = parts[parts.length-2],
//         newQuestion = Number(questionNum) + 1,
//         url = "http://127.0.0.1:8000/question/" + String(newQuestion);
//         window.location.replace(url);
// }


