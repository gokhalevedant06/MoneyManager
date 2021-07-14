$(document).ready(function () {


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
            $('#i_time').val(15);
        }
        if ($(this).val().includes('(NSC)')) {
            $('#i_time').val(5);
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
                    defaultData = [];
                    d = JSON.parse(data.rate);

                    // -------------------------------------- Formula for FD ----------------------------------------- //
                    if (data.is_fd) {

                        formChangeHndler(d[0].fields.intrest_rate, data.A);
                        iTimeHandler(false, $("#i_time").val());
                        $('#amt_lbl').text('Monthly Investment');

                    }

                    // -------------------------------------- Formula for RD ----------------------------------------- //
                    if (data.is_rd) {

                        formChangeHndler(d[0].fields.intrest_rate, data.A);
                        iTimeHandler(false, $("#i_time").val());
                    }

                    // -------------------------------------- Formula for PPF ----------------------------------------- //
                    if (data.is_ppf) {

                        formChangeHndler(d[0].fields.intrest_rate, data.A);
                        iTimeHandler(false, $("#i_time").val(), 15, 40);
                    }

                    // -------------------------------------- Formula for NSC ----------------------------------------- //
                    if (data.is_nsc) {

                        formChangeHndler(d[0].fields.intrest_rate, data.A);

                        iTimeHandler(true, 5, 1, 5);

                    }

                    // -------------------------------------- Formula for MIS ----------------------------------------- //
                    if (data.is_mis) {

                        formChangeHndler(d[0].fields.intrest_rate, data.A);
                        $('#amt_lbl').text('Monthly Investment');
                        iTimeHandler(false, $("#i_time").val());
                    }
                }
            });
        }
    })

    $('#investment_form').submit(function (e) {
        e.preventDefault();
        $.ajax({
            method: 'post',
            url: endpoint,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'bank': $('#i_bank').val(),
                'time': $("#i_time").val(),
                'scheme': $('#i_scheme').val(),
                'principle': $('#i_invested_amount').val(),
                'fd_time': $('#i_time').val(),
                'intr_payout': parseInt($('#i_intr_payout').text()),
            },
            success: function (data) {
                if (data.success) {
                    $('#resultModalContent').html(
                        `<div class="modal-header text-success">
                            <h5 class="modal-title">Success !</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <table class="table">
                                <thead>
                                    <tr class="table-success">
                                        <th>Fields</th>
                                        <th>Data</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Bank Name</td>
                                        <td>${$('#i_bank').val()}</td>
                                    </tr>
                                    <tr>
                                        <td>Investment Scheme</td>
                                        <td>${$('#i_scheme').val()}</td>
                                    </tr>
                                    <tr>
                                        <td>Monthly Investment</td>
                                        <td>${$("#i_invested_amount").val()}</td>
                                    </tr>
                                    <tr>
                                        <td>Timespan</td>
                                        <td>${$("#i_time").val()}</td>
                                    </tr>
                                    <tr>
                                        <td>Intrest Payout</td>
                                        <td>${$("#i_intr_payout").text()}</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div class="modal-footer border border-none">
                            <button id="modalBtn" type="button" class="btn btn-outline-success" data-dismiss="modal" onclick="resetForm();">Ok</button>
                        </div>
                        `
                    )
                    $('#investible_amt').text(`Investable ammount: ${data.updated_income}`);
                }
                else {
                    $('#resultModalContent').html(
                        `<div class="modal-header text-danger">
                            <h5 class="modal-title">Error ! Something went Wrong</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            Please check if you have filled all the fields
                        </div>
                        <div class="modal-footer">
                            <button id="modalBtn" type="button" class="btn btn-outline-danger" data-dismiss="modal">Ok</button>
                        </div>
                        `
                    )
                }
            }
        });
    })
})

function resetForm() {
    // Reset the form
    $('#investment_form').trigger('reset');
    $('#i_time').val(1);
    $('#i_time_value').text("Value: 1 year");

    //Reset the Canvas
    ResetCanvas();

    // Reset the table
    $("#i_rate").text("");
    $("#i_maturity_amt").text("");
    $("#i_intr_payout").text("");
    $("#i_maturity_dt").text("");
}

function iTimeHandler(state, value = 1, min = 1, max = 25) {
    if (value === 1) {
        $("#i_time_container").html(`
    <input type="range" class="col custom-range" id="i_time" min="${min}" max="${max}" value="${value}">
    <output for="i_time" onforminput="value = i_time.value;"></output>
    <div id="i_time_value" class="col-sm-3 mt-1">Value: ${value} year</div>
    `);
    }
    else {
        $("#i_time_container").html(`
    <input type="range" class="col custom-range" id="i_time" min="${min}" max="${max}" value="${value}">
    <output for="i_time" onforminput="value = i_time.value;"></output>
    <div id="i_time_value" class="col-sm-3 mt-1">Value: ${value} years</div>
    `);
    }

    $("#i_time").prop("disabled", state);
    $("#i_time").tooltip();
}

function formChangeHndler(intrest, total) {

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

    var date = new Date();
    var r = parseFloat(intrest);

    $('#i_rate').text(r + " %");
    $('#amt_lbl').text('Yearly Investment');

    $('#i_maturity_amt').text(total + "  Rs.");
    $('#i_intr_payout').text(parseInt(total) - parseInt($('#i_invested_amount').val()) + "  Rs.");
    defaultData.push(parseInt(total) - parseInt($('#i_invested_amount').val()));
    defaultData.push(parseInt($('#i_invested_amount').val()));

    date.setFullYear(date.getFullYear() + parseInt($('#i_time').val()));
    $('#i_maturity_dt').text(month[date.getMonth()] + " " + date.getFullYear());

    ResetCanvas();
    myChart(defaultData, "National Savings Certificate");
}

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