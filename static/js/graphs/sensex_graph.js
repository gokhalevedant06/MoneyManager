$(document).ready(function () {
    loader();

    var diff = 1;
    var interval = '1m';

    $.ajax({
        url: endpoint,
        data: {
            'diff': diff,
            'interval': interval,
        },
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
            $('#loader').hide();
            $('#sen_header').text("Today's Sensex")
            SensexChartToday();
            $("#sensex_graph_today").show();
            $("#sensex_graph_week").hide();
            $("#sensex_graph_year").hide();
            $("#sensex_graph_ten_years").hide();
        }
    });

    $('#sen_today').click(function () {
        loader();
        diff = 1;
        interval = '1m';

        $.ajax({
            url: endpoint,
            data: {
                'diff': diff,
                'interval': interval,
            },
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
                $('#loader').hide();
                $('#sen_header').text("Today's Sensex")
                SensexChartToday();
                $("#sensex_graph_today").show();
                $("#sensex_graph_week").hide();
                $("#sensex_graph_year").hide();
                $("#sensex_graph_ten_years").hide();
            }
        });
    });

    $('#sen_week').click(function () {
        loader();
        diff = 7;
        interval = '30m';

        $.ajax({
            url: endpoint,
            data: {
                'diff': diff,
                'interval': interval,
            },
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
                $('#loader').hide();
                $('#sen_header').text("This Week's Sensex")
                SensexChartWeek();
                $("#sensex_graph_today").hide();
                $("#sensex_graph_week").show();
                $("#sensex_graph_year").hide();
                $("#sensex_graph_ten_years").hide();
            }
        });
    });

    $('#sen_year').click(function () {
        loader();
        diff = 365;
        interval = '1wk';
        $.ajax({
            url: endpoint,
            data: {
                'diff': diff,
                'interval': interval,
            },
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
                $('#loader').hide();
                $('#sen_header').text("This Year's Sensex")
                SensexChartYear();
                $("#sensex_graph_today").hide();
                $("#sensex_graph_week").hide();
                $("#sensex_graph_year").show();
                $("#sensex_graph_ten_years").hide();
            }
        });
    });

    $('#sen_ten_years').click(function () {
        loader();
        diff = 3650;
        interval = '1mo';
        $.ajax({
            url: endpoint,
            data: {
                'diff': diff,
                'interval': interval,
            },
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
                $('#loader').hide();
                $('#sen_header').text("Last 10 years Sensex")
                SensexChartTenYears();
                $("#sensex_graph_today").hide();
                $("#sensex_graph_week").hide();
                $("#sensex_graph_year").hide();
                $("#sensex_graph_ten_years").show();
            }
        });
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