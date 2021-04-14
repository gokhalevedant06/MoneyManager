const monthNames = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

$(document).ready(function () {
    var og_income = parseInt($("#exp_income").text());
    $.ajax({
        url: endpoint,
        success: function (data) {
            for (i = 0; i < data.choice.length; i++) {
                $('#exp_select').append(
                    new Option(data.choice[i][0], data.choice[i][0]),
                );
            }
        }
    })


    $("#exp_select").change(function () {
        if ($(this).val() == "") {
            $("#exp_amt").attr("readonly", true);
        }
        else {
            $("#exp_amt").attr("readonly", false);
        }
    })

    $("#exp_amt").keyup(function () {
        var income = parseInt($("#exp_income").text());
        var expense = parseInt($(this).val());
        if (expense < income) {
            $(this).removeClass("is-invalid text-danger");
            $('#exp_submit').attr("disabled", false);
            $('#exp_submit').removeClass("btn-danger");
            $('#exp_submit').addClass("btn-outline-success");

            if ($("#exp_amt").val() == "") {
                $("#exp_income").text(og_income);
            }
            else {
                $("#exp_income").text(og_income - expense);
            }
        }
        else {
            $(this).addClass("is-invalid text-danger");
            $("#exp_income").text(og_income);
            $('#exp_submit').attr("disabled", true);
            $('#exp_submit').addClass("btn-danger");
            $('#exp_submit').removeClass("btn-outline-success");
        }
    })

    $("#expenses_form").on("submit", function (e) {
        e.preventDefault();
        $.ajax({
            method: 'POST',
            url: endpoint,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                'expense_name': $("#exp_select").val(),
                'expense_amount': parseInt($("#exp_amt").val()),
                'remaining_amount': parseInt($("#exp_income").text()),
            },
            success: function (data) {
                og_income = parseInt($("#exp_income").text());
                d = JSON.parse(data.data);

                $("#expenses_tbl tr").remove();
                for (i = 0; i < d.length; i++) {

                    date = new Date(d[0].fields.time);
                    $("#expenses_tbl").append(
                        `<tr>
                            <td>${monthNames[date.getMonth()] + " " + date.getDate() + ", " + date.getFullYear()}</td>
                            <td>${d[i].fields.expense_name}</td>
                            <td>${d[i].fields.expense_amount}</td>
                            <td>${d[i].fields.remaining_amount}</td>
                        </tr>`
                    )
                }
                $("#expenses_form")[0].reset();
            }
        })
    })
})