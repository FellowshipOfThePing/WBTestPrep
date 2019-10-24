// // ----------- Profile JS ------------- 


// // Statistics Charts

// // https://mdbootstrap.com/docs/jquery/javascript/charts/

// // Right/Wrong Answers
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
