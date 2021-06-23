$(document).ready(function () {
    $('#r_username').keyup(function () {
        $.ajax({
            url: endpoint,
            data: {
                'username': $('#r_username').val(),
            },
            success: function (data) {
                if (data.username_exists) {
                    $('#r_username').addClass('is-invalid');
                    $('#r_btn').attr('disabled', true);
                }
                else {
                    $('#r_username').removeClass('is-invalid');
                    $('#r_btn').attr('disabled', false);
                }
            }
        });
    });

    $('#r_email').keyup(function () {
        $.ajax({
            url: endpoint,
            data: {
                'email': $('#r_email').val(),
            },
            success: function (data) {
                if (data.email_exists) {
                    $('#r_email').addClass('is-invalid');
                    $('#r_btn').attr('disabled', true);
                }
                else {
                    $('#r_email').removeClass('is-invalid');
                    $('#r_btn').attr('disabled', false);
                }
            }
        });
    });

    $('#r_password').keyup(function () {
        if ($(this).val() !== $('#r_confirm_password').val()) {
            $(this).addClass('is-invalid');
            $('#r_confirm_password').addClass('is-invalid');
            $('#r_btn').attr('disabled', true);
        }
        else {
            $(this).removeClass('is-invalid');
            $('#r_confirm_password').removeClass('is-invalid');
            $('#r_btn').attr('disabled', false);
        }
    })

    $('#r_confirm_password').keyup(function () {
        if ($(this).val() !== $('#r_password').val()) {
            $(this).addClass('is-invalid');
            $('#r_password').addClass('is-invalid');
            $('#r_btn').attr('disabled', true);
        }
        else {
            $(this).removeClass('is-invalid');
            $('#r_password').removeClass('is-invalid');
            $('#r_btn').attr('disabled', false);
        }
    })

    $('#r_btn').click(function () {
        $.ajax({
            method: 'POST',
            url: endpoint,
            data: {
                'username': $('#r_username').val(),
                'email': $('#r_email').val(),
                'password': $('#r_password').val(),
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            }
        });
    })
})