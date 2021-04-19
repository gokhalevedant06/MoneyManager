$(document).ready(function () {
    $(".editable").on("dblclick", function () {
        var id = $(this).data("id");
        var value = $(this).text();

        if (id == "name") {
            var input = `<input id="name_inp" class='form-control mb-3 input-data' type='text' value=${value} data-id=${id}/>`;
            var done = "<button class='form-control' type='submit' id='done_btn'>Done</button>";
            $(this).html(input + done);
        }
        else if (id == "email") {
            var input = `<input id="email_inp" class='form-control mb-3 input-data' type='email' value=${value} data-id=${id}/>`;
            var done = "<button class='form-control' type='submit' id='done_btn'>Done</button>";
            $(this).html(input + done);
        }
        else if (id == "income") {
            var input = `<input id="income_inp" class='form-control mb-3 input-data' type='number' value=${value} data-id=${id}/>`;
            var done = "<button class='form-control' type='submit' id='done_btn'>Done</button>";
            $(this).html(input + done);
        }
        else if (id == "profession") {
            var input = `<select class="form-control input-data" id="prof_inp" name="profession" required></select>`;
            profession();
            var done = "<button class='form-control' type='submit' id='done_btn'>Done</button>";
            $(this).html(input + done);
        }
    })
    $(document).on('click', "#done_btn", function () {
        var parent = $(this).parent('div');
        var id = parent.data('id');
        if (id == "name") {
            var value = $("#name_inp").val();
            $("#name_inp").remove();
        }
        else if (id == "email") {
            var value = $("#email_inp").val();
            $("#email_inp").remove();
        }
        else if (id == "income") {
            var value = $("#income_inp").val();
            $("#income_inp").remove();
        }
        else if (id == "profession") {
            var value = $("#prof_inp").val();
            $("#prof_inp").remove();
        }
        else {
            var value = 'error';
        }
        $(this).remove();
        parent.html(value);
        parent.addClass("editable");
        sendData(value, id);
    })
    $(document).on('blur', '.input-data', function () {
        var value = $(this).val();
        var parent = $(this).parent('div');
        var id = parent.data('id');
        $(this).remove();
        parent.html(value);
        parent.addClass('editable');
        sendData(value, id);
    });

    $(document).on('keypress', '.input-data', function (e) {
        var key = e.which;
        if (key == 13) {
            var value = $(this).val();
            var parent = $(this).parent('div');
            var id = parent.data('id');
            parent.html(value);
            parent.addClass('editable');
            sendData(value, id);
        };
    });
})


function profession() {
    $.ajax({
        type: 'GET',
        url: endpoint,
        success: function (data) {
            prf = []

            d = JSON.parse(data);
            for (i = 0; i < d.length; i++) {
                if (d[i].fields.field === "profession") {
                    prf.push(d[i].fields.value);
                }
            }
            $('#prof_inp').append(new Option("-------", null, true))
            for (i = 0; i < prf.length; i++) {
                $('#prof_inp').append(
                    new Option(prf[i], prf[i])
                );
            }
        },
    })
}

function sendData(value, id) {
    $.ajax({
        url: endpoint,
        type: 'POST',
        data: {
            value: value,
            id: id,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
        },
        success: function (data) {
            console.log(data)
        }
    })
}