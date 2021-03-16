$(document).ready(function () {

    var month = new Array();
    month[0] = "January";
    month[1] = "February";
    month[2] = "March";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";

    $('#i_scheme').addClass('is-invalid');


    $('#i_bank').change(function () {
        $.ajax({
            url: endpoint,
            data: {
                'bank': $(this).val(),
            },
            success: function (data) {
                $('#i_scheme').removeClass('is-invalid');
                d = JSON.parse(data.schemes);

                $('#i_scheme').find('option').remove().end();
                $('#i_scheme').append(new Option('--------------', null, true));
                for (var i = 0; i < d.length; i++) {
                    $('#i_scheme').append(
                        new Option(d[i].fields.scheme, d[i].fields.scheme)
                    )
                }
            }
        });
    })

    $('#i_scheme').change(function () {
        $('#i_time').empty();
        if ($(this).val().includes('(PPF)')) {
            for (var i = 15; i <= 50; i++) {
                $('#i_time').append(
                    new Option(i, i)
                );
            }
        }
        else {
            for (var i = 1; i <= 25; i++) {
                $('#i_time').append(
                    new Option(i, i)
                );
            }
        }
    })
    $('#i_invested_amount').keyup(function () {
        if (parseInt($(this).val()) > sal) {
            $(this).addClass('is-invalid');
        }
        else {
            $(this).removeClass('is-invalid');
        }
    })

    $('#investment_form').change(function () {
        if ($('#i_scheme').val() != null) {
            var t;
            if (parseInt($('#i_time').val()) <= 5) {
                t = 'short';
            }
            else if (parseInt($('#i_time').val()) < 15) {
                t = 'medium';
            }
            else {
                t = 'long';
            }
            $.ajax({
                url: endpoint_int,
                data: {
                    'bank': $('#i_bank').val(),
                    'time': t,
                    'scheme': $('#i_scheme').val(),
                    'principle': $('#i_invested_amount').val(),
                    'fd_time': $('#i_time').val(),
                },
                success: function (data) {
                    var date = new Date();
                    defaultData = [];
                    d = JSON.parse(data.rate);

                    // -------------------------------------- Formula for FD ----------------------------------------- //
                    if (data.is_fd) {
                        var r = parseFloat(d[0].fields.intrest_rate);
                        $('#i_rate').text(r + " %");

                        $('#amt_lbl').text('Monthly Investment');

                        $('#i_maturity_amt').text(data.A + "  Rs.");
                        $('#i_intr_payout').text(parseInt(data.A) - parseInt($('#i_invested_amount').val()) + "  Rs.");
                        defaultData.push(parseInt(data.A) - parseInt($('#i_invested_amount').val()));
                        defaultData.push(parseInt($('#i_invested_amount').val()));

                        date.setFullYear(date.getFullYear() + parseInt($('#i_time').val()));
                        $('#i_maturity_dt').text(month[date.getMonth()] + " " + date.getFullYear());

                        ResetCanvas();
                        myChart(defaultData, "Fixed Deposit");
                    }
                    // -------------------------------------- Formula for RD ----------------------------------------- //
                    if (data.is_rd) {
                        var r = parseFloat(d[0].fields.intrest_rate);
                        $('#i_rate').text(r + " %");

                        $('#amt_lbl').text('Monthly Investment');

                        $('#i_maturity_amt').text(data.A + "  Rs.");
                        $('#i_intr_payout').text(parseInt(data.A) - parseInt($('#i_invested_amount').val()) + "  Rs.");
                        defaultData.push(parseInt(data.A) - parseInt($('#i_invested_amount').val()));
                        defaultData.push(parseInt($('#i_invested_amount').val()));

                        date.setFullYear(date.getFullYear() + parseInt($('#i_time').val()));
                        $('#i_maturity_dt').text(month[date.getMonth()] + " " + date.getFullYear());

                        ResetCanvas();
                        myChart(defaultData, "Recurring Deposit");
                    }
                    // -------------------------------------- Formula for PPF ----------------------------------------- //
                    if (data.is_ppf) {
                        var r = parseFloat(d[0].fields.intrest_rate);
                        $('#i_rate').text(r + " %");

                        $('#amt_lbl').text('Yearly Investment');

                        $('#i_maturity_amt').text(data.A + "  Rs.");
                        $('#i_intr_payout').text(parseInt(data.A) - parseInt($('#i_invested_amount').val()) + "  Rs.");
                        defaultData.push(parseInt(data.A) - parseInt($('#i_invested_amount').val()));
                        defaultData.push(parseInt($('#i_invested_amount').val()));

                        date.setFullYear(date.getFullYear() + parseInt($('#i_time').val()));
                        $('#i_maturity_dt').text(month[date.getMonth()] + " " + date.getFullYear());

                        ResetCanvas();
                        myChart(defaultData, "Public Provident Fund");
                    }
                }
            });
        }
    })

    $('#investment_form').submit(function (e) {
        e.preventDefault();
    })
})

Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

function myChart(field_data, chart_name) {
    // Reseller Pie Chart
    var ctx = $("#scheme_graph");
    var myLineChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Intrest Payout', 'Principle'],
            datasets: [{
                label: chart_name,
                data: field_data,
                backgroundColor: [
                    '#00FF6E',
                    '#00FFF9'
                ],
                hoverBackroundColor: [
                    '14DC6A',
                    '0FE3DE'
                ]
            }],
        },
        options: {
            cutoutPercentage: 55,
            maintainAspectRatio: false,
            title: {
                display: true,
                position: 'top',
                text: chart_name
            },
            layout: {
                padding: {
                    left: 0,
                    right: 0,
                    top: 0,
                    bottom: 0
                }
            },
            legend: {
                display: true,
                position: 'bottom',
                align: 'center',
                labels: {
                    boxWidth: 20,
                }
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

function ResetCanvas() {
    $(`#scheme_graph`).remove();
    $('#canvas_wrapper').append(`<canvas id="scheme_graph"></canvas>`);
}