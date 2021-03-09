$(document).ready(function () {
    $.ajax({
        url: endpoint,
        success: function (data) {
            defaultData = []
            Labels = []
            hoverColor = []
            backgroundColor = []
            Labels = data.min_x_lbl;
            defaultData = data.min_x;

            for (var i = 0; i < Labels.length; i++) {
                hoverColor.push('#36b9cc');
                backgroundColor.push('#36b9cc');
            }
            SensexChart();
        }
    });
})


Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function SensexChart() {
    // Reseller Pie Chart
    var ctx = document.getElementById("sensex_graph");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Earnings",
                lineTension: 0.3,
                backgroundColor: "rgba(78, 115, 223, 0.05)",
                borderColor: "rgba(78, 115, 223, 1)",
                pointRadius: 0.2,
                pointBackgroundColor: "rgba(78, 115, 223, 1)",
                pointBorderColor: "rgba(78, 115, 223, 1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "rgba(78, 115, 223, 1)",
                pointHoverBorderColor: "rgba(78, 115, 223, 1)",
                pointHitRadius: 10,
                pointBorderWidth: 2,
                data: defaultData,
            }],
        },
        options: {
            maintainAspectRatio: false,
            layout: {
                padding: {
                    left: 10,
                    right: 25,
                    top: 25,
                    bottom: 0
                }
            },
            legend: {
                display: false
            },
            tooltips: {
                backgroundColor: "rgb(0,0,0,0.7)",
                bodyFontColor: "#ffff",
                borderColor: '#dddfeb',
                borderWidth: 1,
                xPadding: 15,
                yPadding: 15,
                displayColors: false,
                caretPadding: 10,
            },
        }
    });
};