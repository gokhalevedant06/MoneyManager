$(document).ready(function () {
    loader();
    callToday = ajaxCall(SensexChartToday, "#sensex_graph_today", 1, "1m");
    
    $('#sen_today').click(function () {
        loader();
        ajaxCall(SensexChartToday, "#sensex_graph_today", 1, "1m");
    });

    $('#sen_week').click(function () {
        loader();
        ajaxCall(SensexChartWeek, "#sensex_graph_week", 7, '30m');
    });

    $('#sen_year').click(function () {
        loader();
        ajaxCall(SensexChartYear, "#sensex_graph_year", 365, "1wk");
    });

    $('#sen_ten_years').click(function () {
        loader();
        ajaxCall(SensexChartTenYears, "#sensex_graph_ten_years", 3650, "1mo");
    });
})


Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function SensexChartToday() {
    // Reseller Pie Chart
    var ctx = document.getElementById("sensex_graph_today");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Sensex",
                lineTension: 0.3,
                backgroundColor: "rgba(78, 115, 223, 0.1)",
                borderColor: "rgba(78, 115, 223, 1)",
                pointRadius: 0.2,
                pointBackgroundColor: "rgba(78, 115, 223, 1)",
                pointBorderColor: "rgba(78, 115, 223, 1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "#F80A0A",
                pointHoverBorderColor: "#ffff",
                pointHitRadius: 25,
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
function SensexChartWeek() {
    // Reseller Pie Chart
    var ctx = document.getElementById("sensex_graph_week");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Sensex",
                lineTension: 0.3,
                backgroundColor: "rgba(78, 115, 223, 0.1)",
                borderColor: "rgba(78, 115, 223, 1)",
                pointRadius: 0.2,
                pointBackgroundColor: "rgba(78, 115, 223, 1)",
                pointBorderColor: "rgba(78, 115, 223, 1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "#F80A0A",
                pointHoverBorderColor: "#ffff",
                pointHitRadius: 25,
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
function SensexChartYear() {
    // Reseller Pie Chart
    var ctx = document.getElementById("sensex_graph_year");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Sensex",
                lineTension: 0.3,
                backgroundColor: "rgba(78, 115, 223, 0.1)",
                borderColor: "rgba(78, 115, 223, 1)",
                pointRadius: 0.2,
                pointBackgroundColor: "rgba(78, 115, 223, 1)",
                pointBorderColor: "rgba(78, 115, 223, 1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "#F80A0A",
                pointHoverBorderColor: "#ffff",
                pointHitRadius: 25,
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
function SensexChartTenYears() {
    // Reseller Pie Chart
    var ctx = document.getElementById("sensex_graph_ten_years");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Sensex",
                lineTension: 0.3,
                backgroundColor: "rgba(78, 115, 223, 0.1)",
                borderColor: "rgba(78, 115, 223, 1)",
                pointRadius: 0.2,
                pointBackgroundColor: "rgba(78, 115, 223, 1)",
                pointBorderColor: "rgba(78, 115, 223, 1)",
                pointHoverRadius: 3,
                pointHoverBackgroundColor: "#F80A0A",
                pointHoverBorderColor: "#ffff",
                pointHitRadius: 25,
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

function loader() {
    $('#loader').show();
}

function ajaxCall(fn, chart_name, diff, interval) {
    $.ajax({
        url: endpoint,
        data: {
            'diff': diff,
            'interval': interval,
        },
        success: function (data) {
            console.log(data)
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
            $('#loader').hide();
            $('#sen_header').text("This Week's Sensex")
            fn();
            $("#sensex_graph_today").hide();
            $("#sensex_graph_week").hide();
            $("#sensex_graph_year").hide();
            $("#sensex_graph_ten_years").hide();
            $(chart_name).show();
        }
    });
}