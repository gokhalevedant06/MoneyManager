$(document).ready(function () {
    $('#r_username').on('keyup', function () {
        $.ajax({
            url: endpoint,
            data: {
                'username': $(this).val(),
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
            },
        });
    })
    $('#r_email').on('keyup', function () {
        $.ajax({
            url: endpoint,
            data: {
                'email': $(this).val(),
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
            },
        });
    })

    $('#r_password').on('keyup', function () {
        if ($('#r_password').val() != $('#r_confirm_password').val()) {

            $('#r_confirm_password').removeClass('is-valid');
            $('#r_confirm_password').addClass('is-invalid');

            $('#r_password').removeClass('is-valid');
            $('#r_password').addClass('is-invalid');

            $('#r_btn').attr('disabled', true);
        }
        else {
            if ($('#r_password').val() != '' || $('#r_confirm_password').val() != '') {

                $('#r_confirm_password').removeClass('is-invalid');
                $('#r_confirm_password').addClass('is-valid');

                $('#r_password').removeClass('is-invalid');
                $('#r_password').addClass('is-valid');

                $('#valid_password').text("Password don't match !");

                $('#r_btn').attr('disabled', false);
            }
            else {
                $('#valid_password').text('Password Cannot be Empty !');
            }
        }
    })

    $('#r_confirm_password').on('keyup', function () {
        if ($('#r_password').val() != $('#r_confirm_password').val()) {

            $('#r_confirm_password').removeClass('is-valid');
            $('#r_confirm_password').addClass('is-invalid');

            $('#r_password').removeClass('is-valid');
            $('#r_password').addClass('is-invalid');

            $('#r_btn').attr('disabled', true);
        }
        else {
            if ($('#r_password').val() != '' || $('#r_confirm_password').val() != '') {

                $('#r_confirm_password').removeClass('is-invalid');
                $('#r_confirm_password').addClass('is-valid');

                $('#r_password').removeClass('is-invalid');
                $('#r_password').addClass('is-valid');

                $('#valid_password').text("Password don't match !");

                $('#r_btn').attr('disabled', false);
            }
            else {
                $('#valid_password').text('Password Cannot be Empty !');
            }
        }
    })

    $('#r_btn').on('click', function () {
        $.ajax({
            method: 'post',
            url: endpoint,
            data: {
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"'),
                'username': $('#r_username').val(),
                'email': $('#r_email').val(),
                'password': $('#r_password').val()
            },
            success: function (data) {
                window.location.replace('/');
            }
        });
    })
});
