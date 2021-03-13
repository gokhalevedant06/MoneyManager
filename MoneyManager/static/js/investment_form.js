$(document).ready(function () {
    $('#i_scheme').addClass('is-invalid');
    for (var i = 1; i <= 25; i++) {
        $('#i_time').append(
            new Option(i, i)
        );
    }

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
            else if (parseInt($('#i_time').val()) <= 15) {
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
                    defaultData = [];
                    d = JSON.parse(data.rate);
                    var r = parseFloat(d[0].fields.intrest_rate);
                    $('#i_rate').text(r + " %");

                    $('#i_maturity_amt').text(data.A + "  Rs.");
                    $('#i_intr_payout').text(parseInt(data.A) - parseInt($('#i_invested_amount').val()) + "  Rs.");
                    defaultData.push(parseInt(data.A) - parseInt($('#i_invested_amount').val()));
                    defaultData.push(parseInt(parseInt($('#i_invested_amount').val())));
                    ResetCanvas();
                    FdChart();
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

function FdChart() {
    // Reseller Pie Chart
    var ctx = $("#fd_graph");
    var myLineChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Intrest Payout', 'Principle'],
            datasets: [{
                label: "Fixed Deposit",
                data: defaultData,
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
            cutoutPercentage: 60,
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

function ResetCanvas() {
    $('#fd_graph').remove();
    $('#fd_canvas_wrapper').append('<canvas id="fd_graph"></canvas>');
}