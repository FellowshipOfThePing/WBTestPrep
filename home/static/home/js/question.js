// ----------- QUESTION PAGE JS -------------


// TODO: Refactor


// Track if user has current question on display
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