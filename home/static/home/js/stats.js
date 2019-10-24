// ----------- Profile JS ------------- 


// Statistics Charts

// https://mdbootstrap.com/docs/jquery/javascript/charts/

// Right/Wrong Answers
// var accuracy = JSON.parse(document.getElementById('accuracy').textContent);

// var ctxP = document.getElementById("accuracyPieChart").getContext('2d');
// var myPieChart = new Chart(ctxP, {
//     type: 'pie',
//     data: {
//         labels: ["Correct", "Incorrect"],
//         datasets: [{
//             data: [accuracy['correctAnswers'], accuracy['wrongAnswers']],
//             backgroundColor: ["#18c45a", "#F7464A"],
//             hoverBackgroundColor: ["#15d14e", "#FF5A5E"]
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });


// // How many Questions answered from each test
// var subject_distro = JSON.parse(document.getElementById('subject_distribution').textContent);

// var ctxP = document.getElementById("subjectDistroPieChart").getContext('2d');
// var myPieChart = new Chart(ctxP, {
//     type: 'pie',
//     data: {
//         labels: ["Math", "Reading", "Science"],
//         datasets: [{
//             data: [subject_distro["Math_Distro"], subject_distro["Reading_Distro"], subject_distro["Science_Distro"]],
//             backgroundColor: ["#5860a6", "#b02a2a", "#4ec267"],
//             hoverBackgroundColor: ["#7981c7", "#d16464", "#6bd682"]
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });


// // How many Questions answered from each test
// var test_distro = JSON.parse(document.getElementById('test_distribution').textContent);

// var ctxP = document.getElementById("testDistroPieChart").getContext('2d');
// var myPieChart = new Chart(ctxP, {
//     type: 'pie',
//     data: {
//         labels: ["ACT", "SAT", "GRE"],
//         datasets: [{
//             data: [test_distro["ACT_Distro"], test_distro["SAT_Distro"], test_distro["GRE_Distro"]],
//             backgroundColor: ["#4542f5", "#f542cb", "#f5de33"],
//             hoverBackgroundColor: ["#4272f5", "#f069f0", "#ffec61"]
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });




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