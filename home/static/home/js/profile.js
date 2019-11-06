// // ------------------------- PROFILE PAGE ------------------------- // 

// // Retrieve rendered Profile Statistic Dictionaries from template
// var by_test = JSON.parse(document.getElementById('by_test').textContent);
// var by_subject = JSON.parse(document.getElementById('by_subject').textContent);
// var question_info= JSON.parse(document.getElementById('question_info').textContent);


// // --------- Filter By Test Type --------- // 


// // Total Answer Accuracy Pie Chart

// var ctxP = document.getElementById("accuracyPieChart").getContext('2d');
// var myPieChart = new Chart(ctxP, {
//     type: 'pie',
//     data: {
//         labels: ["Correct", "Incorrect"],
//         datasets: [{
//             data: [by_test["questionsCorrect"], by_test["questionsWrong"]],
//             backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)'],
//             borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)']
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });


// // Accuracy Over Time Line Chart

// var ctxL = document.getElementById("improvement").getContext('2d');
// var myLineChart = new Chart(ctxL, {
//     type: 'line',
//     data: {
//         labels: by_test["improvementDates"],
//         datasets: [{
//             label: "% Accuracy at Date",
//             data: by_test["improvementNodes"],
//             backgroundColor: ['rgba(105, 0, 132, .2)',
//             ],
//             borderColor: ['rgba(200, 99, 132, .7)',
//             ],
//             borderWidth: 2
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });


// // Recommendation Bar Chart (Placeholder)

// var ctxP = document.getElementById("recommendationsBar").getContext('2d');
// var myPieChart = new Chart(ctxP, {
//     type: 'bar',
//     data: {
//         labels: ['Math', 'Science', 'Reading'],
//         datasets: [{
//             label: '% recommended study time',
//             data: [40, 10, 50],
//             backgroundColor: ['rgba(105, 0, 132, .2)', 'rgba(0, 137, 132, .2)', 'rgba(255, 99, 132, 0.2)'],
//             borderColor: ['rgba(200, 99, 132, .7)', 'rgba(0, 10, 130, .7)', 'rgba(255,99,132,1)'],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });
