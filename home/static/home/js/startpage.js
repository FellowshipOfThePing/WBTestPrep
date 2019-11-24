// ----------- HOMEPAGE JS ------------- //

// TODO: Refactor checkId method to access text dictionary instead of iterating through strings


// HTML Content for blurbs
var aboutText = "We are a small group of passionate educators and programmers, dedicating our time and effort towards providing quality tools to help students all over the country.";
var linksText = "Here are some links to supplemental study material";
var contactText = "To report a problem with the site or inquire about other matters please contact us using the following information:";
var legalText = "The information contained on WBTestPrep.com and any publications or study materials created by the author of WBTestPrep.com is for informational purposes only. They are to be used to study and review for the ACT, SAT, or GRE. Exam content review, methods of study, tips and sample questions are only recommendations from the author, and reading any information on WBTestPrep.com and any publications or other study materials created by the author does not guarantee passing any of the aforementioned exams. The author has made reasonable efforts to provide current and accurate information. The author will not be held liable for any unintentional errors or omissions that may be found.";



// Open Page 2
$("#start").on('click', function(event) {
    event.preventDefault();
    $("#jumbo1").fadeOut(400, function() {
        $("#jumbo1").remove();
        $("#page2").fadeTo(400, 1);
    });
});



// Bottow Row Transition Animation
$(".customPill").on('click', function(event) {
    event.preventDefault();

    // deactivate all pills
    deactivateAll();

    // activate selected pill
    $(this).addClass("current");

    // fade out title and text, change each mid fade
    var id = checkId($(this).attr("id"));
    $("#title").fadeOut(150, function() {
        $("#title").text(id[0]);
    });
    $("#text").fadeOut(150, function() {
        $("#text").text(id[1]);
    });

    // fade back in
    $("#title").fadeIn();
    $("#text").fadeIn();
});



// Deactivate All Pills
function deactivateAll() {
    $.each($(".customPill"), function() {
        $(this).removeClass("current");
    });
}



// Return id of Selected pill
function checkId(id) {
    if(id === "about") {
        return ["About Us", aboutText];
    }
    else if(id === "links") {
        return ["Links", linksText];
    }
    else if(id === "contact") {
        return ["Contact", contactText];
    }
    else if(id === "legal") {
        return ["Legal", legalText];
    }
}
