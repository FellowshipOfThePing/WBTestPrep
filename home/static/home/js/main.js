// ----------- Central JS Aggregate - Currently Only used for Reference ------------- //


// ----------- HOMEPAGE JS ------------- 

// HTML Content for blurbs
var aboutText = "I just wanna help out!";
var linksText = "Add something here later about links";
var contactText = "Contact stuff";
var legalText = "The information contained on HTMLPrep.com and any publications or study materials created by the author of HTMLPrep.com is for informational purposes only. They are to be used to study and review for the ACT, SAT, or GRE. Exam content review, methods of study, tips and sample questions are only recommendations from the author, and reading any information on HTMLPrep.com and any publications or other study materials created by the author does not guarantee passing any of the aforementioned exams. The author has made reasonable efforts to provide current and accurate information. The author will not be held liable for any unintentional errors or omissions that may be found.";


// Open Homepage
$("#start").on('click', function(event) {
    event.preventDefault();
    $("#jumbo1").fadeOut(400, function() {
        $("#jumbo1").remove();
        $("#page2").fadeTo(400, 1);
    });
});


// Fade out blurb, change html, change active state, fade in
$(".pill").on('click', function(event) {
    event.preventDefault();

    // deactivate all pills
    deactivateAll();

    // activate THIS one
    $(this).addClass("active");

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


// Shut off all menu pills before reactivating selected one
function deactivateAll() {
    $.each($(".pill"), function() {
        $(this).removeClass("active");
    });
}


// Return id of selected pill
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





// ----------- Profile JS ------------- 


// Statistics Charts

// https://mdbootstrap.com/docs/jquery/javascript/charts/

// Right/Wrong Answers
var accuracy = JSON.parse(document.getElementById('accuracy').textContent);

var ctxP = document.getElementById("accuracyPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["Correct", "Incorrect"],
        datasets: [{
            data: [accuracy['correctAnswers'], accuracy['wrongAnswers']],
            backgroundColor: ["#18c45a", "#F7464A"],
            hoverBackgroundColor: ["#15d14e", "#FF5A5E"]
        }]
    },
    options: {
        responsive: true
    }
});


// How many Questions answered from each test
var subject_distro = JSON.parse(document.getElementById('subject_distribution').textContent);

var ctxP = document.getElementById("subjectDistroPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["Math", "Reading", "Science"],
        datasets: [{
            data: [subject_distro["Math_Distro"], subject_distro["Reading_Distro"], subject_distro["Science_Distro"]],
            backgroundColor: ["#5860a6", "#b02a2a", "#4ec267"],
            hoverBackgroundColor: ["#7981c7", "#d16464", "#6bd682"]
        }]
    },
    options: {
        responsive: true
    }
});


// How many Questions answered from each test
var test_distro = JSON.parse(document.getElementById('test_distribution').textContent);

var ctxP = document.getElementById("testDistroPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["ACT", "SAT", "GRE"],
        datasets: [{
            data: [test_distro["ACT_Distro"], test_distro["SAT_Distro"], test_distro["GRE_Distro"]],
            backgroundColor: ["#4542f5", "#f542cb", "#f5de33"],
            hoverBackgroundColor: ["#4272f5", "#f069f0", "#ffec61"]
        }]
    },
    options: {
        responsive: true
    }
});





// ------------------------- STATS PAGE ------------------------- // 


// --------------- FILTER BY TEST TYPE --------------- // 

// Right/Wrong Answers

var ctxP = document.getElementById("accuracyPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["Correct", "Incorrect"],
        datasets: [{
            data: [12, 15],
            backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)'],
            borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)']
        }]
    },
    options: {
        responsive: true
    }
});


// How many Questions answered from each test

var ctxP = document.getElementById("subjectDistroPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'bar',
    data: {
        labels: ["Math", "Reading", "Science"],
        datasets: [{
            label: '# of Questions Answered',
            data: [15, 4, 22],
            backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)', 'rgba(255, 99, 132, 0.2)'],
            borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)', 'rgba(255,99,132,1)'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});


// How many Questions answered from each test

var ctxP = document.getElementById("testDistroPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'radar',
    data: {
        labels: ["ACT", "SAT", "GRE"],
        datasets: [{
            label: "# of Questions Answered",
            data: [22, 42, 15],
            backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)'],
            borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)']
        }]
    },
    options: {
        responsive: true
    }
});




// --------------- FILTER BY TEST TYPE --------------- // 


// Accuracy Over Time Line Chart
var ctxL = document.getElementById("accuracyOverTimeChart").getContext('2d');
var myLineChart = new Chart(ctxL, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "My First dataset",
            data: [65, 59, 80, 81, 56, 55, 40],
            backgroundColor: ['rgba(105, 0, 132, .2)',
            ],
            borderColor: ['rgba(200, 99, 132, .7)',
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true
    }
});


// Total Accuracy Pie Chart
var ctxP = document.getElementById("totalAccuracyPieChart").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'pie',
    data: {
        labels: ["Correct", "Incorrect"],
        datasets: [{
            data: [300, 50],
            backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)'],
            borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)']
        }]
    },
    options: {
        responsive: true
    }
});


// Recommendation Bar Chart
var ctxP = document.getElementById("recommendations").getContext('2d');
var myPieChart = new Chart(ctxP, {
    type: 'bar',
    data: {
        labels: ["Math", "Reading", "Science"],
        datasets: [{
            label: '% recommended study time',
            data: [40, 10, 50],
            backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)', 'rgba(255, 99, 132, 0.2)'],
            borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)', 'rgba(255,99,132,1)'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});