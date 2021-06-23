$(document).ready(function () {
    var diff = null;
    var interval = null;

    $('#nifty_tab').click(function () {
        loader();
        diff = 1;
        interval = '1m';
        $.ajax({
            url: endpoint_nifty,
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
                $('#sen_header').text("Today's NIFTY")
                NiftyChartToday();
                $("#nifty_graph_today").show();
                $("#nifty_graph_week").hide();
                $("#nifty_graph_year").hide();
                $("#nifty_graph_ten_years").hide();
            }
        });
    })

    $('#nifty_today').click(function () {
        loader();
        diff = 1;
        interval = '1m';

        $.ajax({
            url: endpoint_nifty,
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
                $('#sen_header').text("Today's NIFTY")
                NiftyChartToday();
                $("#nifty_graph_today").show();
                $("#nifty_graph_week").hide();
                $("#nifty_graph_year").hide();
                $("#nifty_graph_ten_years").hide();
            }
        });
    });

    $('#nifty_week').click(function () {
        loader();
        diff = 7;
        interval = '30m';

        $.ajax({
            url: endpoint_nifty,
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
                $('#sen_header').text("This Week's NIFTY")
                NiftyChartWeek();
                $("#nifty_graph_today").hide();
                $("#nifty_graph_week").show();
                $("#nifty_graph_year").hide();
                $("#nifty_graph_ten_years").hide();
            }
        });
    });

    $('#nifty_year').click(function () {
        loader();
        diff = 365;
        interval = '1wk';
        $.ajax({
            url: endpoint_nifty,
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
                $('#sen_header').text("This Year's NIFTY")
                NiftyChartYear();
                $("#nifty_graph_today").hide();
                $("#nifty_graph_week").hide();
                $("#nifty_graph_year").show();
                $("#nifty_graph_ten_years").hide();
            }
        });
    });

    $('#nifty_ten_years').click(function () {
        loader();
        diff = 3650;
        interval = '1mo';
        $.ajax({
            url: endpoint_nifty,
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
                $('#sen_header').text("Last 10 years NIFTY")
                NiftyChartTenYears();
                $("#nifty_graph_today").hide();
                $("#nifty_graph_week").hide();
                $("#nifty_graph_year").hide();
                $("#nifty_graph_ten_years").show();
            }
        });
    });
})


Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function NiftyChartToday() {
    // Reseller Pie Chart
    var ctx = document.getElementById("nifty_graph_today");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Nifty",
                lineTension: 0.3,
                backgroundColor: "rgba(74 ,232, 13, 0.1)",
                borderColor: "#56F319",
                pointRadius: 0.2,
                pointBackgroundColor: "#56F319",
                pointBorderColor: "#56F319",
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
function NiftyChartWeek() {
    // Reseller Pie Chart
    var ctx = document.getElementById("nifty_graph_week");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Nifty",
                lineTension: 0.3,
                backgroundColor: "rgba(74 ,232, 13, 0.1)",
                borderColor: "#56F319",
                pointRadius: 0.2,
                pointBackgroundColor: "#56F319",
                pointBorderColor: "#56F319",
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
function NiftyChartYear() {
    // Reseller Pie Chart
    var ctx = document.getElementById("nifty_graph_year");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Nifty",
                lineTension: 0.3,
                backgroundColor: "rgba(74 ,232, 13, 0.1)",
                borderColor: "#56F319",
                pointRadius: 0.2,
                pointBackgroundColor: "#56F319",
                pointBorderColor: "#56F319",
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
function NiftyChartTenYears() {
    // Reseller Pie Chart
    var ctx = document.getElementById("nifty_graph_ten_years");
    var myLineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: Labels,
            datasets: [{
                label: "Nifty",
                lineTension: 0.3,
                backgroundColor: "rgba(74 ,232, 13, 0.1)",
                borderColor: "#56F319",
                pointRadius: 0.2,
                pointBackgroundColor: "#56F319",
                pointBorderColor: "#56F319",
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